import random


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

def rizz():
    rizzes = [
        "I'd like to take you to the movies but they don't let you bring your own snacks in.",
        "No pen, no paper but you still draw my attention.",
        "All the good pick up lines are taken but you aren't.",
        "Excuse me while I delete my dating apps.",
        "This must be a museum because you're a work of art.",
        "Are you WiFi? Because I feel a connection.",
        "I'm not even playing cards but somehow I pulled a Queen.",
        "You must be a dog person because you look fetching.",
        "I didn't even have to run to catch these butterflies.",
        "I'm lost. Can you give me directions to your heart?",
        "Well, here I am. What are your other two wishes?",
        "Hey, how was heaven when you left it?",
        "Are you Siri? Because you autocomplete me.",
        "Are you a charger? Because I'm dying without you.",
        "Wanna be Minecraft without the craft?",
        "Are you lighnting? Because you're McQueen.",
        "Is there an airport nearby or is that my heart taking off?",
        "Do you have a pet? Because seeing you has given me a whole new leash on life.",
        "Is your name Jimmy? Because I've Fallon for you.",
        "I don't normally chase people but for you I'd put my crocs in sport mode.",
        "Are you a Mariah Carey song? Because All I Want for Christmas Is You.",
        "Aren't you worried about global warming? Because you're making it hot in here.",
        "If you were a triangle you'd be acute one.",
        "Are you a loan? You've got my interest.",
        "Are you a magician? Because when I look at you, everyone else disappears.",
        "Did you invent the airplane? Because you're clearly Mr. Wright.",
        "Is your dad a boxer? Because you're a knockout!",
        "How can I plan our wedding without having your number?",
        "Are you a keyboard? Because you might just be my type.",
        "You know, I'm actually terrible at flirting. How about you try to pick me up instead?",
        "4+4=8 but you+me=fate",
        "Are you tired? You've been running through my mind all day.",
        "What's your favorite drink? I'm asking so I know what to buy you when we go on our first date.",
        "I should complain to Spotify for not making you this week's hottest single.",
        "Do you play soccer? Because you're a keeper.",
        "You look so familiar…did we have class together? I could've sworn we had chemistry.",
        "I'm learning about important dates in history, wanna be one of them?",
        "They say dating is a numbers game, so can I get yours?",
        "When I text you good morning tomorrow, what number should I text?",
        "Hi, my name is [your name], but you can call me tomorrow.",
        "Can I show your profile to my friends to prove that angels really do exist?",
        "There's something wrong with my phone, it doesn't have your number in it.",
        "123456789. The only number I don't see here is yours.",
        "Do you have Instagram? My parents always told me to follow my dreams.",
        "Are you an artist? You're really good at drawing me in.",
        "Angels should be in heaven. How'd you escape?",
        "If you and I were socks, we'd make a great pair.",
        "Well, here I am! What are your other two wishes?",
        "Your name must be Barbie because when I saw you I pictured our Dreamhouse.",
        "What is it like to be the most gorgeous person in this room?",
        "If you were words on a page, you'd be fine print.",
        "You must be a talented thief because you managed to steal my heart from all the way over here.",
        "They say nothing lasts forever. Want to be my nothing?",
        "Anyone who says Disney is the happiest place on earth has never stood next to you.",
        "Are you a time traveler? Because I can see you in my future.",
        "I'm not a photographer but I can picture you and me together.",
        "Are you French? Because Eiffel for you.",
        "Guess what I'm wearing? The smile you gave me.",
        "Are your parents bakers? Because you're a cutie pie.",
        "I had a good pickup line ready to go, but you're so good-looking I'm literally speechless.",
        "I think there's something wrong with my phone. Could you call it and see if it works?",
        "Did the sun come out, or did you just smile at me?",
        "Would you mind giving me a pinch? You're so cute, I must be dreaming.",
        "If I had a time machine, I'd use it to relive this exact moment.",
    ] #list of corny pickup lines
    #list of 60ish pickup lines
    print(random.choice(rizzes))

def mathing():
    import mathcmd
    print("Begin mathing.")
    mathing = True
    arguments = []
    command = None
    mathcmds = {
        "add":"mathcmd.add({0})",
        "exit":"return Nonef"
    }
    while True:
        if command == "exit":
            mathing = False
            break
        command = input("chat.math>").lower()
        parts = command.split()
        command = parts[0]
        arguments = parts[1:]

        try:
            exec(mathcmds[command].format(arguments))
        except Exception as e:
            if not mathcmds.__contains__(command):
                print("Invalid Math Command.")

cmd = {"hello": "hello()",
        "rizz_me": "rizz()",
        "math":"mathing()",
        "exit":"exit()"}
command = None

while True:
    if command == "exit":
        exit()

    command = input("chat>").lower()

    try:
        exec(cmd[command])
    except:
        if not cmd.__contains__(command):
            print("Invalid Command.")
