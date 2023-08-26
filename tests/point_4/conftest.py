
def pytest_addoption(parser):
    """function for adding of command line options"""
    parser.addoption(
        "--url",
        action="append",
        default=["https://ya.ru"],
        help="string data of url to pass to test functions",
    )

    parser.addoption(
        "--status_code",
        action="append",
        default=[200],
        help="numeric status code values to pass to test functions",
    )


def pytest_generate_tests(metafunc):
    """hook for extracting CLI parameters and then passing them to the test"""
    if "url" in metafunc.fixturenames:
        metafunc.parametrize("url", metafunc.config.getoption("url"))

    if "status_code" in metafunc.fixturenames:
        metafunc.parametrize("status_code", metafunc.config.getoption("status_code"))
