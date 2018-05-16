import json
try:
    with open("./config.json", "r") as config_file:
        config = json.load(config_file)
except (TypeError, ValueError, IOError):
    config = {}

MESSAGE_SOURCE = config.get("source", "LUNA")
MESSAGE_CAPTION = config.get("caption", "Person detected: {}")
MESSAGE_TEMPLATE = config.get("message", "")
CAMERA_ID = "e3e9a385-7fe0-3ba5-5482-a86cde7faf48" # use Nx Witness camera id (open web interface to view it)
MESSAGE_METADATA = config.get("meta_data", '{"cameraRefs":["%s"]}'%CAMERA_ID)  
NOTIFICATION_URL = config.get("url", "http://admin:admin123@127.0.0.1:7001/api/createEvent") # use Nx Witness server credentials IP 
SUBSCRIPTION_URL = config.get("websocket", "ws://192.168.56.101:9000/events/api/subscribe") # use Luna websocket address

LUNA_TOKEN = config.get("token", "eb0bf8f7-e3ef-4e2c-a3ee-43913fec8e28")
LUNA_LIST = config.get("list", "ce29c6c3-93fd-4c68-9e22-13d136906577")
SUBSCRIPTION_TOKENS = [LUNA_TOKEN,]
TIME_CORRECTION = 3*60*60*1000 - 4*1000  # Time correction for demo: Your timezone minus 4 seconds (aproximate delay between face decection and face recognition)

LUNA_SCORE_THRESHOLD = config.get("threshold", 0)