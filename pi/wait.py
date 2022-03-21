from gpiozero import LED, Button
from signal import pause
import subprocess

button = Button(21)


subprocess.call(['sudo', 'bin/show_waiting.sh'])


def pressed():
    print("pressed")
    subprocess.call(['sudo', 'bin/show_loading.sh'])
    subprocess.call(['omxplayer', 'assets/SM_DE.mp4'])
    subprocess.call(['sudo', 'bin/show_waiting.sh'])

button.when_pressed = pressed

pause()
