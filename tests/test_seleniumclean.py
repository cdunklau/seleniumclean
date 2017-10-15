import pytest

from seleniumclean import clear_firefox_driver_session, LocationNotSet


def get_cookie_report_text(driver):
    return driver.find_element_by_id('cookie-report').text.strip()


def test_cookies_cleared_in_firefox(firefox, cookie_checker_url):
    # Need to be on a page before we clear
    firefox.get(cookie_checker_url)
    clear_firefox_driver_session(firefox)

    firefox.get(cookie_checker_url)
    assert get_cookie_report_text(firefox) == 'not seen'
    firefox.get(cookie_checker_url)
    assert get_cookie_report_text(firefox) == 'seen'

    clear_firefox_driver_session(firefox)
    firefox.get(cookie_checker_url)
    assert get_cookie_report_text(firefox) == 'not seen'


def get_local_storage_report_text(driver):
    return driver.find_element_by_id('local-storage-report').text.strip()


def get_session_storage_report_text(driver):
    return driver.find_element_by_id('session-storage-report').text.strip()


@pytest.mark.parametrize('get_report_text', [
    get_local_storage_report_text,
    get_session_storage_report_text,
])
def test_storage_cleared_in_firefox(
        firefox, storage_checker_url, get_report_text):
    # Need to be on a page before we clear
    firefox.get(storage_checker_url)
    clear_firefox_driver_session(firefox)

    firefox.get(storage_checker_url)
    assert get_report_text(firefox) == 'clear'
    firefox.get(storage_checker_url)
    assert get_report_text(firefox) == 'not clear'

    clear_firefox_driver_session(firefox)
    firefox.get(storage_checker_url)
    assert get_report_text(firefox) == 'clear'


@pytest.mark.xfail
def test_errors_if_location_not_set(firefox):
    with pytest.raises(LocationNotSet) as ctx:
        clear_firefox_driver_session(firefox)
