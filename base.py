class Base:
    cmds = {"exit":"return None"}

    def __init__(self, name) -> None:
        self.name = name
        
    def run(self):
        print("running")
        arguments = []
        command = None
        while True:
            if command == 'exit':
                return "exit"
            command = input("chat>{0}>".format(self.name)).lower()
            parts = command.split()
            command = parts[0]
            arguments = parts[1:]
            try:
                exec(self.cmds[command].format(arguments))
            except Exception as e:
                if not self.cmds.__contains__(command):
                    print(f"Invalid {self.name} Command.")