from cal_lib import SpyderX
from cal_psy import GrayLevels
import numpy as np

# Path to libusb DLL (update this to your actual path)
libusb_path = r"C:\path\to\libusb-1.0.dll"

# Initialize SpyderX device
spyder = SpyderX(libusb_path)

# Initialize GrayLevels for luminance measurement
gl = GrayLevels(spyder, fullscr=True)

# Calibrate black level
gl.calibrate()

# Measure brightness levels
gammas = []
for i in range(3):  # Repeat for accuracy
    gfit = gl.measure(num_levels=12, wait_user=False)
    gammas.append(gfit.gamma)

# Print average brightness (gamma value)
print(f"Average Gamma Value: {np.mean(gammas):.3f}")

# Clean up
gl.close()