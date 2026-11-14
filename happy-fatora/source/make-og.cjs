// Renders the 3 social share images (1200x630 JPG) from ./og/*.html
// Needs internet once so Google Fonts "Cairo" loads.   Usage: node make-og.cjs
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 }, deviceScaleFactor: 1 });
  for (const L of ['ar', 'en', 'fr']) {
    await p.goto('file://' + path.join(__dirname, 'og', `og-${L}.html`), { waitUntil: 'load', timeout: 15000 }).catch(() => {});
    await p.evaluate(() => document.fonts && document.fonts.ready);
    const fam = await p.evaluate(() => document.fonts.check('800 40px Cairo'));
    console.log(L, 'Cairo loaded:', fam);
    await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(__dirname, '..', 'site', 'images', `og-${L}.jpg`), type: 'jpeg', quality: 90 });
  }
  await b.close();
})();
