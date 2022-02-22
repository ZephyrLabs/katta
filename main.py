from modules.tui import tui
from modules.toolchain import toolchain
from modules.build import build

class katta:
    def __init__(self):
        while(1):
            tui.flush(tui)
            opt = tui.menu(tui, tui.cfmt("Katta build system", 1, 1, "orange"), ("build", "toolchain management"))

            # build menu
            if(opt == "1"):
                build()

            # toolchain menu
            if(opt == "2"):
                toolchain()
            
            if(opt == "exit"):
                break
katta()
