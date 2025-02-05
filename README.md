# DateWeekConverter

## What's this?

In my academic institution, semesters are divided into weeks: Week 1, Week 2, and so forth. 
I thought it would be handy to have a program that converts a date into a week number and vice versa for me.

Hence this simple Python program is born. It contains three core functionalities:

1. Set the date of the first day of a semester (this is essential for subsequent conversions and date calculations)
2. Convert a given date to a Week Number 
3. Convert a given Week Number (e.g. Week 7) and Day Number (Day 1 for Monday, Day 7 for Sunday) to a date

## Installation and Usage

### Linux/MacOS:

```bash
# Clone this git repo into your machine
git clone https://github.com/Cookiecodess/DateWeekConverter.git
# Go to the cloned repo
cd DateWeekConverter
# Allow execution permissions for the Python scripts
chmod +x start.py start-3.7.py
```

To run the Python script, type one of the following, according to the version of Python3 you have.

```bash
./start.py # This requires Python 3.10+
./start-3.7.py # This requires Python 3.7+
```

### Windows

Note: Open Powershell, not Command Line, for the below steps.

```powershell
# Clone this git repo into your machine
git clone https://github.com/Cookiecodess/DateWeekConverter.git
# Go to the cloned repo
cd DateWeekConverter
# Run the Python script
python3 start.py # This requires Python 3.10+. 
#python3 start-3.7.py # This requires Python 3.7+. Both versions work completely the same. Use this if your Python3 version is lower than 3.10
```

## First use

IMPORTANT: This is for Linux/MacOS users. Windows users can ignore this section.

Use your preferred text editor (Notepad, VS Code, nano, etc.) to open ```start.py``` and change the first line.

```python3
#!/usr/bin/python3 
# Change the above path to the path where python3 is stored on your machine. (Tip: type "which python3" into your shell)
# Do NOT remove the "#!"
```

You can find the path of python3 on your machine by typing ```which python3``` into your shell. 

```bash
$ which python3
/usr/bin/python3
```

There's a chance that your python3 path is exactly the same as the one already written in ```start.py```. 
If so, you're done and ready to start using the program. If not, change the path to your python3 path. 
**DO NOT REMOVE THE SHEBANG (```#!```).** It's the symbol that tells your shell interpreter that this 
script should be executed using Python3. Also note that there is a backslash (```\```) at the beginning 
of the path, right after the shebang.

```python3
#!usr/bin/python3  # THIS IS WRONG!!!

#!/usr/bin/python3 # This is correct
```




