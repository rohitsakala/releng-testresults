import json

from mock import mock
from six.moves.urllib import parse
import testtools

from testapiclient.cli import projects
from testapiclient.tests.unit import fakes
from testapiclient.tests.unit import utils
from testapiclient.utils import clientmanager


class ProjectTest(utils.TestCommand):
    def setUp(self):
        super(ProjectTest, self).setUp()
        self.base_url = parse.urljoin(self.api_url, 'projects')
        self.project_json = {
            'name': 'test_project',
            'description': ''
        }
        self.project_string = json.dumps(self.project_json)


class ProjectGetTest(ProjectTest):

    def setUp(self):
        super(ProjectGetTest, self).setUp()
        self.projects_rsp = {'projects': [self.project_json]}

    def test_get(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.projects_rsp)
        project_get = projects.ProjectGet(self.app, mock.Mock())
        args = ['-name', 'dfs']
        verifies = [('name', 'dfs')]
        parsed_args = self.check_parser(project_get, args, verifies)
        project_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '?name=dfs',
            headers=clientmanager.ClientManager.headers)

    def test_get_all(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.projects_rsp)
        project_get = projects.ProjectGet(self.app, mock.Mock())
        args = []
        verifies = []
        parsed_args = self.check_parser(project_get, args, verifies)
        project_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url,
            headers=clientmanager.ClientManager.headers)

    def test_get_one(self):
        self.get_mock.return_value = fakes.FakeResponse(data=self.project_json)
        project_get_one = projects.ProjectGetOne(self.app, mock.Mock())
        args = ['def']
        verifies = [('name', 'def')]
        parsed_args = self.check_parser(project_get_one, args, verifies)
        project_get_one.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '/def',
            headers=clientmanager.ClientManager.headers)


class ProjectCreateTest(ProjectTest):

    def setUp(self):
        super(ProjectCreateTest, self).setUp()

    def test_create_success(self):
        succ_rsp = {
            'href': '{}/{}'.format(self.base_url,
                                   self.project_json.get('name'))
        }
        self.post_mock.return_value = fakes.FakeResponse(data=succ_rsp)
        project_create = projects.ProjectCreate(self.app, mock.Mock())
        args = [self.project_string]
        verifies = [('project', self.project_json)]
        parsed_args = self.check_parser(project_create, args, verifies)
        project_create.take_action(parsed_args)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            self.post_mock.return_value = utils.FAKE_FAILURE
            project_create = projects.ProjectCreate(self.app, mock.Mock())
            args = [self.project_string]
            verifies = [('project', self.project_json)]
            parsed_args = self.check_parser(project_create, args, verifies)
            project_create.take_action(parsed_args)


class ProjectDeleteTest(ProjectTest):

    def setUp(self):
        super(ProjectDeleteTest, self).setUp()

    def test_delete_success(self):
        self.delete_mock.return_value = fakes.FakeResponse()
        project_delete = projects.ProjectDelete(self.app, mock.Mock())
        args = ['def']
        verifies = [('name', 'def')]
        parsed_args = self.check_parser(project_delete, args, verifies)
        project_delete.take_action(parsed_args)
        self.delete_mock.assert_called_once_with(
            self.base_url + '/def',
            data=None,
            headers=clientmanager.ClientManager.headers)

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            self.delete_mock.return_value = utils.FAKE_FAILURE
            project_delete = projects.ProjectDelete(self.app, mock.Mock())
            args = ['def']
            verifies = [('name', 'def')]
            parsed_args = self.check_parser(project_delete, args, verifies)
            project_delete.take_action(parsed_args)


class ProjectPutTest(ProjectTest):

    def setUp(self):
        super(ProjectPutTest, self).setUp()

    def test_put_success(self):
        self.put_mock.return_value = fakes.FakeResponse(data=self.project_json)
        project_put = projects.ProjectPut(self.app, mock.Mock())
        args = ['def', self.project_string]
        verifies = [('name', 'def'), ('project', self.project_json)]
        parsed_args = self.check_parser(project_put, args, verifies)
        project_put.take_action(parsed_args)
        self.put_mock.assert_called_once()

    def test_put_failure(self):
        with testtools.ExpectedException(Exception, 'Update failed: Error'):
            self.put_mock.return_value = utils.FAKE_FAILURE
            project_put = projects.ProjectPut(self.app, mock.Mock())
            args = ['def', self.project_string]
            verifies = [('name', 'def'), ('project', self.project_json)]
            parsed_args = self.check_parser(project_put, args, verifies)
            project_put.take_action(parsed_args)
