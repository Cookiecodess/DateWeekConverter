# DateWeekConverter

## What's this?

In my academic institution, semesters are divided into weeks: Week 1, Week 2, and so forth. 
I thought it would be handy to have a program that converts a date into a week number and vice versa for me.

Hence this simple Python program is born. It contains three core functionalities:

1. Set the date of the first day of a semester (this is essential for subsequent conversions and date calculations)
2. Convert a given date to a Week Number 
3. Convert a given Week Number (e.g. Week 7) and Day Number (Day 1 for Monday, Day 7 for Sunday) to a date

## Installation

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

## Before use

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
script should be executed using Python3. Also note that there is a slash (```/```) at the beginning 
of the path, right after the shebang.

```python3
#!usr/bin/python3  # THIS IS WRONG!!!

#!/usr/bin/python3 # This is correct
```

## Usage/Configuration

When you run ```start.py``` or ```start-3.7.py``` for the first time, 
you should encounter this message:

```
You haven't set the first day of the semester yet. Please enter the date of the first day of your semester (i.e. Monday of Week 1) in the format DD-MM-YYYY:
```

Enter the date of the first day of the semester (I'm speaking in the context of the use case I built this for, but you can use it for whatever you want -- maybe you want to mark the start of a new journey and want to know how many weeks have elapsed going into the future). A new ```.txt``` file will be generated in the same directory, in which the entered date will be recorded. By default, the file is named ```dwc_firstday.txt``` by default. For whatever reason you wish to change it, you may do so by changing the value of the constant ```FIRSTDATE_FILENAME``` in the Python scripts. 

Do not move or rename the file that stores the date of the first day if you are not familiar with Python. If you wish to rename it after setting the date, make sure to also edit the constant ```FIRSTDATE_FILENAME``` accordingly in the Python scripts so they don't break. Moving the file is also okay *if* you're familiar with how paths are handled in Python and tweak the constant accordingly.

### Configuring the date format

Only one date format is used throughout the program. The default date format in use is ```DD-MM-YYYY``` (e.g. ```03-10-2025```). If you don't like this at all, you can change the constant ```DATE_FORMAT``` in the Python scripts.

The default value of ```DATE_FORMAT```:

```python3
DATE_FORMAT = "%d-%m-%Y" 
```

For more on the format specifiers and what they signify, take a look at: <a target="_blank" href="https://www.w3schools.com/python/python_datetime.asp">Python Datetime - W3Schools</a>

### The rest

The rest is, I think, pretty intuitive, and you should be able to figure out how to use the program on your own. I hope you enjoy!




