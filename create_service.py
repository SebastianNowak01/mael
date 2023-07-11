import os

def create_config():
    home = os.getenv("HOME")
    # with open(f"{home}/test.service", "x") as file:
    #     file.close()

    with open(f"{home}/test.service", "w") as file:
        file.write(f"[Unit]\nDescription=My test serviceAfter=multi-user.target\n\n[Service]\nType=simpleRestart=always\nExecStart=/usr/bin/python3 {home}/Projects/mael/test.py\n\n[Install]\nWantedBy=multi-user.target")
        file.close()
    # os.system(f"mv {home}/")
        
if __name__ == '__main__':
    create_config()
