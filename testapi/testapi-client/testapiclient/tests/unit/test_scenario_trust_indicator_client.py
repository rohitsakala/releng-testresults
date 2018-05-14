import json

from six.moves.urllib import parse
import testtools

from testapiclient.client import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils


class TrustIndicatorClientTest(utils.TestCommand):
    def setUp(self):
        super(TrustIndicatorClientTest, self).setUp()
        self.scenario_name = 'scenrio1'
        self.base_url = parse.urljoin(
            self.api_url,
            'scenarios/{}/trust_indicators'.format(self.scenario_name))
        self.trust_indicator_json = {
            'status': 'test_status',
            'date': '2018/01/2'
        }
        self.installer_name = 'installer'
        self.version_name = 'version'
        self.project_name = 'project'
        self.trust_indicator_client = scenarios.TrustIndicatorsClient()
        self.trust_indicator_string = json.dumps(self.trust_indicator_json)


class TrustIndicatorClientCreateTest(TrustIndicatorClientTest):

    def setUp(self):
        super(TrustIndicatorClientCreateTest, self).setUp()
        self.succ_rsp = {
            'href': '{}/{}'.format(
                self.base_url, self.trust_indicator_json.get('name'))
        }

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(
            data=self.succ_rsp)
        self.trust_indicator_client.create(
            self.scenario_name, self.installer_name,
            self.version_name, self.project_name,
            self.trust_indicator_json)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            self.trust_indicator_client.create(
                self.scenario_name, self.installer_name,
                self.version_name, self.project_name,
                self.trust_indicator_json)
