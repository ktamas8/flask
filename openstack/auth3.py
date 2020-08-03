#nova = novaclient.Client(version='2',username='admin',password='123123',project_id='fe21e057bfbb4c42b5b7dd91eef1997a',auth_url='http://10.36.50.192:5000/v3/',insecure='True')
#nova = novaclient.Client('2','admin','123123','fe21e057bfbb4c42b5b7dd91eef1997a','http://10.36.50.192:5000/v3/')

# http://docs.openstack.org/developer/keystoneauth/index.html
# http://www.jamielennox.net/blog/2014/09/15/how-to-use-keystoneclient-sessions/

# In iPython: execfile('path/to/this/file')

import os
import logging
from pprint import pprint
import requests

from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client

import novaclient.client

# suppress warning
requests.packages.urllib3.disable_warnings()

# logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.INFO)

LOG = logging.getLogger(__name__)

if os.environ.get('http_proxy') or os.environ.get('https_proxy'):
    LOG.WARN("Proxy env vars set")

# TODO howto pass internalURL
auth = v3.Password(auth_url=os.environ['OS_AUTH_URL'],
                   username=os.environ['OS_USERNAME'],
                   password=os.environ['OS_PASSWORD'],
                   project_name=os.environ['OS_PROJECT_NAME'],
                   user_domain_name=os.environ['OS_USER_DOMAIN_NAME'],
                   project_domain_name=os.environ['OS_PROJECT_DOMAIN_NAME'])

# sess = session.Session(auth=auth, verify='/path/to/ca.cert')
sess = session.Session(auth=auth, verify=False)

novac = novaclient.client.Client(2, session=sess)
print(novac.servers.list())
print(novac.flavors.find(ram=512))

keystonecl = client.Client(session=sess)
pprint(keystonecl.users.list())

#import neutronclient.neutron.client
#neutc = neutronclient.neutron.client.Client('2.0', session=sess)
#neutc.list_networks()

