import pytest

from ic import log


@pytest.fixture(autouse=True)
def log_started_test(request):
    log(f'\n{'-' * 10} {request.node.name}')
