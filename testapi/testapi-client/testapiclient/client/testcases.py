import json

from testapiclient.client import base
from testapiclient.utils import urlparse


class TestcasesClient(base.Client):
    resource = 'projects/{}/cases'

    def __init__(self, **kwargs):
        super(TestcasesClient, self).__init__(**kwargs)

    def create(self, project_name, testcase_req):
        return self.clientmanager.post(
            self.url.format(project_name), testcase_req)

    def get(self, project_name):
        return json.dumps(
            self.clientmanager.get(
                self.url.format(project_name))['testcases'])

    def get_one(self, project_name, name):
        return json.dumps(
            self.clientmanager.get(
                urlparse.path_join(
                    self.url.format(project_name), name)))

    def delete(self, project_name, name):
        return self.clientmanager.delete(
            urlparse.path_join(
                self.url.format(project_name), name))

    def update(self, project_name, name, testcase_req):
        return self.clientmanager.put(
            urlparse.path_join(
                self.url.format(project_name), name), testcase_req)
