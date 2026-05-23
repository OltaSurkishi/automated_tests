from playwright.sync_api import sync_playwright

def test_search():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        print("STEP 1: Open website")
        page.goto("https://www.shopware6-demo.development-s25.com/")

        print("STEP 2: Wait for page load")
        page.wait_for_timeout(3000)

        print("STEP 3: Click search input")
        search_input = page.locator("#header-main-search-input")
        search_input.click()

        print("STEP 4: Enter keyword")
        search_input.fill("product")
        search_input.press("Enter")

        print("STEP 5: Validate results")
        page.wait_for_timeout(3000)

        results = page.locator(".product-box")

        if results.count() > 0:
            print("TEST PASSED: Search works correctly")
        else:
            print("TEST FAILED: No results found")

        browser.close()

test_search()