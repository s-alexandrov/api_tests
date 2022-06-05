import attr

from fixtures.base import BaseClass
from fixtures.register.model import RegisterModel
from fixtures.user_info.model import UserInfoRequest


@attr.s
class MessageResponse:
    message: str = attr.ib()


@attr.s
class UserStore(BaseClass):
    user: RegisterModel = attr.ib(default=None)
    user_uuid: int = attr.ib(default=None)
    header: dict = attr.ib(default=None)
    user_info: UserInfoRequest = attr.ib(default=None)
