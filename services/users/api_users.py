from http import HTTPStatus
import allure
import requests
from services.users.models.user_model import UserModel
from services.users.payloads import Payloads
from services.users.endpoints import Endpoints
from config.headers import Headers
from utils.helper import Helper


class UsersAPI(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step("Create user")
    def create_user(self):
        response = requests.post(
            url=self.endpoints.create_user,
            headers=self.headers.basic,
            json=self.payloads.create_user
        )
        assert response.status_code == HTTPStatus.OK, response.json()
        self.attach_response(response.json())
        user_model = UserModel(**response.json())
        return user_model

    @allure.step("Get user by uuid")
    def get_user_by_uuid(self, uuid):
        response = requests.get(
            url=self.endpoints.get_user_by_uuid(uuid),
            headers=self.headers.basic
        )
        assert response.status_code == HTTPStatus.OK, response.json()
        self.attach_response(response.json())
        user_model = UserModel(**response.json())
        return user_model