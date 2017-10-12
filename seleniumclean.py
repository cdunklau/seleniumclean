def clear_firefox_driver_session(firefox_driver):
    firefox_driver.delete_all_cookies()
    firefox_driver.execute_script('window.localStorage.clear();')

