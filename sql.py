import os
import time
import pyautogui as pag
import pygetwindow as gw

class BrightnessController:
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
        pag.scroll(500)
