import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils


class ScoreClientTest(utils.TestCommand):
    def setUp(self):
        super(ScoreClientTest, self).setUp()
        self.scenario_name = 'scenrio1'
        self.base_url = parse.urljoin(
            self.api_url,
            'scenarios/{}/scores'.format(self.scenario_name))
        self.score_json = {
            'score': 'test_score1',
            'date': '2018/01/2'
        }
        self.installer_name = 'installer'
        self.version_name = 'version'
        self.project_name = 'project'
        self.score_client = scenarios.ScoresClient()
        self.score_string = json.dumps(self.score_json)


class ScoreClientCreateTest(ScoreClientTest):

    def setUp(self):
        super(ScoreClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(
                self.base_url, self.score_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(
            data=self.succ_rsp)
        self.score_client.create(
            self.scenario_name, self.installer_name,
            self.version_name, self.project_name,
            self.score_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.score_client.create(
                self.scenario_name, self.installer_name,
                self.version_name, self.project_name,
                self.score_json)
