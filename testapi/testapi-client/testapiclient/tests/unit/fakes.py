import json
import sys

import requests
import six
import httplib


class FakeResponse(requests.Response):

    def __init__(self, headers=None, status_code=httplib.OK,
                 data=None, encoding=None):
        super(FakeResponse, self).__init__()

        headers = headers or {}

        self.status_code = status_code

        self.headers.update(headers)
        if status_code != httplib.OK:
            self.reason = data

        self._content = json.dumps(data)
        if not isinstance(self._content, six.binary_type):
            self._content = self._content.encode()


class FakeApp(object):

    def __init__(self, _stdout, _log):
        self.stdout = _stdout
        self.client_manager = None
        self.stdin = sys.stdin
        self.stdout = _stdout or sys.stdout
        self.stderr = sys.stderr
        self.log = _log


class FakeLog(object):

    def __init__(self):
        self.messages = {}

    def debug(self, msg):
        self.messages['debug'] = msg

    def info(self, msg):
        self.messages['info'] = msg

    def warning(self, msg):
        self.messages['warning'] = msg

    def error(self, msg):
        self.messages['error'] = msg

    def critical(self, msg):
        self.messages['critical'] = msg


class FakeStdout(object):

    def __init__(self):
        self.content = []

    def write(self, text):
        self.content.append(text)

    def make_string(self):
        result = ''
        for line in self.content:
            result = result + line
        return result
