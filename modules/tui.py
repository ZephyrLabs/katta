import os

class tui:
    def cfmt(text, bold = 0, underline = 0, color = "white"):
        boldc = '\033[1m'
        endlc = '\033[0m'
        undlc = '\033[4m'

        color_lut = {
            'white':(255, 255, 255),\
            'black':(0, 0, 0),\
            'red':(255, 0, 0),
            'orange':(255, 128, 64),\
            'yellow':(255, 255, 0),\
            'lime':(128, 255, 128),\
            'green':(0, 255, 0),\
            'mint':(0, 255, 128),\
            'cyan':(0, 255, 255),\
            'light_blue':(0, 128, 255),\
            'blue':(0, 0, 255),\
            'purple':(128, 0, 255),\
            'magenta':(255, 0, 255),\
            'pink':(255, 0, 128)
        }

        if(color in color_lut):
            color_value = color_lut[color]
        else:
            color_value = color_lut['white']

        result_txt = ""

        if(bold): result_txt += boldc
        if(underline): result_txt += undlc

        result_txt += "\033[38;2;{};{};{}m{}\033[38;2;255;255;255m".\
                        format(color_value[0], color_value[1], color_value[2], text)
        
        result_txt += endlc

        return(result_txt)
    
    def menu(self, msg, options=("yes", "no")):
        while(1):
            print(msg)
            opts = []
            for i in options:
                print(self.cfmt(options.index(i) + 1, 1, 0, "lime"), self.cfmt(i), sep=": ")
                opts.append(options.index(i) + 1)

            opt = input(self.cfmt("> ", 1))
            tui.flush(tui)

            try:
                if(opt == "exit"):
                    return(opt)
                elif(int(opt) in opts):
                    return(opt)
            except Exception as e:
                pass

    def enter(self):
        input()
        os.system("clear")

    def flush(self):
        os.system("clear")