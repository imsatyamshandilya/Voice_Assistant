import speech_recognition as aa
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = aa.Recognizer()
machine = pyttsx3.init()


def talk(text):
    machine.say(text)
    machine.runAndWait()


def input_instruction():
    try:
        with aa.Microphone() as origin:
            print("listening........")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', '')
                # print(instruction)
                return instruction
    except aa.UnknownValueError:
        pass
    except aa.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
    return ""


flag = True


def play_jarvis():
    instruction = input_instruction()
    print(instruction)

    if instruction != "":
        if "play" in instruction:
            song = instruction.replace('play', "")
            talk("playing" + song)
            pywhatkit.playonyt(song)
        elif 'time' in instruction:
            time = datetime.datetime.now().strftime('%I:%M%p')
            talk('Current time' + time)
        elif 'date' in instruction:
            date = datetime.datetime.now().strftime('%d /%m /%Y')
            talk("Today's date" + date)
        elif 'how are you' in instruction:
            talk('I am fine, how about you')
        elif 'what is your name' in instruction:
            talk('I am Jarvis, What can I do for you')
        elif 'who is' in instruction:
            human = instruction.replace("who is", "")
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
        elif "stop" in instruction:
            global flag
            flag = False
            talk("Thank You")
        else:
            talk('Please repeat')
    else:
        talk("Please repeat again")


while flag == True:
    play_jarvis()
