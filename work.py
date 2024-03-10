import pyautogui
from time import sleep

def money():
    import time
    time.sleep(5) 
    for _ in range(100): 
       prefix = "/" # Change this prefix to whatever prefix your server uses
       pyautogui.write(prefix + "work") #you can change this to be whatever command you want
       pyautogui.press("Enter")
       time.sleep(120) #Change this to the cooldown that the server uses

money()