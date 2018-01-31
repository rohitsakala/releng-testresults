##############################################################################
# Copyright (c) 2016 ZTE Corporation
# feng.xiaowei@zte.com.cn
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
##############################################################################
import argparse
import os
import subprocess
import urlparse

import datetime


def get_abspath(path):
    assert os.path.isdir(path), 'Path %s can\'t be found.' % path
    return os.path.abspath(path)


def parse_mongodb_url(url):
    url = urlparse.urlparse(url)
    assert url.scheme == 'mongodb', 'URL must be a MongoDB URL'
    return url


def url_parse(url):
    url = parse_mongodb_url(url)
    return url.username, url.password, url.hostname, url.port


def execute(cmd, args):
    execute_output = subprocess.check_output(cmd)
    print(execute_output)


def do_backup(args):
    db = args.db
    out = get_abspath(args.output_dir)
    now = datetime.datetime.now()
    out = os.path.join(out, '%s__%s' % (db, now.strftime('%Y_%m_%d_%H%M%S')))
    cmd = ['mongodump', '-o', '%s' % out]
    if db:
        cmd.extend(['--db', '%s' % db])

    (username, password, hostname, port) = url_parse(args.url)
    cmd.extend(['--host', '%s' % hostname, '--port', '%s' % port])

    if username:
        cmd.extend(['-u', '%s' % username])
    if password:
        cmd.extend(['-p', '%s' % password])
    print('execute: %s' % cmd)
    execute(cmd, args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Backup MongoDBs')

    parser.add_argument('-u', '--url',
                        type=str,
                        required=False,
                        default='mongodb://127.0.0.1:27017/',
                        help='Mongo DB URL for Backups')
    parser.add_argument('-o', '--output_dir',
                        type=str,
                        required=False,
                        default='./',
                        help='Output directory for the backup.')

    parser.add_argument('-d', '--db',
                        type=str,
                        required=False,
                        default='test_results_collection',
                        help='database for the backup.')

    args = parser.parse_args()
    try:
        do_backup(args)
    except AssertionError as msg:
        print(msg)
