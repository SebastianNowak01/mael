import os

def create_service():
    home = os.getenv("HOME")

    with open(f"{home}/mael.service", "w") as file:
        file.write(f"[Unit]\nDescription=Mael, voice activated, virtual assistant\nAfter=default.target\n\n[Service]\nExecStart=/usr/bin/python3 {home}/mael/main/main.py\n\n[Install]\nWantedBy=default.target")
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
