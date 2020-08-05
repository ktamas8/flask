#!/usr/bin/env python

import sys
import time
import argparse
from os import environ as env
from novaclient.client import Client

def main():
    credentials = get_nova_credentials_v2()
    nova_client = Client(**credentials)

def instance_stop():
    uuid = 'c155a798-372a-492c-93a8-6c7a9975c126'
    # novaclient.v2.servers.stop()

def get_nova_credentials_v2():
    """Returns an list of credentials."""

    d = dict()
    d['version'] = '2'
    d['username'] = env['OS_USERNAME']
    d['password'] = env['OS_PASSWORD']
    d['auth_url'] = env['OS_AUTH_URL']
    d['project_id'] = env['OS_TENANT_NAME']
    return d

if __name__ == '__main__':
    sys.exit(main())
