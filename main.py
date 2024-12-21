from playwright.sync_api import sync_playwright

def main():
	with sync_playwright() as p:
		browser = p.firefox.launch(headless=False)
		page = browser.new_page()
		page.goto("https://rkgamingstore.com/collections/85-keyboards-89-keys/products/rk-royal-kludge-rk89-89-keys-mechanical-keyboard?variant=43033749455069")
		page.wait_for_timeout(3000)
		browser.close()
  
if __name__ == "__main__":
    main()