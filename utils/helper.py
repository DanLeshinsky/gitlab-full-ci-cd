import allure
import json
from allure_commons.types import AttachmentType

import requests



class Helper:

    def attach_response(selfself, response):
        resp_json_str = json.dumps(response, indent=4)
        allure.attach(body=resp_json_str, name="API Response", attachment_type=AttachmentType.JSON)