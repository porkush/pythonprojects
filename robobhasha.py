import pyttsx3

engine = pyttsx3.init()

print("Welcome to Robobhasha created by Paras")
while True:
    x = input("Enter what you want me to speak: ")
    if x.lower() == "q":
        engine.say("Bye bye friend")
        break
    engine.say(x)
    
