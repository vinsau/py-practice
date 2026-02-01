import json

data_string = """
{
  "app": "web-server",
  "version": 1.0,
  "ports": [80, 443],
  "service_enabled": true
}
"""

data_dict = json.loads(data_string)
data_dict['version'] = 1.1
data_dict['owner'] = 'devops-team'

new_data_string = json.dumps(data_dict, indent=4)
print(new_data_string)