"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, have


@pytest.mark.desktop
def test_github_desktop(browser_resolution_desktop):
    if browser_resolution_desktop == (1920, 1080) or browser_resolution_desktop == (
    1024, 768) or browser_resolution_desktop == (1680, 1050):
        pytest.skip("Skip desktop test")
    browser.open('https://github.com')
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))


@pytest.mark.mobile
def test_github_mobile(browser_resolution_mobile):
    if browser_resolution_mobile == (768, 1280) or browser_resolution_mobile == (
    540, 960) or browser_resolution_mobile == (390, 844):
        pytest.skip("Skip mobile test")
    browser.open('https://github.com')
    browser.element(".HeaderMenu-toggle-bar").click()
    browser.element(".HeaderMenu-link--sign-in").click()
    browser.element(".auth-form-header").should(have.text("Sign in to GitHub"))
