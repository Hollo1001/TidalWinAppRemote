I might overhaul this app to use the webplayer instead, as it will make a lot of things a lot easier.

# Tidal Remote Control Application

A Python-based web application for remotely controlling the Tidal desktop application. This application uses Flask for the web server, `pywinauto` for controlling the Tidal window, and `pytesseract` for Optical Character Recognition (OCR).

## Features

- Control playback (play, pause, next, previous, shuffle).
- Adjust volume and seek within tracks.
- Search functionality and queuing.
- Responsive web UI for control from a mobile device or desktop.
- Automatically refocuses the last active application after executing a command.

## Requirements

- Python 3.6 or later.
- Tidal Desktop Application.
- Tesseract OCR Engine.

## TODO
 - Overhaul Web UI
 - More queue management (removing, or moving song)
 - Refactor the code to be easier readable
 - suggested tracks
 - play albums and public playlists
 - radios / mixes
 - playlist management (create, add, remove, like, delete, unlike)
 # If possible
 - preview search on webui
 - list users playlist, tracks and artists on webui

## Installation

### Python Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### Tesseract OCR Engine

Install Tesseract via Chocolatey (Windows):

```bash
choco install tesseract
```

Ensure Tesseract's path is correctly set in the script:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

## Usage

1. Start the Tidal application on your system.
2. Run the Python script to start the Flask server:

   ```bash
   python TidalWinAppRemote.py
   ```

3. Open a web browser and navigate to `http://localhost:5000`.
4. Use the web interface to control the Tidal application.

## Important Notes

- The application must be run with appropriate permissions to interact with the Tidal window.
- The OCR functionality may require fine-tuning based on your system configuration and Tidal's interface.
```
