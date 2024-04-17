import allure
import json
from allure_commons.types import AttachmentType


class Helper:

    def attach_response(self, response):
        resp_json_str = json.dumps(response, indent=4)
        allure.attach(body=resp_json_str, name="API Response", attachment_type=AttachmentType.JSON)