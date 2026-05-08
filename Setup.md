# Setup Guide for the Physical Control of the Antenna System with 2 DoF
### Created 5-8-26, Bertrand Juan
### Update Log


## Note this was originally done in Windows 10 
### Installation requirements

Start with by installing the following
* [Gpredict](https://oz9aec.dk/gpredict/)
* [Arduino IDE](https://docs.arduino.cc/software/ide/)
* [Hamlib](https://github.com/Hamlib/Hamlib/wiki/Download)
    * Be sure to install the correct version I used Hamlib-w64-x.x.x.exe
* [bridge.py](./bridge.py)
    * This is the base bridge file that connects hamlib to COM port so Arduino can get info you will likely change a few things (Written by AI) 

### Gpredict
Once Gpredict is installed locate the exe file and open it up

[Official Gpredict documentation](https://www.sk0tm.se/wp-content/uploads/2023/12/gpredict-user-manual-2.2.pdf)

#### Cooper Ground Station Location
With in Gpredict go to the top left Edit > Preferences > General > Ground Station > Add new > Create your new Cooper Ground Station

I pulled these number off some web based service feel free to use more accurate numbers.

Center at 41 Cooper Square
1. Latitude 40.7285 North
2. Longitude 73.9899 West
3. Altitude 12m
    * Inorder for anything to have a chance of working you'll need to be on the roof

#### Module View




