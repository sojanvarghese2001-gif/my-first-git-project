
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