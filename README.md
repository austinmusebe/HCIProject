# Moodnest Setup

## Installing

### Cloning
- Clone the repository locally onto your computer

### Setting up the python
- In the directory where you cloned it, run this command in your terminal `python -m venv venv`. This will create a virtual python environment for us to run in.
- Depending on the terminal you're using, it's going to be a slightly different command, but assuming you're on Windows and using the Command Prompt, you're going to want to execute `\venv\Scripts\activate`. 
- If you're using Powershell, that would be `\venv\Scripts\activate.bat`.

- Now that you're in the virtual environment, run this command to install Flask and it's SQL implementation. (also date time as it may not work initially)

`pip install Flask Flask-SQLAlchemy datetime` 

or

`pip install Flask Flask-SQLAlchemy` if datetime is already installed which it usually is.

## Getting the website running
- Navigate to the folder containing 'app.py' and run this command in your terminal `python -m app.py`. <br /> The terminal should give you the address where you can access the website in your web browser.
