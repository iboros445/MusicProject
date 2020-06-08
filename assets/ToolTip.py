from tkinter import *
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     # How long before it shows , in miliseconds
        self.wraplength = 180   # How long of a row before text wraps (pixels)
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)       # cursor enters widget
        self.widget.bind("<Leave>", self.leave)       # cursor leaves widget
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None


    def enter(self, event=None):
        self.schedule()


    def leave(self, event=None):
        self.unschedule()
        self.hidetip()


    def schedule(self):
        """ Shows the tip """
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)


    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)


    def showtip(self, event=None):
        """ Creates the window for the tip """
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        # The shift from top/left of the widget, for the tip to show
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window (like Frame, used for pop-up or dialogue)
        self.tw = Toplevel(self.widget)
        # Leaves only the label and removes the app window decorations (wm - window manager)
        self.tw.wm_overrideredirect(True)
        #self.tw.wm_overrideredirect(False)  # To see windows decorations.
        self.tw.wm_geometry("+%d+%d" % (x, y))
        # For Mac OS
        try:
            self.tw.tk.call("::tk::unsupported::MacWindowStyle",
                       "style", self.tw._w,
                       "help", "noActivates")
        except TclError:
            pass
        label = Label(self.tw, text=self.text, justify='left',
                       background="white", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)


    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()
