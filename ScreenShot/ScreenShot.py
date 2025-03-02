from cefpython3 import cefpython as cef
import os
import platform
import subprocess
import sys

try:
    from PIL import Image
except ImportError:
    print("PIP in not installed,"
    "Install it by typing 'pip install PIL' in the command prompt")
    sys.exit(1)

def main(url, w, h):
    global VIEWPORT_SIZE, url, SCREENSHOT_PATH
    URL = url
    VIEWPORT_SIZE = (int(w), int(h))
    SCREENSHOT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), "screenshot.png")

    check_versions()
    sys.excepthook = cef.ExceptHook()  # To shutdown all CEF processes on error

    if os.path.exists(SCREENSHOT_PATH):
        print("Remove old screenshot")
        os.remove(SCREENSHOT_PATH)

    command_line_args()

    setting = {
        "windowless_rendering_enabled": True
    }

    switches = {
        "disable-gpu": "",
        "disable-gpu-compositing": "",
        "enable-begin-frame-scheduling": "",
        "disable-surfaces": ""    }
    
    browser_settings = {
        "windowless_frame_rate": 30,
    }

    cef.Initialize(settings=setting, 
                   switches=switches)
                   
    create_browser(browser_settings)
    cef.MessageLoop()
    cef.Shutdown()
    print("Opening your screenshot with the default application")
    open_with_default_app(SCREENSHOT_PATH)

def check_versions():
    ver = cef.GetVersion()
    print("CEF Python {ver}".format(ver=ver["version"]))
    print("Chromium {ver}".format(ver=ver["chrome_version"]))
    print("CEF {ver}".format(ver=ver["cef_version"]))
    print("Python {ver} {arch}".format(ver=platform.python_version(), arch=platform.architecture()[0]))
    assert cef.__version__>="57.0", "CEF Python v57.0+ required to run this example"



import tkinter as tk

root = tk.Tk()
root.geometry("400x200")

class Widgets:
    def __init__(self, labtext, set_variable):
        self.lab = tk.Label(root, text=labtext)
        self.lab.pack()
        self.v = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.v)
        self.entry.pack()
        self.v.set(set_variable)

obj1 = Widgets("Enter website url: ", "https://www.google.com")
obj2 = Widgets("Enter width: ", "1024")
obj3 = Widgets("Enter height: ", "2048")
root.bind("<Return>", lambda x: main(obj1.v.get()), int(obj2.v.get()), int(obj3.v.get()))
lab4 = tk.Label(root, text="               ")
lab4.pack()

lab5 = tk.Label(root, text="Press the Enter key to create a screenshot")
lab5.pack()

root.mainloop()