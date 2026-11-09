# Clock-app
A Clock, calendar, and weather app written in python
## Installation
### Recommended
Download the release for your system from the [latest release](https://github.com/dragonruler1000/Clock-app/releases/latest).
On linux you will need to mark it as executible `chmod +x clock-app-linux` then run it from the terminal `./clock-app-linux` make sure you have fontconfig installed sense it uses the system fontconfig instead of a bundled version.
### From source
Clone the repo, make a venv, install the requirements and run the app using python
```
git clone https://github.com/dragonruler1000/Clock-app.git | cd Clock-app
python -m venv .venv | source .venv/bin/activate
pip -r requirements.txt
python gui-main.py
```
## Features
- View the current time in 15 different formats (13 unique formats)
- see the current temp
- see the location (latitude, longitude, and elevation)
- see the forecast of the next 3 days with temperature, precipitation, wind-speed and direction.
- light mode and dark mode
## Screen shots
<img src="images/lightmode.png" title="Light mode" alt="Light mode" width="49%" height="auto">
<img src="images/darkmode.png" title="Dark mode" alt="Dark mode" width="49%" height="auto">
