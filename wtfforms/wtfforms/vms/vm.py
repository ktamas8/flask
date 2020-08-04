from config import Config
from pprint import pprint
from shade import *

def vm_discover():
    conn = OpenStackCloud(cloud='train-packstack')
    instances = list(conn.list_servers())
    vms = []
    tmp = []

    for instance in instances:
        tmp.append(instance.id)
        tmp.append(instance.name)
        tmp.append(instance.vm_state)
        tmp.append(instance.flavor.id)

        vms.append(tmp)
        tmp = []

    return(vms)
