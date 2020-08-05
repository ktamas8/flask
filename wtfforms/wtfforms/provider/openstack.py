from config import Config
from os import environ as env
from pprint import pprint
from keystoneauth1 import loading
from keystoneauth1 import session
from novaclient import client as novaclient
from shade import *

def get_nova_credentials_v2():
    """Returns an list of credentials."""

    d = dict()
    d['version'] = '2'
    d['username'] = env['OS_USERNAME']
    d['password'] = env['OS_PASSWORD']
    d['auth_url'] = env['OS_AUTH_URL']
    d['project_id'] = env['OS_TENANT_NAME']
    return d

def nova_connect():
    loader = loading.get_plugin_loader('password')
    auth = loader.load_from_options(auth_url='http://10.36.50.192:5000/v3',
                       username='admin',
                       password='123123',
                       project_name='admin',
                       project_domain_name='Default',
                       user_domain_name='Default')
    # auth = loader.load_from_options(auth_url=env['OS_AUTH_URL'],
    #                    username=env['OS_USERNAME'],
    #                    password=env['OS_PASSWORD'],
    #                    project_name=env['OS_PROJECT_NAME'],
    #                    project_domain_name=env['OS_PROJECT_DOMAIN_NAME'],
    #                    user_domain_name=env['OS_PROJECT_DOMAIN_NAME'])
    sess = session.Session(auth=auth)
    return sess

def openstack_connect():
    conn = OpenStackCloud(cloud='train-packstack')
    return conn

def instance_start(vm_uuid):
    sess = nova_connect()
    nova = novaclient.Client(2, session=sess)
    result = nova.servers.start(vm_uuid)
    print(result)

def instance_stop(vm_uuid):
    sess = nova_connect()
    nova = novaclient.Client(2, session=sess)
    result = nova.servers.stop(vm_uuid)
    print(result)

def instance_discover():

    conn = openstack_connect()
    instances = list(conn.list_servers())
    vms = []
    tmp = []

    for instance in instances:
        tmp.append(instance.id)
        tmp.append(instance.name)
        tmp.append(instance.vm_state)
        tmp.append(instance.flavor.id)

        vms.append(tmp)
        #tmp.clear()
        tmp = []

    return(vms)

def image_discover():
    pass

def network_discover():
    pass

def subnet_discover():
    pass

def keypair_discover():
    pass
