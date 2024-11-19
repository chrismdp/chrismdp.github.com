require 'fileutils'

# Directories to process
DIRECTORIES = ['_posts', 'pages']

# Regex to match tag links
TAG_LINK_REGEX = /\[([^\]]+)\]\((?:http:\/\/[^)]+\/tag\/|\/tag\/)([^\)]+)\)/

# Method to slugify tags into kebab-case
def slugify(tag)
  tag.strip.downcase.gsub(/[^a-z0-9]+/, '-').gsub(/^-|-$/, '')
end

# Convert tag links in the content
def convert_tag_links(content)
  content.gsub(TAG_LINK_REGEX) do
    link_text = $1
    tag = $2
    slugified_tag = slugify(tag)
    "[#{link_text}](/tags##{slugified_tag})"
  end
end

# Process all Markdown files in the specified directories
DIRECTORIES.each do |dir|
  Dir.glob("#{dir}/*.md").each do |file|
    content = File.read(file)
    updated_content = convert_tag_links(content)

    if updated_content != content
      File.write(file, updated_content)
      puts "Updated: #{file}"
    else
      puts "No changes: #{file}"
    end
  end
end
