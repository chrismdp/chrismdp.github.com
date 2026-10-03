# Comic archive

`_data/comics.json` is the ordered catalogue, oldest first. Each entry has a stable
`slug`, `title`, `/comics/<slug>/` URL, full-resolution `image`, actual pixel `width`
and `height`, descriptive `alt` text and the Vault `source_id`.

To add a comic:

1. Download the original from the Newsletter Vault Comics folder
   (`1GGQoswjRVrsJxQ_s0ugna0tAw5n3-heB`) using `gog drive download <id> --out <path>`.
   Save it as `assets/comics/<title-slug>.<extension>` without resizing or recompressing.
2. Append its entry to `_data/comics.json`. Use a lowercase, hyphenated slug based on
   the title. Keep that URL stable after publication, even if the title changes.
3. Run `python3 scripts/sync_comic_pages.py`. This creates the Jekyll page and updates
   the image lookup and generates lightweight archive thumbnails with ImageMagick
   (`convert`). The originals stay full resolution. Navigation, the archive and the random catalogue use the data
   file automatically; no plugin or Jekyll configuration change is needed.
4. Embed the catalogue image via `inline-image.html` or a post's `image:` field.
   Both templates link catalogue images to their comic page and use the original.
   Raw HTML and Markdown images need an explicit link to the comic page.
5. In newsletters, embed the full-resolution original and set its click-through to
   `https://www.chrismdp.com/comics/<slug>/`. Link readers to that page.

`_data/comic_images.json` also maps older blog image paths to their originals and
canonical pages. Preserve these aliases. When adding an alias, copy the target
comic's `url`, `image` and `alt`; the synchronisation script refreshes its metadata.

Checks (template rendering only; no Jekyll build or server):

```sh
bundle exec ruby tests/comics/render_test.rb
node tests/comics/random_test.js
```

Set `COMIC_PREVIEW_DIR=/tmp/comic-preview` for the Ruby check to save a few rendered
examples for browser inspection. This does not write to `_site`.
