import json

from mock import mock
from six.moves.urllib import parse

from testapiclient.cli import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils


class TrustIndicatorTest(utils.TestCommand):
    def setUp(self):
        super(TrustIndicatorTest, self).setUp()
        self.base_url = parse.urljoin(
            self.api_url,
            'scenarios/{}/trustindicators'
            )
        self.scenario_name = 's1'
        self.trust_indicator_json = {
            'status': 'test_status',
            'date': '2018/01/2'
        }
        self.trust_indicator_string = json.dumps(self.trust_indicator_json)


class TrustIndicatorCreateTest(TrustIndicatorTest):

    def setUp(self):
        super(TrustIndicatorCreateTest, self).setUp()

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(data=None)
        ti_create = scenarios.TrustIndicatorCreate(self.app, mock.Mock())
        args = [
            '--scenario-name', 's1', '--installer', 'i1', '--version', 'v1',
            '--project', 'p1', self.trust_indicator_string]
        verifies = [
            ('scenario_name', 's1'),
            ('installer', 'i1'),
            ('version', 'v1'),
            ('project', 'p1'),
            ('trust_indicator', self.trust_indicator_json)]
        parsed_args = self.check_parser(ti_create, args, verifies)
        ti_create.take_action(parsed_args)
        self.post_mock.assert_called_once()
