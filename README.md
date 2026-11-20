# Kerdos website

Live at https://kerdos.sgdventures.com (Netlify site "adspendcheck").

- `site/`: the published static site (Netlify publishes this folder, see netlify.toml).
- `src/`: generators. Edit `src/build.py` / `src/build_extra.py`, then run `python3 src/build_extra.py` to rebuild `site/`, commit and push to `main`: Netlify deploys automatically once the repo is linked.
