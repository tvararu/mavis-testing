from playwright.sync_api import Page, expect

def test_homepage_title(page: Page):
    page.goto("https://test.mavistesting.com")
    expect(page).to_have_title("Manage vaccinations in schools")
