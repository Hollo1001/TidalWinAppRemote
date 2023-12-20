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
 ### If possible
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

## Why I'm Building a Tidal Remote Control App

As a user of Tidal, I've recognized a significant gap in its functionality compared to some of its competitors like Spotify. While Tidal is renowned for its high-quality audio, it lacks a crucial feature: the ability to control playback on a PC remotely from another device. This feature is especially vital for audiophiles and those with advanced audio setups who prefer to manage their music without being physically present at their computer.

A few years ago, there was an anticipation among the Tidal community when the company announced plans to introduce remote playback control. However, this feature never came to fruition and was subsequently removed from their upcoming features list. This absence in functionality has left a noticeable void in the user experience.

While there are premium players like Roon and Audirvana that offer advanced control features and integration with Tidal, they come with their own set of drawbacks. Firstly, they are quite expensive, making them less accessible for many users. Additionally, these players often introduce complexities and limitations that may not align with the needs or preferences of all users.

To bridge this gap, I have decided to create a remote control application for Tidal. My goal is to provide an accessible and user-friendly solution that allows users to enjoy Tidal's superior audio quality while offering the convenience of remote control. Whether it's skipping tracks, adjusting the volume, or exploring new playlists, this app aims to enable seamless control over Tidal playback from any device. The development of this app is driven by the desire to enhance the listening experience for Tidal users and to bring a much-needed functionality that has been long awaited.

## Important Notes

- The OCR functionality may require fine-tuning based on your system configuration and Tidal's interface.
