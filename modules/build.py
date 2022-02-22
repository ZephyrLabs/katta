import os
from modules.tui import tui

class build:
    def __init__(self):
        tui.flush(tui) 

        if(os.path.exists("buildtools/gcc-arm-none-eabi") and os.path.exists("buildtools/nrf5_sdk")):pass
        else:
            print(tui.cfmt("Toolchain and SDK are missing!", 1, 0, "orange"))
            tui.enter(tui)
            return

        opt = tui.menu(tui, tui.cfmt("build system", 1, 1, "orange"), ("manage source", "build"))

        project = "InfiniTime"
        src_cmd = "git clone https://github.com/InfiniTimeOrg/InfiniTime.git --recurse-submodules"

        # manage source menu 
        if(opt == "1"):
            tui.flush(tui) 
            opt = tui.menu(tui, tui.cfmt("", 1, 0, "orange"), ("get source", "update existing"))
            if(opt == "1"):
                os.system("rm -rf "+project)
                os.system(src_cmd)
                tui.enter(tui)
            if(opt == "2"):
                os.system("cd " + project + " && git pull")
                tui.enter(tui)

        if(opt == "2"):
            tui.flush(tui)
            if(os.path.exists("InfiniTime")): pass
            else: 
                try:
                    os.system(src_cmd)
                except Exception as e:
                    print(tui.cfmt("looks like something went wrong :(", 1, 0, "pink"))
                    print("error: \n" + e)
                    tui.enter(tui)

            opt = tui.menu(tui, tui.cfmt("Katta build system", 1, 0, "orange"), ("build dfu", "build mcuboot-app"))

            if(os.path.exists("InfiniTime/build")): pass
            else:
                os.system("cd InfiniTime" 
                        " && mkdir build")

            if(opt == "1"):
                os.system("cd InfiniTime" 
                        " && cd build"
                        " && cmake -DARM_NONE_EABI_TOOLCHAIN_PATH={}/buildtools/gcc-arm-none-eabi" 
                        " -DNRF5_SDK_PATH={}/buildtools/nrf5_sdk"
                        " -DNRFJPROG=/opt/nrfjprog/nrfjprog" 
                        " -DBUILD_DFU=1 ../"
                        " && make -j8 pinetime-mcuboot-app".format(os.getcwd(), os.getcwd()))
                        
            if(opt == "2"):
                os.system("cd InfiniTime" 
                        " && cd build"
                        " && cmake -DARM_NONE_EABI_TOOLCHAIN_PATH={}/buildtools/gcc-arm-none-eabi" 
                        " -DNRF5_SDK_PATH={}/buildtools/nrf5_sdk"
                        " -DNRFJPROG=/opt/nrfjprog/nrfjprog"
                        " -DUSE-OPENOCD=1 ../"
                        " && make -j8 pinetime-mcuboot-app".format(os.getcwd(), os.getcwd()))

                tui.enter(tui)


            
