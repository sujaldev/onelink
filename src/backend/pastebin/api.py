import json
import requests
from env import api_key
from pastebin_exceptions import *
from urllib.parse import urlparse


class API:
    GET_ENDPOINT = "https://pastebin.com/raw/"

    POST_ENDPOINT = "https://pastebin.com/api/api_post.php"
    POST_DATA_TEMPLATE = {
        # required
        "api_dev_key": api_key,
        "api_option": "paste",
        "api_paste_code": "",  # actual data to be pasted (present here just for verbosity, will be overridden)

        # optional
        "api_paste_private": 1,  # 1 sets as unlisted
        "api_paste_expire_date": "N"  # Never expire by default
    }

    ACCEPTED_EXPIRE_VALUES = ("N", "10M", "1H", "1D", "1W", "2W", "1M", "6M", "1Y")

    def __init__(self):
        self.session = requests.Session()

    def __create_post_data(self, data, expire=None):
        post_data = self.POST_DATA_TEMPLATE.copy()
        post_data["api_paste_code"] = data

        if expire is not None:
            if expire in self.ACCEPTED_EXPIRE_VALUES:
                post_data["api_paste_expire_date"] = expire
            else:
                raise PastebinInvalidExpireParameter

        return post_data

    @staticmethod
    def __parse_post_response(response):
        copy_link = response.content.decode()
        copy_code = urlparse(copy_link).path.lstrip("/")
        return copy_code

    def paste(self, data, expire=None):
        response = self.session.post(
            url=self.POST_ENDPOINT,
            data=self.__create_post_data(data, expire)
        )

        if response.ok:
            return self.__parse_post_response(response)
        else:
            raise PastebinServerOrClientError(response.status_code)

    def copy(self, copy_code):
        url = self.GET_ENDPOINT + copy_code
        response = self.session.get(url)

        if response.ok:
            parsed_json = json.loads(response.content)
            return parsed_json
        else:
            raise PastebinServerOrClientError(response.status_code)
