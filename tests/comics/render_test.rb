# Render selected templates in memory; this does not build or write the site.
require 'jekyll'
require 'json'
require 'nokogiri'
require 'fileutils'

def check(condition, message)
  raise message unless condition
end
site = Jekyll::Site.new(Jekyll.configuration('source' => Dir.pwd, 'destination' => '/tmp/comic-tests-unused', 'quiet' => true))
site.reset
site.read
comics = site.data['comics']
check(comics.size > 1, 'Missing catalogue')
check(comics.map { |c| c['slug'] }.uniq.size == comics.size, 'Duplicate slugs')
preview = ENV['COMIC_PREVIEW_DIR']
FileUtils.mkdir_p(preview) if preview
comics.each_with_index do |comic, index|
  page = site.pages.find { |p| p.url == comic['url'] }
  check(page, "Missing page: #{comic['slug']}")
  output = Jekyll::Renderer.new(site, page).run
  doc = Nokogiri::HTML(output)
  check(doc.at_css('link[rel=canonical]')['href'] == site.config['url'] + comic['url'], 'Incorrect canonical')
  image = doc.at_css('.comic-art')
  check(image['src'] == comic['image'], 'Incorrect original')
  check(File.exist?('.' + image['src']), 'Missing original')
  check(image['width'].to_i == comic['width'] && image['height'].to_i == comic['height'], 'Incorrect dimensions')
  check(doc.css('.comic-nav a[rel=prev]').map { |a| a['href'] } == (index > 0 ? [comics[index-1]['url']] * 2 : []), 'Incorrect previous link')
  check(doc.css('.comic-nav a[rel=next]').map { |a| a['href'] } == (index < comics.size-1 ? [comics[index+1]['url']] * 2 : []), 'Incorrect next link')
  check(doc.css('[data-random-comic]').size == 2, 'Missing random buttons')
  if preview && [0, comics.size/2, comics.size-1].include?(index)
    path = File.join(preview, comic['url'], 'index.html')
    FileUtils.mkdir_p(File.dirname(path))
    File.write(path, output)
  end
end
catalogue_page = site.pages.find { |p| p.url == '/comics/index.json' }
check(JSON.parse(Jekyll::Renderer.new(site, catalogue_page).run) == comics.map { |c| c['url'] }, 'Random catalogue mismatch')
archive = site.pages.find { |p| p.url == '/comics/' }
archive_html = Jekyll::Renderer.new(site, archive).run
check(Nokogiri::HTML(archive_html).css('.comic-archive li a').size == comics.size, 'Archive omits comics')
if preview
  FileUtils.mkdir_p(File.join(preview, 'comics'))
  File.write(File.join(preview, 'comics/index.html'), archive_html)
  File.write(File.join(preview, 'comics/index.json'), JSON.generate(comics.map { |c| c['url'] }))
  asset_link = File.join(preview, 'assets')
  File.symlink(File.join(Dir.pwd, 'assets'), asset_link) unless File.exist?(asset_link)
end
# Exercise hero, inline-include and raw HTML images through actual post rendering.
affected_posts = site.posts.docs.select do |post|
  site.data['comic_images'].key?(post.data['image']) || site.data['comic_images'].keys.any? { |path| post.content.include?(path) }
end
affected_posts.each do |post|
  filename = File.basename(post.path)
  output = Jekyll::Renderer.new(site, post).run
  doc = Nokogiri::HTML(output)
  images = doc.css('article img').select { |img| site.data['comic_images'].key?(img['src']) }
  check(!images.empty?, "No comics tested in #{filename}")
  images.each do |img|
    comic = site.data['comic_images'][img['src']]
    check(img['src'] == comic['image'], "Resized image in #{filename}")
    check(img.ancestors('a').first&.[]('href') == comic['url'], "Unlinked comic in #{filename}")
  end
end
site.pages.select { |p| p.data['layout'] == 'page' && site.data['comic_images'].key?(p.data['image']) }.each do |page|
  doc = Nokogiri::HTML(Jekyll::Renderer.new(site, page).run)
  comic = site.data['comic_images'][page.data['image']]
  check(doc.css('a').any? { |a| a['href'] == comic['url'] && a.at_css('img')&.[]('src') == comic['image'] }, "Unlinked page hero: #{page.url}")
end
puts "PASS: #{affected_posts.size} posts with comics and comic page heroes"
puts "PASS: #{comics.size} comic pages, archive, random catalogue, boundary navigation and blog embeds"
