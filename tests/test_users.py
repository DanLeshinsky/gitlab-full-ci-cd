import allure
import pytest

from config.base_test import BaseTest

@allure.epic("Administration")
@allure.feature("Users")
class TestUsers(BaseTest):

    @pytest.mark.users
    @allure.title("Create new user")
    def test_create_user(self):
        user = self.api_users.create_user()
        user_uuid = self.api_users.get_user_by_uuid(user.uuid)
        print(user_uuid)