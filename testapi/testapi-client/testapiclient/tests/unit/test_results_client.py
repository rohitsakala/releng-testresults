import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import results
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class ResultClientTest(utils.TestCommand):
    def setUp(self):
        super(ResultClientTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'results')
        self.result_json = {
            'project_name': 'functest',
            'scenario': 'test-scenario',
            'stop_date': '2018-04-09 13:44:53',
            'case_name': 'test-case',
            'build_tag': 'test-build',
            'version': 'test-version',
            'pod_name': 'test-pod',
            'criteria': 'test-criteria',
            'installer': 'test-installer',
            'start_date': '2018-04-09 13:44:53',
            'details': 'test-details'
        }
        self.result_id = '5a6dc1089a07c80f3c9f8d62'
        self.result_string = json.dumps(self.result_json)
        self.result_client = results.ResultsClient()


class ResultClientGetTest(ResultClientTest):

    def setUp(self):
        super(ResultClientGetTest, self).setUp()
        self.results_rsp = {'results': [self.result_json]}

    def test_get(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.results_rsp)
        self.result_client.get()
        self.get_mock.assert_called_once_with(
            self.base_url,
            headers=clientmanager.ClientManager.headers)

    def test_get_search(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.results_rsp)
        self.result_client.get(name='result1')
        self.get_mock.assert_called_once_with(
            self.base_url + '?name=result1',
            headers=clientmanager.ClientManager.headers)

    def test_get_one(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.result_json)
        self.result_client.get_one('2333')
        self.get_mock.assert_called_once_with(
            self.base_url + '/2333',
            headers=clientmanager.ClientManager.headers)


class ResultClientCreateTest(ResultClientTest):

    def setUp(self):
        super(ResultClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(self.base_url, self.result_id)
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(data=self.succ_rsp)
        self.result_client.create(self.result_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.result_client.create(self.result_json)
