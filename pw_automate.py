from playwright.sync_api import sync_playwright, expect, TimeoutError
from send_text import send_notification

URL_LINK = "https://rkgamingstore.com/collections/85-keyboards-89-keys/products/rk-royal-kludge-rk89-89-keys-mechanical-keyboard?variant=43033749455069"
blackKeyboardElement = "a.variant-color-btn:nth-child(3) > div:nth-child(1)"
brownKeysElement = ".product_variant_box > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > a:nth-child(3)"
popUpCancel = "svg.needsclick > circle:nth-child(2)"
submitButton = "div.product-form__controls-group:nth-child(2) > div:nth-child(1) > button:nth-child(1)"


timeDelay = 2000

def checkItem():
	with sync_playwright() as p:
		browser = p.firefox.launch(headless=False)
		page = browser.new_page()
		page.goto(URL_LINK)
		page.wait_for_timeout(timeDelay)
  
		print("Logging into Page")
  
		try:
			page.locator(popUpCancel).wait_for(state="visible", timeout=5000)
			print("Pop-up Appeared")
			page.locator(popUpCancel).click()
			print("Pop-up Removed")
			print("Now Clicking Keyboard Choices...")
		except TimeoutError:
			print("No Pop-Up. Going to Next Code")

	
		page.wait_for_timeout(timeDelay)
		page.locator(blackKeyboardElement).click()
		print("Black Keyboard Selected")
  
		page.wait_for_timeout(timeDelay)
		page.locator(brownKeysElement).click()
		print("Brown Keys Selected")
  
		try:
			keyboardUnavailable = page.get_by_role(role="button").filter(has_text="Sold out").is_visible()
			keyboardAvailable = page.get_by_role(role="button").filter(has_text="add To Cart").first.is_visible()
	
			if keyboardUnavailable:
				print("Keyboard is Unavailable")
				send_notification(message_="Keyboard is Unvailable")	
			elif keyboardAvailable:
				print("Keyboard is Availble")
				print("Sending notification")
				send_notification(message_="Keyboard is Available")
			else:
				print("Page has been Updated")
		except Exception as error:
			print(error)
		
		print("Terminating Code")
		page.wait_for_timeout(timeDelay)
		browser.close()
  
if __name__ == "__main__":
	checkItem()