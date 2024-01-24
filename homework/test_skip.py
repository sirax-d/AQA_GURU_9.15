"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.mark.desktop
def test_github_desktop(check_resolution_browser):
    if not check_resolution_browser:
        pytest.skip("Desktop test")
    browser.open('https://github.com')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.mobile
def test_github_mobile(check_resolution_browser):
    if check_resolution_browser:
        pytest.skip("Mobile test")
    browser.open('https://github.com')
    browser.element(".HeaderMenu-toggle-bar").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
