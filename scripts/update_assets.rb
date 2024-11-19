require 'fileutils'

# Directories
BLOG_DIR = './_posts'.freeze
ASSETS_DIR = './assets'.freeze
ASSETS_IMG_DIR = "#{ASSETS_DIR}/img".freeze

# Ensure target directories exist
FileUtils.mkdir_p(ASSETS_IMG_DIR)

# File extensions considered images
IMAGE_EXTENSIONS = %w[png jpg jpeg gif svg webp].freeze

# Process a single markdown file
def process_markdown_file(file_path)
  puts "[DEBUG] Processing file: #{file_path}"
  updated_content = []
  modified = false

  File.readlines(file_path).each_with_index do |line, line_number|
    updated_line = line

    # Log the current line being processed
    puts "[DEBUG] Line #{line_number + 1}: #{line.strip}"

    # Match both relative and absolute file references
    if line =~ /\[.*?\]\((\/?files\/.*?\.(\w+))\)/ || line =~ /!\[.*?\]\((\/?files\/.*?\.(\w+))\)/
      original_path = Regexp.last_match(1) # Extract original file path
      file_extension = Regexp.last_match(2) # Extract file extension
      file_name = File.basename(original_path) # Extract file name

      # Determine target directory
      if IMAGE_EXTENSIONS.include?(file_extension.downcase)
        target_dir = ASSETS_IMG_DIR
        new_markdown_path = "/assets/img/#{file_name}" # Absolute path
      else
        target_dir = ASSETS_DIR
        new_markdown_path = "/assets/#{file_name}" # Absolute path
      end

      source_path = "../blog#{original_path}" # Adjusted for absolute paths
      target_path = "#{target_dir}/#{file_name}"

      puts "[DEBUG] Found file reference: #{original_path} -> #{target_path}"

      # Copy file if it exists
      if File.exist?(source_path)
        puts "[DEBUG] File exists: #{source_path}. Copying..."
        FileUtils.mkdir_p(target_dir)
        FileUtils.cp(source_path, target_path)
        puts "[DEBUG] Copied #{source_path} to #{target_path}"
        updated_line = line.gsub(original_path, new_markdown_path)
        modified = true
      else
        puts "[WARNING] File not found: #{source_path}"
      end
    end

    updated_content << updated_line
  end

  # Update the file if modifications were made
  if modified
    File.open(file_path, 'w') { |f| f.puts(updated_content) }
    puts "[INFO] Updated references in #{file_path}"
  else
    puts "[INFO] No changes made to #{file_path}"
  end
end

# Process all Markdown files in the blog directory
Dir.glob("#{BLOG_DIR}/*.md").each do |markdown_file|
  process_markdown_file(markdown_file)
end

puts '[INFO] Processing complete!'
