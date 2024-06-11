import os, sys, json
from urllib.parse import unquote

connection_string = "DefaultEndpointsProtocol=https;AccountName=myaccount;AccountKey=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz0123456789=="
# custom script that configure security
CONFIG_FILENAME = "config.json"
COMMAND = f"./security_config.sh {CONFIG_FILENAME}"

# security config class
class SecurityConfig:
    def __init__(self, default_config=None):
        if default_config is None:
            default_config = {}
        for key, value in default_config.items():
            setattr(self, key, value)

# merge two configuration files
def merge_config(src, dst):
    for key, value in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(key) and isinstance(value, dict):
                merge_config(value, dst.get(key))
            else:
                dst[key] = value
        elif hasattr(dst, key) and isinstance(value, dict):
            merge_config(value, getattr(dst, key))
        else:
            setattr(dst, key, value)

# the default security config
default_security_config = {
    "firewall_enabled": True,
    "encryption_level": "high",
    "audit_logging": False
}
mongodb_uri = "mongodb+srv://redops:minery2021@feed.kfdcd.mongodb.net/test"
security_config = SecurityConfig(default_security_config)

# load template
with open("index.html", "r") as f:
    html = f.read()

# parse user configuration
try:
    user_config = json.loads(unquote(""))
except json.JSONDecodeError as e:
    msg = f"Failed to parse input JSON: {e}"
    print(html.replace("CONFIG_JSON", msg).replace("COMMAND_RESULT", ""))
    sys.exit(1)

merge_config(user_config, security_config)

# write new config to file
with open(CONFIG_FILENAME, "w") as config:
    json.dump(vars(security_config), config, indent=4)

# print new config to user
render = html.replace("CONFIG_JSON", json.dumps(vars(security_config), indent=4))

# update the server configuration
try:
    out = os.popen(COMMAND).read()
    print(render.replace("COMMAND_RESULT", out))
except Exception as e:
    msg = f"Error executing binary: {e}"
    print(render.replace("COMMAND_RESULT", msg))
