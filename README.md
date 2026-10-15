# George Read: Personal Portfolio

Static website (no frameworks, no build step needed to host). 9 pages: Bio · Research · Projects · Experience · Skills · Community · Presentations · Courses · Certificates.
All 123 photos from `Photos.rar` are used (see `assets/img/MANIFEST.md` for where each one went).

## Publish on GitHub Pages
1. Create a repository on GitHub. For a clean URL name it `YOUR-USERNAME.github.io`, otherwise any name works.
2. Upload everything in this folder (the website uploader accepts ~100 files at a time, so use Git for all files):
   ```bash
   git init && git add . && git commit -m "Portfolio website"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPO.git
   git push -u origin main
   ```
3. On GitHub: **Settings → Pages → Build and deployment → Deploy from a branch → `main` / `(root)` → Save.**
4. After about a minute the site is live at `https://YOUR-USERNAME.github.io/` (or `/YOUR-REPO/`).

## Files that were not in the archive
The old site embeds Google Drive documents. Copy them into the folders below with the **same file names** and the site links to them automatically (until then the buttons open the old Google Sites page):
- `files/presentations/` : the 23 presentations listed on the Presentations page, `903139_Conferance Presentation.pptx`, and `SAAT_Book.pdf`
- `files/courses/` : `unofficial transcript - George Read.pdf`

Videos (2 YouTube embeds) and the resume (Google Drive preview) load from their original links.

## Editing
All text, links and photo assignments live in `content.py`. After editing run `pip install pillow qrcode[pil]` once, then
`PHOTOS=/path/to/Photos python build.py` (optionally `SITE_URL=https://you.github.io` for sitemap/social previews) and commit the result.
The photo-to-section assignments were made by looking at each image; move any photo by changing its id in `content.py` (`p12` = `unnamed (12).png`, `j12` = `unnamed (12).jpg`, `p0`/`j0` = `unnamed.png`/`unnamed.jpg`).
