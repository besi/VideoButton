from gpiozero import LED, Button
from signal import pause
import subprocess

button = Button(21)


subprocess.call(['sudo', 'bin/show_waiting.sh'])


def pressed():
    print("pressed")
    subprocess.call(['omxplayer', 'assets/small.mp4'])

button.when_pressed = pressed

pause()
