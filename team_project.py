import subprocess as sb
import pywhatkit as py
import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand your voice.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

def run_command(command):
    if command == "1":
        d = sb.getoutput("date")
        print(d)
    elif command == "2":
        docker = sb.getoutput("docker ps -a")
        print(docker)
    elif command == "3":
        print("Enter your song name:")
        song = input()
        py.playonyt(song)
    elif command == "4":
        print("Enter hrs of study:")
    else:
        print("Invalid input")

print("Choose a method to enter your command:")
print("1. Type manually")
print("2. Voice recognition")
choice = input("Enter your choice: ")

if choice == "1":
    print("""
    Press 1: to run date command
    Press 2: to run docker commands
    Press 3: to play song on YouTube
    Press 4: to run a ML code based on Simple Linear Regression
    Enter your hours of study (x)
    """)
    command = input("Enter your choice: ")
    run_command(command)
elif choice == "2":
    command = get_audio()
    if command:
        run_command(command)
else:
    print("Invalid choice")

# Run docker images command to display all images in Docker
docker_images = sb.getoutput("docker images")
print(docker_images)