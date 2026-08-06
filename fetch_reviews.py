import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        print("Navigating...")
        await page.goto('https://share.google/gRYasnxQULCMfPzk6')
        
        # Wait for the page to load, wait for network idle
        await page.wait_for_load_state("networkidle")
        await page.wait_for_timeout(5000)
        
        print("Current URL:", page.url)
        
        body_text = await page.evaluate('document.body.innerText')
        with open('reviews_dump.txt', 'w', encoding='utf-8') as f:
            f.write(body_text)
            
        print("Dumped text to reviews_dump.txt")
        await browser.close()

asyncio.run(main())
