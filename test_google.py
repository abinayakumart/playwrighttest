import pytest
from playwright.sync_api import Page, expect

def test_google_search(page: Page):
    # 1. Navigate to the website
    page.goto("https://google.com")
    
    # 2. Interact with the page (Handle cookies if prompted, then type)
    # This searches for the search input box by its title attribute
    search_box = page.get_by_title("Search")
    search_box.fill("Playwright Python")
    search_box.press("Enter")
    
    # 3. Assert the result (Verify the title contains our keyword)
    expect(page).to_have_title(/Playwright Python/)
