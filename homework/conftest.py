import pytest
from selene import browser


@pytest.fixture(params=[(1920, 1080), (1024, 768), (1680, 1050)])
def browser_resolution_desktop(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


@pytest.fixture(params=[(768, 1280), (540, 960), (390, 844)])
def browser_resolution_mobile(request):
    browser.config.window_width = request.param[0]
    browser.config.window_height = request.param[1]


def check_resolution_browser(request):
    resolution = request.param
    resolution_width, resolution_height = resolution
    browser.config.window_width = resolution_width
    browser.config.window_height = resolution_height
    if resolution == (1920, 1080) or resolution == (1024, 768) or resolution == (1680, 1050):
        return True
    else:
        pytest.skip("Skip desktop test")
