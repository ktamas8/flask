from openstack import connection
from pprint import pprint
import json
import os

conn = connection.Connection(auth_url=os.environ['OS_AUTH_URL'],
                             project_name=os.environ['OS_PROJECT_NAME'],
                             username=os.environ['OS_USERNAME'],
                             password=os.environ['OS_PASSWORD'],
                             user_domain_id="default",
                             project_domain_id=os.environ['OS_PROJECT_DOMAIN_ID'])

#print("conn: ", conn)

server_list = list(conn.compute.servers())
#servers=json.loads(server_list)

pprint(server_list[0].addresses)

#pprint(server_list)
#print(server_list)
