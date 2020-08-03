
from shade import *
from pprint import pprint

#simple_logging(debug=True)

#conn = openstack_cloud(cloud='train-packstack')
conn = OpenStackCloud(cloud='train-packstack')

#images = conn.list_images()
#for image in images:
#    pprint(image)

#instances = conn.list_servers()
#for instance in instances:
#    pprint(instance)

#pprint(conn.list_servers())

instances = list(conn.list_servers())

for instance in instances:
    print(instance.name)
    print(instance.vm_state)
    print(instance.public_v4)
    print(instance.id)
    print(instance.tenant_id)
    print(instance.user_id)
    print(instance.flavor.id)
    volumes = list(instance.volumes)
    for volume in volumes:
        print(volume.id)
    print('---')


