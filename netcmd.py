from pythonping import ping
import requests, json
from base import Base

class Net(Base):
    def __init__(self) -> None:
        super().__init__("net")
        netcmds = {
            "ping":"self.ping({0})",
            "http_get":"self.get({0})",
        }
        self.cmds.update(netcmds)
    
    def ping(self, args):
        ip = args[0]
        log = True
        try:
            if args[1] == "false":
                log = False
        except:
            pass
        ping(ip, verbose=log)
        
    def get(self, location):
        print(location[0])
        reply = requests.get(location[0])
        jsonloaded = json.loads(reply.text)
        print(json.dumps(jsonloaded,sort_keys=True,indent=4))
        print(f"HTTP GET request ended {reply}")