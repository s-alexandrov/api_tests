import logging
import pytest
from fixtures.app import App
from fixtures.common_models import UserStore
from fixtures.register.model import RegisterModel, RegisterUserResponse

logger = logging.getLogger("api")


def pytest_addoption(parser):
    parser.addoption(
        "--api-url",
        action="store",
        help="enter api url",
        default="https://stores-tests-api.herokuapp.com",
    )


@pytest.fixture
def app(request):
    url = request.config.getoption('--api-url')
    logger.info(f"Start api tests, url is {url}")
    return App(url)


@pytest.fixture
def user(app) -> UserStore:
    data = RegisterModel.random()
    res = app.register.new_register(data=data, type_response=RegisterUserResponse)
    uuid = res.data.uuid
    assert res.status_code == 201
    return UserStore(user = data, user_uuid=uuid)


@pytest.fixture
def auth_user(app, user) -> UserStore:
    res_login = app.login.login_user(data=user.user)
    token = res_login.data.access_token
    header = {"Authorization": f"JWT {token}"}
    return UserStore(user = user.user, user_uuid=user.user_uuid, header=header)
