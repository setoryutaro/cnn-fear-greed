const { chromium } = require("playwright");

(async () => {

  const browser = await chromium.launch({
    headless: true
  });

  const page = await browser.newPage();

  await page.goto(
    "https://en.macromicro.me/charts/50108/cnn-fear-and-greed",
    {
      waitUntil: "domcontentloaded",
      timeout: 30000
    }
  );

  console.log("TITLE =", await page.title());

  console.log("URL =", page.url());

  console.log(await page.content());

  await browser.close();

})();
