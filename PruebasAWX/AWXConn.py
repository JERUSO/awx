import sys
import requests
import json
templateid=sys.argv[1]
from requests.auth import HTTPBasicAuth
headers = {'content-type': 'application/json'}
data_new = {'limit': 'server-PRC-05'}
res = requests.post('http://awx_host/api/v2/job_templates/'+templateid+'/launch/',
verify=False, auth=HTTPBasicAuth('user', 'password'), data=json.dumps(data_new), headers=headers)
print (res.content)
