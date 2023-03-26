import win32com.client as wincl


if __name__ == '__main__':
    print("Welcome to RoboSpeaker created by Mayank")
    while True:
        x = input("enter what you want me to speak:")
        if x == "q":
            speak = wincl.Dispatch("SAPI.SpVoice")
            speak.Speak("bye bye friend")
            break

        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak(x)
