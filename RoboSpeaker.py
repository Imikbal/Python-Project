import pyttsx3

if __name__ == "__main__":
    print("WELCOME TO ROBOSPEAKER")
    while True:
        x = input("ENTER WHAT YOU WANT ME TO SPEAK: ")
        if(x==0):
            break
        else:
            engine = pyttsx3.init()
            engine.say(x)
            engine.runAndWait()
