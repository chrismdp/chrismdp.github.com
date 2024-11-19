require 'fileutils'
require 'nokogiri'

POSTS_DIR = '_posts'
ALERT_REGEX = /<div class=['"]alert(?: alert-(\w+))?(?: alert-block)?['"]>(.*?)<\/div>/m

def strip_html(content)
  Nokogiri::HTML(content).text.strip
end

def convert_alerts_to_callouts(content)
  content.gsub(ALERT_REGEX) do
    # Determine color based on the alert type
    color = case $1
            when 'info' then '#d9edf7'
            when 'success' then '#dff0d8'
            when 'warning' then '#fcf8e3'
            when 'danger' then '#f2dede'
            else '#f5f5f5' # default color for unspecified alerts
            end

    # Extract and clean up the inner content
    inner_content = strip_html($2.strip).gsub('"', '\"') # Escape double quotes for Liquid syntax
    "{% include callout.html color=\"#{color}\" text=\"#{inner_content}\" %}"
  end
end

Dir.glob("#{POSTS_DIR}/*.md").each do |file|
  content = File.read(file)
  updated_content = convert_alerts_to_callouts(content)

  if updated_content != content
    File.write(file, updated_content)
    puts "Updated: #{file}"
  else
    puts "No changes: #{file}"
  end
end
