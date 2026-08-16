import pytest
from playwright.sync_api import Page, expect

def test_practice_login(page: Page):
    # 1. Navigate to a stable, cloud-friendly practice site
    page.goto("https://practicetestautomation.com/practice-test-login/")
    
    # 2. Enter training credentials into the form input fields
    page.get_by_label("Username").fill("student")
    page.get_by_label("Password").fill("Password123")
    page.get_by_role("button", name="Submit").click()
    
    # 3. Assert that the successful login message appears on the next screen
    expect(page.get_by_role("heading")).to_contain_text("Logged In Successfully")