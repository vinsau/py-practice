import yaml

config_yaml_string = """
apiVersion: v1
kind: Pod
metadata:
  name: my-app
spec:
  containers:
  - name: main-app
    image: my-app:latest
    ports:
    - containerPort: 8080
  - name: sidecar-proxy
    image: proxy:1.0
    ports:
    - containerPort: 9000
"""

config_dict = yaml.safe_load(config_yaml_string)
print(config_dict['spec']['containers'][1]['name'])