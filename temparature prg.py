import screen_brightness_control as sbc
import time
import pyautogui as pag
import os

# Get current brightness (for reference)
current_brightness = sbc.get_brightness(display=0)[0]
print(f"Current brightness: {current_brightness}%")

# Set brightness to 50%
sbc.set_brightness(50)
print("Brightness set to 50%")
#having a delay of 5 sec
time.sleep(2)
pag.hotkey('win', 'a')
time.sleep(5)
current_brightness = sbc.get_brightness(display=0)[0]
sbc.set_brightness(75)
print("Brightness set to 75%")
latest_brightness=sbc.get_brightness(display=0)[0]
time.sleep(2)
while True:
    # Get the current brightness of the first display
    current_brightness = sbc.get_brightness(display=0)[0]

    # If brightness is already 100%, stop the loop
    if current_brightness >= 100:
        print("Brightness already at 100%. Task ended.")
        break

    # Increase brightness by 1%
    new_brightness = current_brightness + 1
    sbc.set_brightness(new_brightness, display=0)

    print(f"Brightness set to {new_brightness}%")
    time.sleep(5)  # Small pause for visible change
os.system('start shell:AppsFolder\\AppUp.IntelArcSoftware_8j3eq9eme6ctt!INTELGRAPHICSSOFTWARE')

# Wait for the app to open
time.sleep(10)  # Adjust based on your computer speed
pag.click(x=95, y=225)  # coordinates of "Display" tab
pag.scroll(500)




