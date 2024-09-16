# Free_Hand_Function_PC

## Overview
This project is about implementing a free-hand feature on a PC. As the first step, we will create a feature that navigates to a specific URL without using the keyboard. In this case, we will use OpenCV for face detection, and if a face is detected continuously for a certain period of time, the feature will automatically navigate to the specified URL.

## Usage
1. First, run the detect_function.py script. When executed, an OpenCV window will appear on the screen, and face detection will begin.

2. Second, if a face is continuously detected for a certain period, the OpenCV window will close, and the free-hand feature will be activated.

3. The free-hand feature first minimizes all other windows and ensures the desktop screen is visible. Then, on the desktop, the feature locates the coordinates of the Firefox icon and double-clicks it to open Firefox.

4. Next, the feature finds the specific character and locates its coordinates. Then, it performs a single click to enter the designated URL.



