from playwright.sync_api import sync_playwright, expect, TimeoutError

URL_LINK = "https://rkgamingstore.com/collections/85-keyboards-89-keys/products/rk-royal-kludge-rk89-89-keys-mechanical-keyboard?variant=43033749455069"
blackKeyboardElement = "a.variant-color-btn:nth-child(3) > div:nth-child(1)"
brownKeysElement = ".product_variant_box > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > a:nth-child(3)"
popUpCancel = "svg.needsclick > circle:nth-child(2)"

timeDelay = 4000

def main():
	with sync_playwright() as p:
		browser = p.firefox.launch(headless=False)
		page = browser.new_page()
		page.goto(URL_LINK)
		page.wait_for_timeout(5000)
  
		try:
			expect(page.locator(popUpCancel)).to_be_visible()
			print("Popup appeared")
			page.locator(popUpCancel).click()
			print("Pop up removed")
			print("Now Clicking Keyboard Choices")
		except TimeoutError:
			print("No Pop-Up. Going to Next Code")

		page.locator(blackKeyboardElement).click()
		page.wait_for_timeout(timeDelay)
		page.locator(blackKeyboardElement).click()
		print("Chose Black Keyboard")
  
		page.locator(brownKeysElement).click()
		print("Chose Brown Keys")
  
		page.wait_for_timeout(timeDelay)
		browser.close()
  
if __name__ == "__main__":
    main()