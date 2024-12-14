import json

data = [{"name": "xiaohong", "age": 10}, {"name": "xiaobai", "age": 99}, {"name": "xiaowang", "age": 23}]
json_str = json.dumps(data)
print(type(json_str))
print(json_str)
