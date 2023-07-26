import os
from notification import send_notification
from subprocess import Popen, PIPE

close_commands = ["kill", "close"]
editor_names = ["emacs", "editor"]


def process_command(command):
    command = command.split()
    if len(command) == 2 and command[0] in "open" and command[1] in editor_names:
        send_notification("Opening Emacs...")
        os.system("emacs")
    elif len(command) == 2 and command[0] in "open" and command[1] in "browser":
        send_notification("Opening browser...")
        os.system("xdg-open https://www.google.com/")
    elif len(command) == 2 and command[0] in "open":
        send_notification(f"Opening {command[1]}...")
        os.system(f"{command[1]}")
    elif len(command) == 2 and command[0] in close_commands:
        send_notification(f"Killing all {command[1]} processes...")
        os.system(f"killall {command[1]}")
    else:
        command = "+".join(command)
        print(f"{command}")
        os.system(f"xdg-open https://www.google.com/search?q={command}")

        
def listen(text):
    p = Popen(['xsel', '-bi'], stdin=PIPE)
    p.communicate(input=text.encode())
