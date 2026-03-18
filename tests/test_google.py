import re

from playwright.sync_api import expect

def test_google_serach(page):
    
    page.wait_for_timeout(5000)
    
    page.goto("https://www.google.com/")
    
    try:
        page.get_by_role("button", name="Accept all").click(timeout=5000)
    except:
        print("no popup found")    
        
    page.get_by_role("combobox", name="Search").fill("playwright")  
    
    page.keyboard.press("Enter") 
    
    expect(page).to_have_title(re.compile("playwright", re.IGNORECASE))
    
    

