const { chromium } = require("playwright");

(async () => {

  const browser = await chromium.launch({
    headless: true
  });

  const page = await browser.newPage();

  // JSONレスポンスを待つ
  const responsePromise = page.waitForResponse(r =>
    r.url().includes("/charts/data/50108")
  );

  await page.goto(
    "https://en.macromicro.me/charts/50108/cnn-fear-and-greed",
    {
      waitUntil: "networkidle",
      timeout: 120000
    }
  );

  const response = await responsePromise;

  console.log("STATUS =", response.status());
  console.log("URL =", response.url());

  await browser.close();

})();
