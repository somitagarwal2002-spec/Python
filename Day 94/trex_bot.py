import time
import pyautogui
from PIL import Image

# (left, top, width, height)
SCAN_REGION = (520, 390, 180, 60)
PIXEL_THRESHOLD = 120

time.sleep(3)
pyautogui.press("space")

while True:
    img = pyautogui.screenshot(region=SCAN_REGION).convert("L")
    pixels = img.load()
    obstacle = False

    for x in range(img.width):
        for y in range(img.height):
            if pixels[x, y] < PIXEL_THRESHOLD:
                obstacle = True
                break
        if obstacle:
            break

    if obstacle:
        pyautogui.press("space")
        time.sleep(0.05)
