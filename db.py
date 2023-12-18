import json

def load_config():
    try:
     with open('config.txt', 'r') as config:
      config_udate = json.loads(config.read())
      return config_udate
    except Exception as e:
        print("error: "+ str(e))
db = load_config()

print(db)