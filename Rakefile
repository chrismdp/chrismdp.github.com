task :cloud_basic do
    puts 'Generating tag cloud...'
    require 'rubygems'
    require 'jekyll'
    include Jekyll::Filters

    options = Jekyll.configuration({})
    site = Jekyll::Site.new(options)
    site.read_posts('')

    html = ''

    site.categories.sort.each do |category, posts|

      s = posts.count
      font_size = 12 + (s*1.2);
      html << "<a href=\"/tag/#{category}/\" title=\"Pages tagged #{category}\" style=\"font-size: #{font_size}px; line-height:#{font_size}px\" rel=\"tag\">#{category}</a> "
    end

    File.open('_includes/tags.html', 'w+') do |file|
      file.puts html
    end

    puts 'Done.'
  end


task :cloud do
  puts 'Generating tag cloud...'
  require 'rubygems'
  require 'jekyll'
  include Jekyll::Filters

  options = Jekyll.configuration({})
  site = Jekyll::Site.new(options)
  site.read_posts('')


  html =<<-HTML
---
layout: default
title: Tags
type: A tag cloud
---
<div id="home">
  <div id="current" class="post">
    <div id="post" class="post">
      <h1><a>tag cloud</a></h1>

      <p>Click on a tag to see the relevant posts.</p>
  HTML

  site.categories.sort.each do |category, posts|
    next if category == ".net"
    html << <<-HTML
    HTML

    s = posts.count
    font_size = 12 + (s*1.5);
    html << "<a class='tag' href=\"/tag/#{category}/\" title=\"Entries tagged #{category}\" style=\"font-size: #{font_size}px; line-height:#{font_size}px\">#{category}</a> "
  end

  html << "<p>You may also wish to browse the <a href=\"/all/\" title=\"Archives for {{site.title}}\">archives</a>.</div></div></div>"


  File.open('tags/index.html', 'w+') do |file|
    file.puts html
  end

  puts 'Done.'
end

def build_atom_feed(category, posts)
  html = ''
  html << <<-HTML
---
layout: nil
---
<?xml version="1.0" encoding="utf-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">

  <title>Chris Parsons: posts tagged #{category}</title>

  <link href="http://chrismdp.com/"/>
  <updated>#{ posts.first.to_liquid['date'].xmlschema }</updated>
  <id>http://chrismdp.com/tag/#{category}</id>
  <author>
    <name>Chris</name>
    <email>chrismdp@gmail.com</email>
  </author>
  HTML
  posts.each.with_index do |post, index|
    post_data = post.to_liquid
    html += "<entry>"
    html += "<title>#{post_data['title']}</title>"
    post.categories.each do |post_category|
      html += "<category term='#{post_category}'/>"
    end
    html += <<-HTML
    <author>
      <name>Chris</name>
      <email>chrismdp@gmail.com</email>
    </author>
    HTML
    html += "<link href='http://chrismdp.com#{ post_data['url'] }'/>"
    html += "<updated>#{ post_data['date'].xmlschema}</updated>"
    html += "<id>http://chrismdp.com#{ post_data['id'] }</id>"
    html += "<content type='html'>{% for post in site.posts %}{% if post.id == \"#{ post_data['id']}\" %}{{ post.content | xml_escape }}{% endif %}{% endfor %}</content>"
    html += "</entry>"
  end
  html += "</feed>"
  html
end

def build_tag_page(category, posts)
  html = ''
  html << <<-HTML
---
layout: default
title: Entries tagged "#{category}"
type: "#{category.gsub(/\b\w/){$&.upcase}}"
---
<div id="home">
  <div id="current" class="post">
    <div id="post" class="post">
    <h1 id="#{category}"><a>entries tagged "#{category}"</a></h1>
    <p>&laquo; <a href="/tags/" title="Tag cloud for {{site.title}}">show all tags</a></p>
  HTML

  html << '<ul class="posting_list">'
  posts.each do |post|
    post_data = post.to_liquid
    html << <<-HTML
        <li>
          <span>#{post_data['date'].strftime("%d %b %Y")}</span> &raquo; <a href="#{post.url}">#{post_data['title']}</a>
          <div class='strap'>#{ post.categories.map {|tag| "<a class='tag' href='/tag/#{tag}/'>#{tag}</a>" }.join(' ') }</div>
        </li>
    HTML
  end
  html << '</ul>'

  html << '<p>You may also be interested in browsing the <a href="/all/" title="Archives">archives</a> or seeing <a href="/tags/" title="Tag cloud">the tag cloud</a>.</div></div></div>'
  html
end

desc 'Generate tags page'
task :tags do
  puts "Generating tags..."
  require 'rubygems'
  require 'jekyll'
  include Jekyll::Filters

  options = Jekyll.configuration({ 'markdown' => 'kramdown' })
  site = Jekyll::Site.new(options)
  site.read_posts('')
  site.categories.sort.each do |category, posts|
    next if category == ".net"

    posts.reverse!

    FileUtils.mkdir_p "tag/#{category}"

    File.open("tag/#{category}/index.html", 'w+') do |file|
      file.puts build_tag_page(category, posts)
    end

    File.open("tag/#{category}/atom.xml", 'w+') do |file|
      file.puts build_atom_feed(category, posts)
    end
  end
  puts 'Done.'
end
