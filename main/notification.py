import subprocess


def send_notification(message):
    subprocess.Popen(['notify-send', message])


if __name__ == '__main__':
    lorem = "lorem"
    send_notification(f"ipsum {lorem}")
