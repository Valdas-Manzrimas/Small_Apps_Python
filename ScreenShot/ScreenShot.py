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
    global VIEWPORT_SIZE, URL, SCREENSHOT_PATH
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

def command_line_args():
    if len(sys.argv) == 4:
        url = sys.argv[1]
        width = int(sys.argv[2])
        height = int(sys.argv[3])
        if url.startswith("http://") or url.startswith("https://"):
            global URL
            URL = url
        else:
            print("Error: Invalid URL entered")
            sys.exit(1)
        if width > 0 and height > 0:
            global VIEWPORT_SIZE
            VIEWPORT_SIZE = (width, height)
        else:
            print("Error: Invalid width or height entered")
            sys.exit(1)
    elif len(sys.argv) > 1:
        print("Error: Expected arguments not received"
        "Usage: python screenshot.py <url> <width> <height>")
        sys.exit(1)

def create_browser(settings):
    global VIEWPORT_SIZE, URL
    parent_window_handle = 0
    window_info = cef.WindowInfo()
    window_info.SetAsOffscreen(parent_window_handle)
    print("Viewport size: {size}".format(size=str(VIEWPORT_SIZE))) 
    print("Loading URL: {url}".format(url=URL))
    browser = cef.CreateBrowserSync(window_info=window_info, settings=settings, url=URL)
    browser.SetClientHandler(LoadHandler())
    browser.SetClientHandler(RenderHandler())
    browser.SendFocusEvent(True)
    browser.WasResized()

def save_screenshot(browser):
    global SCREENSHOT_PATH
    buffer_string = browser.GetUserData("OnPaint.buffer string")
    if not buffer_string:
        raise Exception("Buffer string was empty because OnPaint was never called")
    image = Image.frombytes("RGBA", VIEWPORT_SIZE, buffer_string, "raw", "RGBA", 0, 1)
    image.save(SCREENSHOT_PATH, "PNG")
    print("Saved screenshot to : {path}".format(path=SCREENSHOT_PATH))


def open_with_default_app(path):
    if sys.platform.startswith("darwin"):
        subprocess.call(("open", path))
    elif os.name == "nt":
        os.startfile(path)
    elif os.name == "posix":
        subprocess.call(("xdg-open", path)) 

def exit_app(browser):
    print("Closing browser and exiting application" )
    browser.CloseBrowser()
    cef.QuitMessageLoop()

class LoadHandler(object):
    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:
            sys.stdout.write(os.linesep)
            print("Website has been loaded")
            save_screenshot(browser)
            cef.PostTask(cef.TID_UI, exit_app, browser)

    def OnLoadError(self, browser, frame, error_code, failed_url, **_):
        if not frame.IsMain():
            return
        print("Failed to load url: {url}".format(url=failed_url))
        print("Error code: {code}".format(code=error_code))
        cef.PostTask(cef.TID_UI, exit_app, browser) 

class RenderHandler(object):
    def __init__(self):
        self.OnPaint_called = False

    def GetViewRect(self, rect_out, **_):
        rect_out.extend([0, 0, VIEWPORT_SIZE[0], VIEWPORT_SIZE[1]])
        return True
    
    def OnPaint(self, browser, element_type, paint_buffer, **_):
        if self.OnPaint_called:
            sys.stdout.write(".")
            sys.stdout.flush()
        else:
            sys.stdout.write("OnPaint")
            self.OnPaint_called = True
        if element_type == cef.PET_VIEW():
            buffer_string = paint_buffer.GetBytes(mode='rgba', origin='top-left')
            browser.SetUserData("OnPaint.buffer string", buffer_string)
        else:
            raise Exception("Unsupported element type in OnPaint")



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