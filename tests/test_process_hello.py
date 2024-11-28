from http import HTTPStatus

from pygeoapi.api import FORMAT_TYPES, F_HTML, F_JSON
from pygeoapi.api.processes import (
    describe_processes,
    execute_process,
    delete_job,
    get_job_result,
    get_jobs,
)

from tests.util import mock_api_request


def test_process_hello_world(api_):
    # Check JSON response when requested in headers
    req = mock_api_request(HTTP_ACCEPT="application/json")
    rsp_headers, code, response = describe_processes(api_, req, "hello-world")
    assert code == HTTPStatus.OK
    assert rsp_headers["Content-Type"] == FORMAT_TYPES[F_JSON]
    assert rsp_headers["Content-Language"] == "en-US"
