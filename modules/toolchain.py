import wget
import os
import platform

from modules.tui import tui

class toolchain:
    def __init__(self):

        plat = {
            "Windows": "win32",
            "Linux": "linux",
            "MacOS": "darwin",
        }.get(platform.system(), "")

        arch = {
            "AMD64": "x64",
            "x86_64": "x64",
            "i386": "ia32",
            "aarch64": "aarch64"

        }.get(platform.machine(), "")

        un_plat = ("win32", "darwin")
        un_arch = ("ia32",)

        if not plat or not arch:
            print(tui.cfmt("Unable to determine appropriate toolchain.", 1, 0, "pink"))
            tui.enter(tui)
            return
        
        print("your system is", tui.cfmt(plat, 1, 0, "mint"))
        print("your arch is", tui.cfmt(arch, 1, 0, "mint"))
        print("\n")

        if(arch in un_arch):
            print(tui.cfmt(arch, 1, 0, "mint"), "is currently", tui.cfmt("not supported", 1, 0, "pink"))
            tui.enter(tui)
            return

        if(plat in un_plat):
            print(tui.cfmt(plat, 1, 0, "mint"), "is currently", tui.cfmt("not supported", 1, 0, "pink"))
            tui.enter(tui)
            return
        
        toolchain_url = ""

        # urls for toolchain
        if(plat == 'linux' and arch == 'x64'):
            toolchain_url = "https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2"

        if(plat == 'linux' and arch == 'x64'):
            toolchain_url = "https://armkeil.blob.core.windows.net/developer/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-aarch64-linux.tar.bz2"

        sdk_url = "https://developer.nordicsemi.com/nRF5_SDK/nRF5_SDK_v15.x.x/nRF5_SDK_15.3.0_59ac345.zip"

        if(os.path.exists("buildtools/gcc-arm-none-eabi") and os.path.exists("buildtools/nrf5_sdk")):
            print("toolchain and sdk are already installed")
            opt = tui.menu(tui, tui.cfmt("do you want to re-install the toolchain and sdk ?", 1, 0, "pink"))
            if(opt == "1"):
                print(tui.cfmt("reinstalling...", 1, 0, "yellow"), "\n")
                os.system("rm -rf buildtools")
        try:
            self.install(toolchain_url, sdk_url)
            self.cleanup()
        except Exception as e:
            print(tui.cfmt("looks like something went wrong :(", 1, 0, "pink"))
            self.cleanup()

    def install(self, toolchain_url, sdk_url):
        if(os.path.exists("buildtools")): pass
        else: 
            # create a place to store the toolchain and sdk
            os.system("mkdir buildtools")

        if(os.path.exists("buildtools/gcc-arm-none-eabi")): 
            print(tui.cfmt("toolchain is installed", 1, 0, "mint"), "\n")
        else: 
            # download toolchain
            print(tui.cfmt("downloading toolchain...", 1, 0, "mint"))
            wget.download(url=toolchain_url, out="buildtools/gcc-arm-none-eabi.tar.bz2")

            print(tui.cfmt("\nextracting toolchain...", 1, 0, "mint"))
            os.system("cd buildtools && tar -xf gcc-arm-none-eabi.tar.bz2 && mv gcc-arm-none-eabi-9-2020-q2-update gcc-arm-none-eabi")
            print(tui.cfmt("toolchain is installed", 1, 0, "mint"), "\n")

        if(os.path.exists("buildtools/nrf5_sdk")): 
            print(tui.cfmt("sdk is installed", 1, 0, "mint"), "\n")
        else: 
            # download sdk
            print(tui.cfmt("downloading sdk...", 1, 0, "mint"))
            wget.download(url=sdk_url, out="buildtools/nrf5_sdk.zip")

            print(tui.cfmt("\nextracting sdk...", 1, 0, "mint"))
            os.system("cd buildtools && unzip -q nrf5_sdk.zip && mv nRF5_SDK_15.3.0_59ac345 nrf5_sdk")
            print(tui.cfmt("sdk is installed", 1, 0, "mint"), "\n")

        tui.enter(tui)
        return
    
    def cleanup(self):
        os.system("cd buildtools && rm -rf *.tmp")
        return