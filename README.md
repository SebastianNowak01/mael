# Mael
Mael is a Linux-exclusive speech-to-text Python bot to assist you in your daily man-to-computer communication. 

## Requirements
Mael is written in Python so Python interpreter is required to work correctly. To communicate with user Mael uses
notification server so be sure to have one. Don't forget to have a working microphone!
Mael has to be cloned in the ~/ directory to be working correctly.
IMPORTANT! Pynput does not work with Wayland, to use Mael you have to be using X server.

## Dependencies
To translate speech to text Mael uses module named [SpeechRecognition](https://pypi.org/project/SpeechRecognition/).
It is required by this module to have [PyAudio](https://pypi.org/project/PyAudio/) installed too.
To get keyboard input module [pynput](https://pypi.org/project/pynput/) was used.
To install these modules simply run commands given below:

`pip install pyaudio`

`pip install speechrecognition`

`pip install pynput`

## Installation
Follow steps below to install Mael:
1. `git clone https://gitlab.com/sebnow91/mael.git` in your HOME directory to download source code
2. cd into *mael/* and run `python3 setup_mael.py`. It will generate configuration file and service file and active systemd service.
==Root privilages required== (run it with sudo).
3. After service file is generated you have to activate said service. Simply write `systemctl --user enable mael` and then `systemctl --user start mael`
4. Restart your computer and voila! Mael is successfully installed on your computer.

## Usage
To start listening you have to press a keybind to activate Mael (default: \<ctrl\>+l).
A brand new function! Now Mael can listen to what you say and save it to a clipboard! (default: \<ctrl\>+s).

### Configuration
You can change  what keybind will trigger Mael in your configuration file.

### Commands
To check available commands use `cat commands.txt` in *mael/* directory.
