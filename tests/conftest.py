from urllib.parse import urljoin

import pytest

pytest_plugins = "pytest_pulp_cli"


@pytest.fixture
def pulp_cli_vars(pulp_cli_vars):
    PULP_FIXTURES_URL = pulp_cli_vars["PULP_FIXTURES_URL"]
    result = {}
    result.update(pulp_cli_vars)
    result.update(
        {
            "OSTREE_REMOTE_URL": urljoin(PULP_FIXTURES_URL, "/ostree"),
        }
    )
    return result
