"""
A small app to allow investigation of cookie and local/sessionStorage
status.

There are two endpoints.

/cookie.html

    Each response will inform of the cookie status of the incoming
    request, and include a Set-Cookie header to tell the browser
    to send a cookie on the next request.

    The report of cookie status is encoded in a <span> element
    with the ID "cookie-report". If the request was sent with the
    test cookie, the textContent of the <span> will be "seen",
    otherwise it will be "not seen". The parser should trim the
    text content before comparing equality.

/storage.html

    This is a static page that uses JavaScript to interrogate the
    status of sessionStorage and localStorage APIs in the browser,
    and set values in each that should be saved unless they are
    cleared by some other action.

    The status report is encoded in two <span> elements with the
    respective IDs "session-storage-report" and "local-storage-report".
    There are three possible values for the textContent of these
    elements. "unknown" means the JavaScript was not executed
    successfully, "clear" means the saved key was not found in the
    respective store, and "not clear" means the saved key was found.

"""
import os.path

from flask import (
    Flask,
    request,
    make_response,
    render_template,
    send_file,
)

here = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(here, 'templates'),
    static_folder=os.path.join(here, 'static'),
    static_url_path='',
)


@app.route('/')
def root():
    return 'try /cookie.html or /storage.html'


@app.route('/cookie.html')
def set_or_update_cookie():
    cookie_name = 'testcookie'
    cookie_seen = cookie_name in request.cookies
    response = make_response(
        render_template('cookie.jinja2', cookie_seen=cookie_seen),
    )
    response.set_cookie(cookie_name, 'somevalue', max_age=500)
    return response
