import os
from dotenv import load_dotenv
from playwright.sync_api import Browser, expect

load_dotenv()

def test_homepage_title(browser: Browser):
    context = browser.new_context(
        http_credentials={
            "username": os.getenv("TEST_USERNAME"),
            "password": os.getenv("TEST_PASSWORD"),
        }
    )
    new_page = context.new_page()
    new_page.goto(os.getenv("TEST_URL"))
    expect(new_page.locator("h1")).to_contain_text("Manage vaccinations in schools")
