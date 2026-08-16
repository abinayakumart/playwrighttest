import pytest
from playwright.sync_api import Page, expect

def test_practice_login(page: Page):
    # Ensure this full URL is exactly correct inside the quotes
    page.goto("https://herokuapp.com")
    
    page.locator("#username").fill("tomsmith")
    page.locator("#password").fill("SuperSecretPassword!")
    page.locator("button[type='submit']").click()
    
    expect(page.locator("#flash")).to_contain_text("You logged into a secure area!")
