import os

def read_config():
    home = os.getenv('HOME')
    with open(f"{home}/.config/mael/config.mael", "r") as file:
        file.readline()
        file.readline()
        return file.readline().strip()

if __name__ == '__main__':
    print(read_config())
