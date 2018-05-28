import json

from testapiclient.client import base
from testapiclient.utils import urlparse


class ResultsClient(base.Client):
    resource = 'results'

    def __init__(self, **kwargs):
        super(ResultsClient, self).__init__(**kwargs)

    def create(self, testcase_req):
        return self.clientmanager.post(self.url, testcase_req)

    def get(self, **queries):
        if queries:
            return json.dumps(
                self.clientmanager.get(
                    urlparse.query_join(self.url, **queries))['results'])
        else:
            return json.dumps(
                self.clientmanager.get(self.url)['results'])

    def get_one(self, id):
        return json.dumps(
            self.clientmanager.get(
                urlparse.path_join(self.url, id)))
