import pytest
from selene import browser, have


@pytest.mark.desktop
@pytest.mark.parametrize('check_resolution_browser', [(1920, 1080), (1024, 768), (1680, 1050)], indirect=True)
def test_github_desktop(check_resolution_browser):
    browser.open('https://github.com')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.mobile
@pytest.mark.parametrize('check_resolution_browser', [(768, 1280), (540, 960), (390, 844)], indirect=True)
def test_github_mobile(check_resolution_browser):
    browser.open('https://github.com')
    browser.element(".HeaderMenu-toggle-bar").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
