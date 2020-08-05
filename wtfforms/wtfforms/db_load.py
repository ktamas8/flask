from wtfforms import db
from wtfforms.models import Instance, Flavor
from sqlalchemy import exc

def instance_load(vms):
    for vm in vms:
        print(vm[0])
        print(vm[1])
        print(vm[2])
        print(vm[3])
        print('----')
        instance = Instance(uuid = vm[0], name = vm[1], state = vm[2], flavor_id = vm[3])

        try:
            db.session.add(instance)
            return db.session.commit()
        except exc.IntegrityError:
            # print('IntegrityError Exception')
            db.session.rollback()

def image_load(images):
    pass

def network_load(networks):
    pass

def subnet_load(networks):
    pass

def keypair_load(keypairs):
    pass
