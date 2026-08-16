import pytest
from playwright.sync_api import Page, expect

def test_practice_login(page: Page):
    # 1. Navigate to a stable, automation-friendly practice website
    page.goto("https://herokuapp.com")
    
    # 2. Interact with the form using specific element IDs
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    
    # 3. Assert the success banner is visible
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")