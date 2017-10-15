import sys
import os
import os.path
import time
import subprocess

from selenium import webdriver
import pytest

here = os.path.abspath(os.path.dirname(__file__))


@pytest.fixture(scope='session')
def testapp_baseurl():
    flaskport = os.environ.get('SELENIUMCLEAN_TESTS_TESTAPP_PORT', '5000')
    env = {
        'FLASK_APP': os.path.join(here, 'testapp/app.py'),
        'LC_ALL': 'en_US.UTF-8',
        'LANG': 'en_US.UTF-8',
    }
    args = [sys.executable, '-m', 'flask', 'run', '-p', flaskport]
    app_process = subprocess.Popen(args, env=env)
    base_url = 'http://localhost:{port}'.format(port=flaskport)
    # Wait a bit to let it start
    time.sleep(5)
    try:
        yield base_url
    finally:
        app_process.terminate()
        try:
            app_process.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            app_process.kill()
            app_process.communicate()


@pytest.fixture(scope='session')
def storage_checker_url(testapp_baseurl):
    return testapp_baseurl + '/storage.html'


@pytest.fixture(scope='session')
def cookie_checker_url(testapp_baseurl):
    return testapp_baseurl + '/cookie.html'


@pytest.fixture(scope='session')
def firefox():
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
