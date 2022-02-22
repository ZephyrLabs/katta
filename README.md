# Katta

![katta.png](katta.png)

an updated build script to replace the old Infinitime builder script

* requires `wget, wheel, cbor, intelhex, adafruit-nrfutil cryptography, mcuboot` via `pip` 
* `cmake` on your system
* features new terminal-ui interface
* more features planned ahead..

- [x] support for `x64` and `aarch64` linux environments for building
- [ ] support for win32 environment for building
- [ ] support for macOS environment for building

getting started:
* pull the repo 
```sh
git clone https://github.com/ZephyrLabs/katta.git
cd katta
```
* script can be launched simply with `python main.py` after that

* the number on the right is the menu option to select an option, 
typing exit will take you back to the main menu, or exit

* setup the toolchain first, make sure your device is a a part of the supported build envionments, however you will be notified of 
it when you run the script

* after that you can go ahead and enter the build menu and build 
the firmware

* built firmware will be present in 
 ```sh
$(pwd)/InfiniTime/build/
```

* you can pull your source code to the latest, within the manage source > update

* modify your code within the repo and build it again

* if you need to clean your repo and get a fresh clone of InfiniTime go to manage source > get source