from cmath import rect
import time
import psutil
from pywinauto.application import Application
from pywinauto.mouse import click
from flask import Flask, request
from pywinauto import Desktop
import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
from mss import mss
import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import pyautogui
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import keyboard

app = Flask(__name__)
tidal_window = None
process_name = "TIDAL.exe"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.form.get('command')
    if command:
        handle_command(command)
        print(f"Command '{command}' sent.")
    return redirect(url_for('index'))

@app.route('/command', methods=['POST'])
def receive_command():
    command = request.json.get('command')
    if command:
        handle_command(command)
        return {'status': 'Command received'}, 200
    return {'status': 'No command provided'}, 400

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


def capture_window_with_mss(hwnd):
    with mss() as sct:
        rect = win32gui.GetWindowRect(hwnd)
        monitor = {"top": rect[1], "left": rect[0], "width": rect[2] - rect[0], "height": rect[3] - rect[1]}
        sct_img = sct.grab(monitor)
        return Image.frombytes("RGB", sct_img.size, sct_img.rgb)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update the path

def Listener():
    print("Commands: open-settings, search, play, shuffle, prev-song, next-song, seek-back, seek-forward, volume-down, volume-up, prev-page, next-page, exit")

    while True:
        command = input("Enter command: ").lower()

        if command == "exit":
            break
        else:
            handle_command(command)

def handle_command(command):
    tidal_window.set_focus()

    if command == "open-settings":
        open_settings()
    elif command.startswith("search "):
        query = command[len("search "):]
        search(query)
    elif command == "play":
        play_song()
    elif command == "shuffle":
        shuffle()
    elif command == "prev-song":
        previous_song()
    elif command == "next-song":
        next_song()
    elif command == "seek-back":
        seek_backward()
    elif command == "seek-forward":
        seek_forward()
    elif command == "volume-down":
        decrease_volume()
    elif command == "volume-up":
        increase_volume()
    elif command == "prev-page":
        previous_page()
    elif command == "next-page":
        next_page()
    elif command.startswith("playlist "):
        query = command[len("playlist "):]
        playlist(query)
    elif command.startswith("queue "):
        query = command[len("queue "):]
        queue_song(query)
    elif command.startswith("queue_next "):
        query = command[len("queue_next "):]
        queue_next(query)
    else:
        print("Unknown command.")
    open_home()
    refocus_last_application()

def refocus_last_application():
    keyboard.send('alt+tab')
    time.sleep(0.1)

def get_tidal_main_window():
    global tidal_window
    """Find a process ID by its name."""
    for proc in psutil.process_iter():
        try:
            if process_name.lower() in proc.name().lower():
                try:
                    if proc.pid:
                        app = Application(backend="uia").connect(process=proc.pid,timeout=5)
                        tidal_window = app.window()
                        tidal_window.set_focus()
                        refocus_last_application()
                        return tidal_window
                except:
                        pass
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    print("No tidal window found.")

def click_absolute_position(x_offset, y_offset, button='left'):
    global tidal_window
    if tidal_window is None:
        tidal_window = get_tidal_main_window()

    rect = tidal_window.rectangle()
    abs_x = rect.left + x_offset
    abs_y = rect.top + y_offset

    # Save current mouse position
    current_mouse_x, current_mouse_y = pyautogui.position()

    # Perform the click
    click(button, coords=(abs_x, abs_y))

    # Move mouse back to original position
    pyautogui.moveTo(current_mouse_x, current_mouse_y)

def send_keystroke(keystrokes):
    global tidal_window
    if(tidal_window == None):
        tidal_window = get_tidal_main_window()
    tidal_window.type_keys(keystrokes, with_spaces=True)

def open_settings():
    send_keystroke('^,')

def search(query):
    send_keystroke('^f')
    time.sleep(0.1)
    send_keystroke('^a{DELETE}')
    time.sleep(0.1)
    send_keystroke(query)
    time.sleep(0.1)
    send_keystroke('{ENTER}')
    time.sleep(0.1)
    send_keystroke('{TAB 2}{ENTER}')
    time.sleep(0.1)
    click_absolute_position(314, 270)

def play_song():
    send_keystroke('{SPACE}')

def shuffle():
    send_keystroke('^s')

def previous_song():
    send_keystroke('^{LEFT}')

def next_song():
    send_keystroke('^{RIGHT}')

def seek_backward():
    send_keystroke('^+{LEFT}')

def seek_forward():
    send_keystroke('^+{RIGHT}')

def decrease_volume():
    send_keystroke('^{DOWN}')

def increase_volume():
    send_keystroke('^{UP}')

def previous_page():
    send_keystroke('^[')

def next_page():
    send_keystroke('^]')

def playlist(query):
    open_home()
    time.sleep(0.1)
    open_playlists()
    time.sleep(0.1)
    send_keystroke('{TAB 2}')
    send_keystroke(query)
    time.sleep(0.1)
    send_keystroke('{TAB 4}{ENTER}')


def open_home():
    click_absolute_position(20, 140)

def open_playlists():
    click_absolute_position(20, 362)

def queue_song(query):
    send_keystroke('^f')
    time.sleep(0.1)
    send_keystroke('^a{DELETE}')
    time.sleep(0.1)
    send_keystroke(query)
    time.sleep(0.1)
    send_keystroke('{ENTER}')
    time.sleep(0.1)
    send_keystroke('{TAB 2}{ENTER}')
    time.sleep(0.1)
    click_absolute_position(314, 270, "right")
    time.sleep(0.1)
    try:
        if (click_text("queue")):
            return
    except:
        pass
    try:
        if (click_text("next")):
            return
    except:
        pass
    try:
        if (click_text("now")):
            return
    except:
        pass

def queue_next(query):
    send_keystroke('^f')
    time.sleep(0.1)
    send_keystroke('^a{DELETE}')
    time.sleep(0.1)
    send_keystroke(query)
    time.sleep(0.1)
    send_keystroke('{ENTER}')
    time.sleep(0.1)
    send_keystroke('{TAB 2}{ENTER}')
    time.sleep(0.1)
    click_absolute_position(314, 270, "right")
    time.sleep(0.1)
    try:
        if (click_text("next")):
            return
    except:
        pass
    try:
        if (click_text("now")):
            return
    except:
        pass

def find_text_coordinates(text):
    global tidal_window
    try:
        # Bring the Tidal window to the front
        time.sleep(1)  # Short delay to ensure the window is in focus

        hwnd = tidal_window.wrapper_object().handle
        screenshot = capture_window_with_mss(hwnd)
        if screenshot is None:
            raise Exception("Failed to capture window image")

        #screenshot_path = "screenshot.png"
        #screenshot.save(screenshot_path)
        #print(f"Screenshot saved to {screenshot_path}")

        # Convert the image for OCR
        gray = cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGR2GRAY)
        # Experiment with different threshold values or methods
        _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)

        #thresh_path = "thresh.png"
        #cv2.imwrite(thresh_path, thresh)
        #print(f"Thresholded image saved to {thresh_path}")

        # Use pytesseract to detect text and its location
        data = pytesseract.image_to_data(thresh, output_type=pytesseract.Output.DICT)
        #print("OCR Output:", data)
        text_index = [i for i, t in enumerate(data['text']) if text.lower() in t.lower()]
        if text_index:
            x = data['left'][text_index[0]]
            y = data['top'][text_index[0]]
            print(f"Text '{text}' found at coordinates: ({x}, {y})")
            return (x, y)
        print(f"Text '{text}' not found")
    except Exception as e:
        print(f"An error occurred in find_text_coordinates: {e}")
    return None


def click_text(text):
    global tidal_window
    coords = find_text_coordinates(text)
    if coords:
        x, y = coords
        click_absolute_position(x, y)
        return True
    else:
        print(f"Unable to click: Text '{text}' not found")
        return False

def run_server():
    app.run(host='0.0.0.0', port=5000, debug=True)

def initialize_tidal_window():
    global tidal_window
    print("Searching for Tidal window...")
    tidal_window = get_tidal_main_window()
    if tidal_window is None:
        print("No Tidal window found. Please ensure Tidal is running.")

if __name__ == "__main__":
    initialize_tidal_window()
    run_server()
    # The command line interface can be removed or kept depending on your needs
