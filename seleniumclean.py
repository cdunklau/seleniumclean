def clear_firefox_driver_session(firefox_driver):
    firefox_driver.delete_all_cookies()
    # Note this only works if the browser is set to a location.
    firefox_driver.execute_script('window.localStorage.clear();')

