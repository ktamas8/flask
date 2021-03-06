#!/usr/bin/env python

from keystoneclient.auth.identity import v3
from keystoneclient import session
from novaclient import client as nova_client

import getpass
import os
import sys
import time

example_credentials = ("auth_url=''\n"
                       "name=''\n"
                       "project_id=''\n"
                       "user_domain_id=''\n"
                       "ssl_bundle=''\n"
                      )

# import user details from credentials.py - if none exist, raise exit & print help

try:
    if os.path.isfile('./credentials.py'):
        from credentials import auth_url, username, project_id, user_domain_id, ssl_bundle
    else:
        print "credentials.py file missing, please create one. ie:\n{cred}".format(cred=example_credentials)
        raise SystemExit
except ImportError:
    print "Unable to read all variables, ensure file is correct, i.e.:"
    print example_credentials
    raise SystemExit

# get password variable

password = getpass.getpass()

# session

auth = v3.Password(auth_url=auth_url, username=username, password=password, project_id=project_id, user_domain_id=user_domain_id)
sess = session.Session(auth=auth, verify=ssl_bundle)

# nova connection

nova = nova_client.Client(2, session=sess)

# list function:

def prompt_user(lst):
    lst_len = len(lst)
    while  True:
        for i in range(lst_len):
            print i, lst[i]
        print "-1 to exit..."
        try:
            choice = int(input('Your choice? '))
        except:
            print "Invalid choice."
            continue
        if choice not in range(-1, lst_len):
            print "Need an integer between -1 and %s" %(lst_len-1)
        else:
            return choice

# gather vm details

# function to get the VM name

def get_name():
    selection_ok = ''
    while selection_ok not in [ 'y', 'yes']:
        get_name.name = raw_input('What should we call this VM? ')
        print "Server name is {name}".format(name=get_name.name)
        selection_ok = raw_input('Is that OK? Answer y/Y to continue. ').lower()

# function to check the SSH key to use

def get_key():
    keypair_list = nova.keypairs.list()
    if len(keypair_list) is 0:
        print "You do not have any keypairs associated with this account, proceeding..."
    elif len(keypair_list) is 1:
        print "You only have one keypair, proceeding..."
        get_key.name = keypair_list[0].name
    else:
        print "Here are your available SSH keys:"
        index = int(prompt_user(keypair_list))
        get_key.name = keypair_list[index].name

# function to select the VM image

def get_image():
    print "Here are your available images:"
    image_list = nova.images.list()
    index = int(prompt_user(image_list))
    get_image.id = image_list[index].id
    get_image.name = image_list[index].name

# function to select the flavor

def get_flavor():
    print "Here are your available flavors:"
    flavor_list = nova.flavors.list()
    index = int(prompt_user(flavor_list))
    get_flavor.id = flavor_list[index].id

# function to find a list of free ips

def get_floating_ip():
    nova_ips = nova.floating_ips.list()
    free_ips = [ip for ip in nova_ips if ip.instance_id is None]
    if len(free_ips) == 0:
        get_floating_ip.ob = nova.floating_ips.create()
        print "No IP address found, one has been acquired."
    elif len(free_ips) == 1:
        print "One IP address available, this will be used."
        get_floating_ip.ob = free_ips[0]
    else:
        print "More than one IP available, choosing first available."
        get_floating_ip.ob = free_ips[0]

# call all our build functions

get_name()
get_key()
get_image()
get_flavor()

# if they do not have an SSH key let's just carry on without it...

try:
    if 'name' in get_key.__dict__:
        create_server = nova.servers.create(name=get_name.name, image=get_image.id, flavor=get_flavor.id, key_name=get_key.name)
    else:
        create_server = nova.servers.create(name=get_name.name, image=get_image.id, flavor=get_flavor.id)
except nova_client.exceptions.Forbidden:
    print "Nova denied your request, please check you have sufficient quota and your details are correct..."

server_id = create_server.id
server_info = nova.servers.get(server_id)
server_status = server_info.status

print "Waiting for build to complete."

while server_status == 'BUILD':
    time.sleep(2)
    server_info = nova.servers.get(server_id)
    server_status = server_info.status

if server_status == 'ACTIVE':
    print "The server has finished building."
else:
    print "Something went wrong, server status is not ACTIVE!"
    raise SystemExit

# ask user if they would like a floating IP address

associate_floating_ip = raw_input('Would you like to associate a floating IP with this host? Answer y/Y to continue. ').lower()

# if they answer yes let's call our floating ip function

if associate_floating_ip in [ 'y', 'yes' ]:
    get_floating_ip()
    server_info.add_floating_ip(get_floating_ip.ob)
    build_ip = get_floating_ip.ob.ip
else:
    build_ip = "None."

# print summary table

build_name = get_name.name
build_image = get_image.name

print "Summary:"
print "----------------------------"
print '{:<15} {:<15}'.format("Name:", build_name)
print '{:<15} {:<15}'.format("IP:", build_ip)
print '{:<15} {:<15}'.format("Image:", build_image)
