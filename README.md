# Foking Good Nails

Website for [@foking.good.nails](https://www.instagram.com/foking.good.nails/), custom press-on nails from Vaughan, ON.

`index.html` is the whole site in one file (logo and photos are built in), so it can be hosted as-is on Vercel or GitHub Pages.

## What's on it
- **Home**: 3D nail case you can drag, plus a strip of her recent sets
- **Design**: 3D studio — pick style, colours, finish, shape, length and charms, see a price estimate, then order that design
- **Sets**: her real sets with filters and a big-photo view
- **Prices**: her price list with a live estimate and the nail card
- **Order**: add or take an inspo photo, a thumb-beside-a-coin photo, then send everything as one order card by email or Instagram DM
- **Contact**: Instagram links and order rules

## Editing
Edit `src/site.html`, then run:

```
python3 src/build.py
```

That rebuilds `index.html`. Photos live in `src/photos/`, the logo is `src/logo.webp`.

## Still needed before launch
- `ORDER_EMAIL` in `src/site.html` — the email orders get sent to (orders only preview until this is set)
- Original high-res logo file
- Her OK to use her Instagram photos
