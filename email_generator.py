import os
import pyautogui as pag
import time
import screen_brightness_control as sc
import pygetwindow as gw

class BrightnessController:
    def __init__(self,display=0):
        self.display = display
        try:
            self.current_brightness=sc.get_brightness(display=self.display)[0]
        except:
            self.current_brightness=0
            print(f"[INIT] Current brightness: {self.current_brightness}%")
        print(f"current brightness :{self.current_brightness}%")

    def set_brightness(self):
        """Set brightness to 75 """
        print(f"Brightness set to 75%")
        try:
            sc.set_brightness(75)
            self.current_brightness=75
        except Exception as e:
            print(f"[ERROR] Could not set brightness: {e}")

    def intel_graphics(self):
        print("[INFO] Opening Intel Graphics Software...")
        os.system('start shell:AppsFolder\\AppUp.IntelArcSoftware_8j3eq9eme6ctt!INTELGRAPHICSSOFTWARE')
        time.sleep(10)  # Wait for it to open

        # Find all visible Intel-related windows
        windows = [w for w in gw.getWindowsWithTitle('Intel') if w.visible]

        if windows:
            win = windows[0]
            print(f"[INFO] Found window: {win.title}")

            # Check if the window is already maximized/fullscreen
            if not win.isMaximized:
                print("[INFO] Window is not fullscreen — maximizing it.")
                win.maximize()
                time.sleep(1)
            else:
                print("[INFO] Window is already fullscreen.")
        else:
            print("[WARN] Could not find Intel Graphics window. Sending Win+Up as fallback.")
            pag.hotkey('win', 'up')  # Fallback maximize
            print("[INFO] Navigating to Display tab in Intel Graphics...")
            pag.click(x=95, y=225)
            time.sleep(5)
            pag.scroll(500)
            time.sleep(2)

    def automation_testcase(self):
        print("[INFO] Running automation test case...")

        self.set_brightness()
        self.intel_graphics()
        time.sleep(10)
        print("[INFO] Automation test completed.")
if __name__ == "__main__":
    controller = BrightnessController(display=0)
    controller.automation_testcase()