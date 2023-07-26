import os

def read_config():
    home = os.getenv('HOME')
    with open(f"{home}/.config/mael/config.mael", "r") as file:
        hotkeys = []
        file.readline()
        file.readline()
        hotkeys.append(file.readline().strip())
        hotkeys.append(file.readline().strip())
        file.close()
        return hotkeys

if __name__ == '__main__':
    print(read_config())
