import pytest

from pygeoapi.api import API
from pygeoapi.util import yaml_load

from tests.util import get_test_file_path


@pytest.fixture()
def config():
    with open(get_test_file_path("pygeoapi-test-config.yml")) as fh:
        return yaml_load(fh)


@pytest.fixture()
def openapi():
    with open(get_test_file_path("pygeoapi-test-openapi.yml")) as fh:
        return yaml_load(fh)


@pytest.fixture()
def api_(config, openapi):
    return API(config, openapi)
