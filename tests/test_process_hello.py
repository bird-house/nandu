import json
from http import HTTPStatus

from pygeoapi.api.processes import (
    execute_process,
)

from tests.util import mock_api_request


def test_process_hello_world(api_):
    req_body_sync = {"inputs": {"name": "Nandu"}}

    req = mock_api_request(data=req_body_sync)
    rsp_headers, code, response = execute_process(api_, req, "hello-world")

    data = json.loads(response)
    assert code == HTTPStatus.OK
    assert data["value"] == "Hello Nandu!"
