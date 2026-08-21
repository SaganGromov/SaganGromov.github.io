# frozen_string_literal: true

require "pathname"
require "set"
require "uri"

root = Pathname(ARGV.fetch(0, "_site")).expand_path
required_pages = %w[
  index.html
  pesquisa/index.html
  textos/index.html
  recursos/index.html
  en/index.html
  en/research/index.html
  en/writing/index.html
  en/resources/index.html
  404.html
]
errors = []

required_pages.each do |relative_path|
  path = root.join(relative_path)
  unless path.file?
    errors << "#{relative_path}: missing generated page"
    next
  end

  html = path.read
  {
    "language" => /<html\s[^>]*lang="[^"]+"/,
    "title" => /<title>[^<]+<\/title>/,
    "viewport" => /<meta\s+name="viewport"/,
    "main landmark" => /<main(?:\s|>)/,
    "heading" => /<h1(?:\s|>)/,
  }.each do |label, pattern|
    errors << "#{relative_path}: missing #{label}" unless html.match?(pattern)
  end

  unless relative_path == "404.html"
    errors << "#{relative_path}: missing description" unless html.include?('<meta name="description"')
    errors << "#{relative_path}: missing canonical URL" unless html.include?('<link rel="canonical"')
  end

  ids = html.scan(/\sid="([^"]+)"/).flatten
  duplicates = ids.group_by(&:itself).select { |_id, entries| entries.length > 1 }.keys
  errors << "#{relative_path}: duplicate IDs #{duplicates.join(', ')}" unless duplicates.empty?

  html.scan(/(?:href|src)="([^"]+)"/).flatten.each do |reference|
    next unless reference.start_with?("/")
    next if reference.start_with?("//")

    clean = URI::DEFAULT_PARSER.unescape(reference.split(/[?#]/, 2).first)
    target = root.join(clean.delete_prefix("/"))
    target = target.join("index.html") if clean.end_with?("/")
    errors << "#{relative_path}: missing local target #{reference}" unless target.file?
  end

  html.scan(/<a\b[^>]*target="_blank"[^>]*>/).each do |tag|
    errors << "#{relative_path}: target=_blank without noopener" unless tag.match?(/rel="[^"]*noopener/)
  end
end

if errors.any?
  warn errors.map { |error| "- #{error}" }.join("\n")
  exit 1
end

puts "Checked #{required_pages.length} generated pages and their local targets."
