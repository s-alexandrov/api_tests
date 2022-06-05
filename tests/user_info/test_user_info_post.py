from fixtures.user_info.model import UserInfoRequest


class TestLogin:
    def test_valid_add_user_info(self, app, auth_user):
        """
        Precondition: Register new user
        2. Login user from step 1
        3. Try to add info about user
        4. Check status code is 200
        """
        data_user = UserInfoRequest.random()
        user_info_response = app.user_info.add_user_info(user_id=auth_user.user_uuid, data=data_user,
                                                         header=auth_user.header, type_response=None)
        assert user_info_response.status_code == 200
