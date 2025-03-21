import pyautogui
import time
import random

def move_mouse():
    while True:
        x, y = pyautogui.position()
        offset = random.randint(1, 10)  # Small movement
        pyautogui.moveTo(x + offset, y + offset, duration=0.2)
        pyautogui.moveTo(x, y, duration=0.2)  # Moves back to the original position
        wait_time = random.randint(240, 300)  # 4-5 minutes
        time.sleep(wait_time)

if __name__ == "__main__":
    print("Keeping you active for your lovely manager... 😈")
    move_mouse()