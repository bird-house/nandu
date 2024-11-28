# =================================================================
#
# TODO: This is based on pygeoapi.tests.util.py
#
# =================================================================


import logging
import os.path

from werkzeug.test import create_environ
from werkzeug.wrappers import Request
from werkzeug.datastructures import ImmutableMultiDict

from pygeoapi.api import APIRequest


def get_test_file_path(filename: str) -> str:
    """helper function to open test file safely"""

    if os.path.isfile(filename):
        return filename
    else:
        return f"tests/{filename}"


def mock_request(params: dict = None, data=None, **headers) -> Request:
    """
    Mocks a Request object so the @pre_process decorator can inject it
    as an APIRequest.

    :param params: Optional query parameter dict for the request.
                   Will be set to {} if omitted.
    :param data: Optional data/body to send with the request.
                 Can be text/bytes or a JSON dictionary.
    :param headers: Optional request HTTP headers to set.
    :returns: A Werkzeug Request instance.
    """
    params = params or {}
    # TODO: We are not setting a path in the create_environ() call.
    #       This is fine as long as an API test does not need the URL path.
    if isinstance(data, dict):
        environ = create_environ(base_url="http://localhost:5000/", json=data)
    else:
        environ = create_environ(base_url="http://localhost:5000/", data=data)
    environ.update(headers)
    request = Request(environ)
    request.args = ImmutableMultiDict(params.items())  # noqa
    return request


def mock_api_request(params: dict | None = None, data=None, **headers) -> APIRequest:
    """
    Mocks an APIRequest

    :param params: Optional query parameter dict for the request.
                   Will be set to {} if omitted.
    :param data: Optional data/body to send with the request.
                 Can be text/bytes or a JSON dictionary.
    :param headers: Optional request HTTP headers to set.
    :returns: APIRequest instance
    """
    return APIRequest.from_flask(
        mock_request(params=params, data=data, **headers),
        # NOTE: could also read supported_locales from test config
        supported_locales=["en-US", "fr-CA"],
    )
