Running Instructions

This application has been tested on Python 3.8 and 
isn't guaranteed to work on previous or later versions.

To download the required dependencies, open a command prompt
and enter:
pip install -r requirements.txt

To check if your system is running 32 bit or 64 bit, enter
'python' and check the end of the first line. 

If the system is 32-bit, enter:
pip install PyAudio-0.2.11-cp38-cp38-win32.whl
Otherwise enter:
pip install PyAudio-0.2.11-cp38-cp38-win_amd64.whl

The path at the top of MyLogParser.py is the default Windows 
install directory for Hearthstone. If yours is different, 
replace the path with the appropriate one. 

To enable Hearthstone logging, create a log.config file in the 
folder at this location: %LOCALAPPDATA%/Blizzard/Hearthstone
Put the following text in the file
[Power]
LogLevel=1
FilePrinting=true
ConsolePrinting=true
ScreenPrinting=false


To run the application, enter:
python Main.py