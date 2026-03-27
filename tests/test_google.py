import re
from playwright.sync_api import expect


def test_google_search(page):
    page.wait_for_timeout(1000)  # Wait for 1 second to ensure the page is fully loaded
    page.goto("https://www.google.com/ncr")
    
    try:
        page.get_by_role("button", name="I agree").click(timeout=5000)
    except:
        print("No cookie consent dialog found.")
        
    page.get_by_role("combobox", name="Search").fill("Playwright")
    page.keyboard.press("Enter")
    
    expect(page).to_have_title(re.compile("Playwright", re.IGNORECASE))
   
    
            
        
   