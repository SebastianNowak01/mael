import os

def create_service():
    home = os.getenv("HOME")

    with open(f"{home}/mael.service", "w") as file:
        file.write("[Unit]\nDescription=Mael, voice activated, virtual assistant\nAfter=graphical-session.target\n\n[Service]\nExecStart=/usr/bin/python3 /home/sebas/mael/main/main.py\nRestart=always\nRestartSec=3\n\n[Install]\nWantedBy=graphical-session.target")
        file.close()
    os.system(f"sudo mv {home}/mael.service /etc/systemd/user")
    os.system("systemctl --user enable mael")
    os.system("systemctl --user start mael")

def create_config():
    home = os.getenv("HOME")

    os.system(f"mkdir {home}/.config/mael")
    os.system(f"touch {home}/.config/mael/config.mael")
    with open(f"{home}/.config/mael/config.mael", "w") as file:
        file.write("# Set your shotcut below. Keys are coded as they would be\n# in a pynput program.\n<ctrl>+l")
        file.close()

if __name__ == '__main__':
    create_service()
    create_config()
