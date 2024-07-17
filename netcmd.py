from pythonping import ping
import requests, json
from base import Base

class Net(Base):
    def __init__(self) -> None:
        super().__init__("net")
        netcmds = {
            "ping":"self.ping({0})",
            "get":"self.get({0})",
        }
        nethelp = {
            "ping":"Ping a server 4 times.",
            "get" :"HTTP GET any API Endpoint."
        }
        netusage= {
            "ping":"ping [IP/URL] [TRUE/FALSE - LOG]",
            "get" :"get [ENDPOINT] [TRUE/FALSE - DUMP REPLY]"
        }
        
        self.cmds.update(netcmds)
        self.helps.update(nethelp)
        self.usage.update(netusage)

    
    def ping(self, args):
        ip = args[0]
        log = True
        try:
            if args[1] == "false":
                log = False
        except:
            pass
        ping(ip, verbose=log)
        
    def get(self, args):
        print(args[0])
        reply = requests.get(args[0])
        jsonloaded = json.loads(reply.text)
        print(json.dumps(jsonloaded,sort_keys=True,indent=4))
        print(f"HTTP GET request ended {reply}")
        
        if args[1] == 'true':
            with open('data.json', 'w+') as f:
                json.dump(jsonloaded,f,indent=4)
                print("Saved to file.")