from gpiozero import LED, Button
from signal import pause
import subprocess

button = Button(21)

def pressed():
    print("pressed")
    subprocess.call(['sudo', '/home/pi/ISSButton/bin/show_hero.sh'])
    
button.when_pressed = pressed

pause()
