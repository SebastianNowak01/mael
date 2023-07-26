import speech_recognition as sr
from multiprocessing import Process
from command import process_command
from notification import send_notification
from pynput import keyboard
from config import read_config

def main(hotkey):
    # Initialize the recognizer
    recognizer = sr.Recognizer()
    print(f"{hotkey}")
    # Exception handling to handle
    # exceptions at the runtime
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            recognizer.adjust_for_ambient_noise(source, duration=0.2)

            # listens for the user's input
            send_notification("Enter command/query")
            audio = recognizer.listen(source)

            # Using google to recognize audio
            command = recognizer.recognize_google(audio)
            command = command.lower()

            p = Process(target=process_command, args=(command,))
            p.start()

    except sr.RequestError as e:
        send_notification(f"Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        send_notification("unknown error occurred")

if __name__ == '__main__':
    # Listening begins only after pressing a hotkey
    process_hotkey, listen_hotkey = read_config()
    
    with keyboard.GlobalHotKeys({
             process_hotkey: lambda: main(process_hotkey)}) as h:
        h.join()
