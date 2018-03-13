import StringIO
import httplib
import json

from mock import mock
import requests
from six.moves.urllib import parse
import testtools

from testapiclient.cli import projects
from testapiclient.tests.unit import utils
from testapiclient.utils import http_client
from testapiclient.utils import user


class ProjectTest(utils.TestCommand):
    def setUp(self):
        super(ProjectTest, self).setUp()
        user.User.session = requests.session()
        self.base_url = parse.urljoin(self.api_url, 'projects')
        self.project_json = {
            'name': 'test_project',
            'description': ''
        }
        self.project_string = json.dumps(self.project_json)


class ProjectGetTest(ProjectTest):

    def setUp(self):
        super(ProjectGetTest, self).setUp()
        self.get_mock = mock.patch('requests.get').start()
        self.get_mock.return_value.status_code = httplib.OK

    def test_get(self):
        project_get = projects.ProjectGet(mock.Mock(), mock.Mock())
        args = ['-name', 'dfs']
        verifies = [('name', 'dfs')]
        parsed_args = self.check_parser(project_get, args, verifies)
        project_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '?name=dfs')

    def test_get_all(self):
        project_get = projects.ProjectGet(mock.Mock(), mock.Mock())
        args = []
        verifies = []
        parsed_args = self.check_parser(project_get, args, verifies)
        project_get.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url)

    def test_get_one(self):
        project_get_one = projects.ProjectGetOne(mock.Mock(), mock.Mock())
        args = ['def']
        verifies = [('name', 'def')]
        parsed_args = self.check_parser(project_get_one, args, verifies)
        project_get_one.take_action(parsed_args)
        self.get_mock.assert_called_once_with(
            self.base_url + '/def')


class ProjectCreateTest(ProjectTest):

    def setUp(self):
        super(ProjectCreateTest, self).setUp()
        self.post_mock = mock.patch(
            'testapiclient.utils.user.User.session.post').start()
        self.post_mock.return_value.status_code = httplib.OK

    def test_create_success(self):
        project_create = projects.ProjectCreate(mock.Mock(), mock.Mock())
        args = [self.project_string]
        verifies = [('project', self.project_json)]
        parsed_args = self.check_parser(project_create, args, verifies)
        project_create.take_action(parsed_args)
        self.post_mock.assert_called_once()

    def test_create_failure(self):
        with testtools.ExpectedException(Exception, 'Create failed: Error'):
            project_create = projects.ProjectCreate(mock.Mock(), mock.Mock())
            self.post_mock.return_value.status_code = httplib.BAD_REQUEST
            self.post_mock.return_value.reason = "Error"
            args = [self.project_string]
            verifies = [('project', self.project_json)]
            parsed_args = self.check_parser(project_create, args, verifies)
            project_create.take_action(parsed_args)

    def test_create_unauthorized(self):
        self.mock_unautherized()
        with mock.patch('sys.stdout', new=StringIO.StringIO()) as mock_stdout:
            with mock.patch('requests.Session') as mock_sessions:
                mock_sessions().post.return_value.text = "login"
                project_create = projects.ProjectCreate(
                    mock.Mock(), mock.Mock())
                args = ['-u', 'user', '-p', 'password', self.project_string]
                verifies = [
                    ('u', 'user'),
                    ('p', 'password'),
                    ('project', self.project_json)]
                parsed_args = self.check_parser(project_create, args, verifies)
                project_create.take_action(parsed_args)
                self.assertEqual(mock_stdout.getvalue(),
                                 "Authentication has failed.\n")

    def test_create_authorized(self):
        project_create = projects.ProjectCreate(mock.Mock(), mock.Mock())
        args = ['-u', 'user', '-p', 'password', self.project_string]
        verifies = [
            ('u', 'user'),
            ('p', 'password'),
            ('project', self.project_json)
        ]
        parsed_args = self.check_parser(project_create, args, verifies)
        project_create.take_action(parsed_args)
        self.post_mock.assert_called_once()


class ProjectDeleteTest(ProjectTest):

    def setUp(self):
        super(ProjectDeleteTest, self).setUp()
        self.delete_mock = mock.patch(
            'testapiclient.utils.user.User.session.delete').start()
        self.delete_mock.return_value.status_code = httplib.OK

    def test_delete_success(self):
        project_delete = projects.ProjectDelete(mock.Mock(), mock.Mock())
        args = ['def']
        verifies = [('name', 'def')]
        parsed_args = self.check_parser(project_delete, args, verifies)
        project_delete.take_action(parsed_args)
        self.delete_mock.assert_called_once_with(
            self.base_url + '/def',
            data='null',
            headers=http_client.HTTPClient.headers)

    def test_delete_failure(self):
        with testtools.ExpectedException(Exception, 'Delete failed: Error'):
            project_delete = projects.ProjectDelete(mock.Mock(), mock.Mock())
            self.delete_mock.return_value.status_code = httplib.FORBIDDEN
            self.delete_mock.return_value.reason = "Error"
            args = ['def']
            verifies = [('name', 'def')]
            parsed_args = self.check_parser(project_delete, args, verifies)
            project_delete.take_action(parsed_args)

    def test_delete_authorized(self):
        project_delete = projects.ProjectDelete(mock.Mock(), mock.Mock())
        args = ['-u', 'user', '-p', 'password', 'def']
        verifies = [('u', 'user'), ('p', 'password'), ('name', 'def')]

        parsed_args = self.check_parser(project_delete, args, verifies)
        project_delete.take_action(parsed_args)
        self.delete_mock.assert_called_once_with(
            self.base_url + '/def',
            data='null',
            headers=http_client.HTTPClient.headers)

    def test_delete_unauthorized(self):
        self.mock_unautherized()
        with mock.patch('sys.stdout', new=StringIO.StringIO()) as mock_stdout:
            with mock.patch('requests.Session') as mock_sessions:
                mock_sessions().post.return_value.text = "login"
                project_delete = projects.ProjectDelete(
                    mock.Mock(), mock.Mock())
                args = ['-u', 'user', '-p', 'password', 'def']
                verifies = [('u', 'user'), ('p', 'password'), ('name', 'def')]
                parsed_args = self.check_parser(project_delete, args, verifies)
                project_delete.take_action(parsed_args)
                self.assertEqual(mock_stdout.getvalue(),
                                 "Authentication has failed.\n")


class ProjectPutTest(ProjectTest):

    def setUp(self):
        super(ProjectPutTest, self).setUp()
        self.put_mock = mock.patch(
            'testapiclient.utils.user.User.session.put').start()
        self.put_mock.return_value.status_code = httplib.OK

    def test_put_success(self):
        project_put = projects.ProjectPut(mock.Mock(), mock.Mock())
        args = ['def', self.project_string]
        verifies = [('name', 'def'), ('project', self.project_json)]
        parsed_args = self.check_parser(project_put, args, verifies)
        project_put.take_action(parsed_args)
        self.put_mock.assert_called_once()

    def test_put_failure(self):
        with testtools.ExpectedException(Exception, 'Update failed: Error'):
            project_put = projects.ProjectPut(mock.Mock(), mock.Mock())
            self.put_mock.return_value.status_code = httplib.BAD_REQUEST
            self.put_mock.return_value.reason = "Error"
            args = ['def', self.project_string]
            verifies = [('name', 'def'), ('project', self.project_json)]
            parsed_args = self.check_parser(project_put, args, verifies)
            project_put.take_action(parsed_args)

    def test_put_unauthorized(self):
        self.mock_unautherized()
        with mock.patch('sys.stdout', new=StringIO.StringIO()) as mock_stdout:
            with mock.patch('requests.Session') as mock_sessions:
                mock_sessions().post.return_value.text = "login"
                project_put = projects.ProjectPut(mock.Mock(), mock.Mock())
                args = ['-u', 'user', '-p', 'password', 'def',
                        self.project_string]
                verifies = [
                    ('u', 'user'),
                    ('p', 'password'),
                    ('name', 'def'),
                    ('project', self.project_json)]
                parsed_args = self.check_parser(project_put, args, verifies)
                project_put.take_action(parsed_args)
                self.assertEqual(mock_stdout.getvalue(),
                                 "Authentication has failed.\n")

    def test_create_authorized(self):
        project_put = projects.ProjectPut(mock.Mock(), mock.Mock())
        args = ['-u', 'user', '-p', 'password', 'def', self.project_string]
        verifies = [
            ('u', 'user'),
            ('p', 'password'),
            ('name', 'def'),
            ('project', self.project_json)
        ]
        parsed_args = self.check_parser(project_put, args, verifies)
        project_put.take_action(parsed_args)
        self.put_mock.assert_called_once()
