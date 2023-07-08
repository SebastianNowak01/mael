import os

close_commands = ["kill", "close"]
editor_names = ["emacs", "editor"]


def process_command(command):
    command = command.split()
    if len(command) == 2 and command[0] in "open" and command[1] in editor_names:
        print("Opening editor...")
        os.system("emacs")
    elif len(command) == 2 and command[0] in "open":
        print(f"Opening {command[1]}...")
        os.system(f"{command[1]}")
    elif len(command) == 2 and command[0] in close_commands:
        print(f"Killing all {command[1]} processes...")
        os.system(f"killall {command[1]}")
    else:
        command = "+".join(command)
        print(f"{command}")
        os.system(f"xdg-open https://www.google.com/search?q={command}")


if __name__ == '__main__':
    X = "how to fix plumber"
    process_command(X)
