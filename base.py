class Base:
    cmds = {"exit":"return None",
            "help":"self.help({0})"}
    
    helps = {"exit":"Exit the module",
            "help":"Get help (like this)."}
    
    usage ={"exit":"exit",
            "help":"help [*command]"}
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
                    
    def help(self, args):
        print("Helping you!")
        command = None
        if len(args) > 0:
            command = args[0]
            print(command)
        if command:
            if command in self.cmds:
                print(f"{command} - {self.helps[command]} \nSymtax:{self.usage[command]} \n(* indicates optional argument.)")
            else:
                print("Invalid command, cannot help!")
                
        else:
            for x in self.cmds.keys():
                print(f"{x} - {self.helps[x]}")