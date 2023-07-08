import speech_recognition as sr
from multiprocessing import Process
from commands import process_command

# Initialize the recognizer
if __name__ == '__main__':
    r = sr.Recognizer()
    while 1:

        # Exception handling to handle
        # exceptions at the runtime
        try:

            # use the microphone as source for input.
            with sr.Microphone() as source:

                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source, duration=0.2)

                # listens for the user's input
                print("What do you want to say?")
                audio = r.listen(source)

                # Using google to recognize audio
                command = r.recognize_google(audio)
                command = command.lower()

                p = Process(target=process_command, args=(command,))
                p.start()
                # print(f"Did you say {MyText}")

        except sr.RequestError as e:
            print(f"Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
