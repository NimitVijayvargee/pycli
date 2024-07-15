import random
from mathcmd import Math
from netcmd import Net

#modules:
maths = Math()
net = Net()


def hello():
    print(
        random.choice(
            [
                "Hello!",
                "Hey",
                "Hi!",
                "sup?",
                "wassup?",
                "Hello World!",
                "ok, and?",
                'bro really said "hello"',
            ]
        )
    )

cmd = {"hello": "hello()",
        "math":"maths.run()",
        "net":"net.run()",
        "exit":"exit()"}


while True:
    command = input("chat>").lower()
    if command == "exit":
        exit()

    try:
        exec(cmd[command])
    except:
        if not cmd.__contains__(command):
            print("Invalid Command.")
