# Python-Arduino-Programmer-GUI
A python GUI to flash Arduinos

This is an Windows Arduino compiler and flasher program that I did as an exercise. It uses Python3 and PyQT5. 

Instructions to use:
- Click on Install Tool to download and install the latest version of arduino-cli
- Browse the .ino file
- Input the target ID. This will be written in a file called _ID.H, if it exists.
- Select the correct COM port
- Click on Flash. This will compile the code and upload it.

The ID thing makes sense in a scenario where you have an installation with hundreds of microcontrollers, each having their own ID. In your IDE, make sure you define the ID in the code as "NODE_ID". Place the definition (#define NODE_ID 24 for example) in that file. Do not put antything else in the file, as the file will be rewritten and the contents deleted.

You can download the .exe file from the Release section or build it from the source code.

To build from scratch:
- `pip install PyQt5`
- `pip install pyserial`
- `pip install subprocess.run`
- `pip install pyinstaller`
- Download the source, got to the folder of the source, and type:
- `pyinstaller --onefile -w ArduinoFlasher_1.0.py`

After a minute, a .exe will be created in the dist folder. You can remove the other folder.

![Screenshot](/Source/GUI.PNG)

TO DO:
- [ ] Send output of the installation and flash scripts to the debug output
- [ ] Add a drop-down menu to select which microcontroller to use
- [ ] Detect if a .hex file has been chosen and uploadid directly rather than compiling first
- [ ] Test compatibility on Mac and Linux

Let me know if you find any bugs!
