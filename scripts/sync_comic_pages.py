#!/usr/bin/env python3
"""Regenerate comic pages and image lookups from _data/comics.json (no site build)."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def sync():
    comics = json.loads((ROOT / '_data/comics.json').read_text())
    urls = {comic['url']: comic for comic in comics}
    if len(urls) != len(comics) or len({c['slug'] for c in comics}) != len(comics):
        raise ValueError('Comic slugs and URLs must be unique')
    for comic in comics:
        if comic['url'] != f"/comics/{comic['slug']}/":
            raise ValueError(f"URL does not match slug: {comic['slug']}")
        if not (ROOT / comic['image'].lstrip('/')).is_file():
            raise ValueError(f"Missing original: {comic['image']}")
    lookup_path = ROOT / '_data/comic_images.json'
    old_lookup = json.loads(lookup_path.read_text()) if lookup_path.exists() else {}
    lookup = {}
    for asset, previous in old_lookup.items():
        if previous['url'] not in urls:
            raise ValueError(f"Image alias points to a missing comic: {asset}")
        comic = urls[previous['url']]
        lookup[asset] = {key: comic[key] for key in ('url', 'image', 'alt')}
    directory = ROOT / 'pages/comics'
    directory.mkdir(parents=True, exist_ok=True)
    thumbnails = ROOT / 'assets/comics/thumbnails'
    thumbnails.mkdir(parents=True, exist_ok=True)
    for comic in comics:
        original = ROOT / comic['image'].lstrip('/')
        thumbnail = thumbnails / (comic['slug'] + '.jpg')
        if not thumbnail.exists() or thumbnail.stat().st_mtime < original.stat().st_mtime:
            subprocess.run(['convert', str(original), '-auto-orient', '-thumbnail',
                            '640x800>', '-strip', '-quality', '85', str(thumbnail)], check=True)
        metadata = dict(layout='comic', title=comic['title'], permalink=comic['url'],
                        comic_slug=comic['slug'], image=comic['image'],
                        image_width=comic['width'], image_height=comic['height'],
                        excerpt=comic['alt'])
        page = '---\n' + '\n'.join(f'{k}: {json.dumps(v, ensure_ascii=False)}' for k, v in metadata.items()) + '\n---\n'
        (directory / (comic['slug'] + '.md')).write_text(page)
        lookup[comic['image']] = {key: comic[key] for key in ('url', 'image', 'alt')}
    lookup_path.write_text(json.dumps(lookup, indent=2, ensure_ascii=False, sort_keys=True) + '\n')
    print(f'Synchronised {len(comics)} comic pages and {len(lookup)} image paths')


if __name__ == '__main__':
    sync()
