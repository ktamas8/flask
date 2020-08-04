from wtfforms import db
from wtfforms.models import Instance, Flavor

def instance_load(vms):
    for vm in vms:
        print(vm[0])
        print(vm[1])
        print(vm[2])
        print(vm[3])
        print('----')
        instance = Instance(uuid = vm[0], name = vm[1], state = vm[2], flavor_id = vm[3])
        db.session.add(instance)
        db.session.commit()

def image_load(images):
    pass

def network_load(networks):
    pass

def subnet_load(networks):
    pass

def keypair_load(keypairs):
    pass
