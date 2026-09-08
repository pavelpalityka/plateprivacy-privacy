# Privacy policy site (PlatePrivacy)

Static multilingual privacy policy for **Google Play Console** and the in-app **About → Privacy Policy** link.

## Contents

| Path | Purpose |
|------|---------|
| `index.html` | Main page |
| `styles.css` | Layout (light/dark) |
| `app.js` | Language picker + JSON loader |
| `content/en.json` | English (canonical) |
| `content/ru.json` | Russian |
| `content/*.json` | Other app locales |
| `generate_content.py` | Regenerate fallback locales after editing `en.json` |
| `app-ads.txt` | Appodeal ads.txt (same developer account) |

## Google Play

1. Publish this folder to a **public HTTPS URL** (see hosting below).
2. In Play Console → **App content** → **Privacy policy**, paste that URL.
3. The app uses `https://pavelpalityka.github.io/plateprivacy-privacy/` in `AppSettings::privacyPolicyUrl()`.

Required because PlatePrivacy may use **Appodeal** advertising and **Google Play Billing**.
The policy mentions **IP address** and **advertising identifier (GAID)** and links to [Appodeal’s privacy policy](https://www.appodeal.com/privacy-policy).

## app-ads.txt

Place `app-ads.txt` at the **root of the developer website domain** listed in Google Play, for example:

`https://pavelpalityka.github.io/app-ads.txt`

Crawlers look at the domain root, not `…/plateprivacy-privacy/app-ads.txt`.

## Hosting (GitHub Pages)

1. Create a repo `pavelpalityka/plateprivacy-privacy` and push this folder.
2. **Settings → Pages → Deploy from branch** → `main`, folder `/` (root).
3. URL: `https://pavelpalityka.github.io/plateprivacy-privacy/`

4. Verify `?lang=ru` opens Russian text.

## Local preview

```bash
python -m http.server 8080
```

Open `http://localhost:8080/?lang=ru`

## Updating the policy

1. Edit `content/en.json` (and `ru.json` / `uk.json` if needed).
2. Run `python generate_content.py` to refresh fallback locales.
3. Redeploy the site.
4. Change the **Last updated** date in JSON files.

## Contact

Policy contact email: `pavelpalityka@gmail.com` (must match Play Console developer contact).
