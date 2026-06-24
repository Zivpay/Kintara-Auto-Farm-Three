## HOW TO INSTALL

### 1. Install Python
Ensure you have Python installed on your system (Python 3.8 or higher is recommended). 
* You can download it from [python.org](https://www.python.org/downloads/).
* **Crucial:** During installation, make sure to check the box that says **"Add Python to PATH"**.

### 2. Install Dependencies via requirements.txt
Open your terminal, command prompt, or VS Code terminal, navigate to the project directory, and run the following command to install all required libraries (`pyautogui`, `opencv-python`, `Pillow`, and `numpy`):

```bash
pip install -r requirements.txt

HOW TO USE
1. Game Setup
Log into the game and equip your Axe.
Move your character to an area where you can find a bunch of trees.

2. Run the Autoclicker
Double-click and open the Loop.bat file.
Immediately switch back to your game window. The autoclicker will automatically start scanning the screen and clicking the trees for you.

⚠️ Emergency Stop (Fail-Safe)
If the mouse starts moving out of control or you need to stop the script instantly:

Forcefully drag your mouse cursor to any of the four corners of your screen.

This will trigger PyAutoGUI's built-in fail-safe and immediately shut down the script.