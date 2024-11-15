require 'yaml'

Dir.glob("_posts/*.{md,markdown}") do |filename|
  # Extract date and title from filename
  if filename =~ /(\d{4})-(\d{2})-(\d{2})-(.+)\.(md|markdown)/
    year, month, day, title = $1, $2, $3, $4

    # Construct the redirect URL based on the extracted data
    redirect_url = "/#{year}/#{month}/#{title}"

    # Read the file contents
    content = File.read(filename)
    
    # Parse the front matter
    if content =~ /\A(---\s*\n.*?\n?)^(---\s*$\n?)/m
      front_matter = YAML.safe_load($1, permitted_classes: [Time])
      body = $'

      # Add redirect_from if it doesn't already exist
      front_matter['redirect_from'] ||= []
      front_matter['redirect_from'] << redirect_url unless front_matter['redirect_from'].include?(redirect_url)

      # Write the updated content back to the file
      new_content = "#{front_matter.to_yaml}---\n#{body}"
      File.write(filename, new_content)
      puts "Updated #{filename} with redirect_from: #{redirect_url}"
    else
      puts "No front matter found in #{filename}"
    end
  else
    puts "Filename format does not match expected pattern: #{filename}"
  end
end
