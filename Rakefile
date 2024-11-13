rule '.html' => [ proc { |name| name.sub(/\.html/,'_haml.haml') } ] do |t|
  sh %{ haml -E utf-8 #{t.source} #{t.name.sub(/_haml\./,'.')} }
end

rule '.css' => ['.scss'] do |t|
    sh %{ sass -t compressed #{t.source} #{t.name} }
end

task :tag do
  raise "Doesn't exist"
end

task :cloud do
  puts 'Generating tag cloud...'
  require 'rubygems'
  require 'jekyll'
  include Jekyll::Filters

  options = Jekyll.configuration({})
  site = Jekyll::Site.new(options)
  site.read


  html =<<-HTML
---
layout: default
title: Tags
type: A tag cloud
---
<div class='hero-unit'>
  <p>
    <a href='{{ site.url }}'>a blog by Chris Parsons</a>
  </p>
  <h1>
   Tag cloud
  </h1>
</div>
<hr />
<div class='row' id='post'>
  <div class='col-sm-8'>
      <p>Click on a tag to see the relevant posts.</p>
      <ul class='tags'>
  HTML

  site.categories.sort.each do |category, posts|
    next if category == ".net"
    html << <<-HTML
    HTML

    s = posts.count
    font_size = 12;
    html << "<li><a class='tag' href=\"/tag/#{category}/\" title=\"Entries tagged #{category}\" style=\"font-size: #{font_size}px;\">#{category}</a></li>"
  end

  html << <<-HTML
  </ul>
  <br/><br/>
  </div>

  <div class='sidebar col-sm-4'>
    <div class='widget'>
      <ul class='list-unstyled'>
        <li>
          <i class='icon-chevron-right'></i>
          <a href='/all'>Archives</a>
        </li>
      </ul>
    </div>
  </div>
  </div>
  HTML


  File.open('tags/index.html', 'w+') do |file|
    file.puts html
  end

  puts 'Done.'
end

def build_atom_feed(category, posts)
  html = ''
  html << <<-HTML
---
layout: null
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
    html += "<entry>\n"
    html += "<title>#{post_data['title']}</title>\n"
    post_data.fetch('categories').each do |post_category|
      html += "<category term='#{post_category}'/>\n"
    end
    html += <<-HTML
    <author>
      <name>Chris</name>
      <email>chrismdp@gmail.com</email>
    </author>
    HTML
    html += "<link href='http://chrismdp.com#{ post_data['url'] }'/>\n"
    html += "<updated>#{ post_data['date'].xmlschema}</updated>\n"
    html += "<id>http://chrismdp.com#{ post_data['id'] }</id>\n"
    html += "<content type='html'>{% for post in site.posts %}{% if post.id == \"#{ post_data['id']}\" %}{{ post.content | xml_escape }}{% endif %}{% endfor %}</content>\n"
    html += "</entry>\n"
  end
  html += "</feed>\n"
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
<div class='hero-unit'>
  <p>
    <a href='{{ site.url }}'>a blog by Chris Parsons</a>
  </p>
  <h1>
    Posts tagged "#{category}"
  </h1>
</div>
<hr />
<div class='row' id='post'>
  <div class='col-sm-8'>
  HTML

  posts.each do |post|
    post_data = post.to_liquid
    html << <<-HTML
<article class="post">
  <div class="entry-body">
    <a href="#{post.url}">
      <h2 class="entry-title">#{post_data['title']}</h2>
    </a>
  </div>
  <div class="entry-meta">
    <span class="entry-date">#{post_data['date'].strftime("%d %b %Y")}</span>
  </div>
</article>
    HTML
  end
  html << <<-HTML
  </div>
  <div class='col-sm-4 sidebar'>
    <div class='widget'>
      <ul class='list-unstyled'>
        <li>
          <i class='icon-chevron-right'></i>
          <a href='/all'>Archives</a>
        </li>
        <li>
          <i class='icon-chevron-right'></i>
          <a href='/tags'>All Categories</a>
        </li>
      </ul>
    </div>
  </div>
  </div>
  HTML

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
  site.read
  site.categories.sort.each do |category, posts|
    next if category == ".net"

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
