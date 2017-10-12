from seleniumclean import clear_firefox_driver_session


def get_cookie_report_text(driver):
    return driver.find_element_by_id('cookie-report').text.strip()


def test_cookies_cleared_in_firefox(firefox, cookie_checker_url):
    firefox.get(cookie_checker_url)
    clear_firefox_driver_session(firefox)
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


def test_local_storage_cleared_in_firefox(firefox, storage_checker_url):
    clear_firefox_driver_session(firefox)

    firefox.get(storage_checker_url)
    assert get_local_storage_report_text(firefox) == 'clear'
    firefox.get(storage_checker_url)
    assert get_local_storage_report_text(firefox) == 'not clear'

    clear_firefox_driver_session(firefox)
    firefox.get(storage_checker_url)
    assert get_local_storage_report_text(firefox) == 'clear'
