import json

from mock import mock
from six.moves.urllib import parse

from testapiclient.cli import scenarios
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils


class ScoreTest(utils.TestCommand):
    def setUp(self):
        super(ScoreTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'scenarios/{}/scores')
        self.scenario_name = 's1'
        self.score_json = {
            'score': 'test_score1',
            'date': '2018/01/2'
        }
        self.score_string = json.dumps(self.score_json)


class ScoreCreateTest(ScoreTest):

    def setUp(self):
        super(ScoreCreateTest, self).setUp()

    def test_create_success(self):
        self.post_mock.return_value = fakes.FakeResponse(data=None)
        score_create = scenarios.ScoreCreate(self.app, mock.Mock())
        args = [
            '--scenario-name', 's1', '--installer', 'i1', '--version', 'v1',
            '--project', 'p1', self.score_string]
        verifies = [
            ('scenario_name', 's1'),
            ('installer', 'i1'),
            ('version', 'v1'),
            ('project', 'p1'),
            ('score', self.score_json)]
        parsed_args = self.check_parser(score_create, args, verifies)
        score_create.take_action(parsed_args)
        self.post_mock.assert_called_once()
