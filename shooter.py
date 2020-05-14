# pip3 install pyscreenshot
# pip3 install pynput

import pyscreenshot as ig
import gi
#import logging

import time # for timer

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk

import os

# https://discourse.gnome.org/t/top-level-window-transparency-in-newer-versions-of-gtk/2210

#from gi.repository import Gdk

# default positions and height/width
x = 10
y = 10
h = 400
w = 500

catching = 0 # still selecting capture rectangle?
just_show = 0 # just showing (read-only) when select window opens?

color_blink = False # blink when just showing the box

class Select(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self) #, title="Selection window")
      
        self.canvas = Gtk.DrawingArea()
        self.canvas.connect("button-press-event", self.on_button_press)
        self.canvas.connect("motion-notify-event", self.on_mouse_move)
        self.canvas.set_events(self.canvas.get_events() |
                               Gdk.EventMask.BUTTON_MOTION_MASK |
                               #Gdk.EventMask.BUTTON1_MOTION_MASK |
                               #Gdk.EventMask.BUTTON2_MOTION_MASK |
                               #Gdk.EventMask.BUTTON3_MOTION_MASK |
                               Gdk.EventMask.BUTTON_PRESS_MASK | 
                               Gdk.EventMask.POINTER_MOTION_MASK)

        self.canvas.connect('draw', self.draw_cb) # draw 'event'
        self.add(self.canvas) # add to the window

        # 4 commands to provide transparency
        # TODO: set_opacity is deprecated
        self.set_opacity(0.4)
        scr = self.get_screen()
        vis = scr.get_rgba_visual()
        self.set_visual(vis)

    def draw_cb(self, widget, cr):
        global x
        global y
        global w
        global h
        global color_blink
        
        if color_blink:
            cr.set_source_rgba(3,25,35,0.7)
        else:
            cr.set_source_rgba(10,15,25,0.4)

        cr.rectangle(x,y,w,h)
        cr.fill()
        return False

    def on_mouse_move(self, widget, event):
        #print(event.x, event.y)
        global catching
        global x
        global y
        global w
        global h
        global just_show
        global color_blink

        if just_show == 0: # editing mode?
            # defining height and width?
            if catching == 1:
                w = abs(event.x - x)
                h = abs(event.y - y)
                # draw while sizing
                self.canvas.queue_draw() 
        else:
            # only repaint the rectangle blinking
            color_blink = not color_blink
            self.canvas.queue_draw() 


    def on_button_press(self, widget, event):
        global catching
        global x
        global y
        global w
        global h
        global just_show
        global color_blink

        if just_show == 1:
            self.hide() # close it!

        else: # just_show == 0, I hope

            if catching == 0: # defining initial x and y?
                color_blink = False
                x = event.x
                y = event.y
                #print(x, y)

            if catching == 1: # defining height and width?
                w = abs(event.x - x)
                h = abs(event.y - y)
                #print(w, h)

            catching += 1 # next step

            if catching == 2: # rectangle defined?
                self.canvas.queue_draw() # update the rectangle selected
                self.hide() # stop selection
                catching = 0 # next time, restart selecting

class Shooter(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Trainer: shooter")

        self.set_default_size(300, 250)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.set_property("margin", 8) # adicionar uma borda na janela
        self.add(box) # inserir o layout na janela
        
        self.msg = Gtk.Label() # criar um rótulo na janela
        self.msg.set_text("Screenshot description: ")
        box.pack_start(self.msg, True, True, 0)
        
        self.txt_description = Gtk.TextView()# caixa de entrada
        self.txt_description.set_wrap_mode(Gtk.WrapMode.CHAR) # wrap as you type
        box.pack_start(self.txt_description, True, True, 0)
        
        self.btn_area = Gtk.Button(label="Define it!") # criar botão "Ok"
        self.btn_area.connect("clicked", self.area) # associar evento de clique ao botão
        box.pack_start(self.btn_area, True, True, 0)

        self.btn_show_area = Gtk.Button(label="Just show") 
        self.btn_show_area.connect("clicked", self.show_area) 
        box.pack_start(self.btn_show_area, True, True, 0)

        self.button = Gtk.Button(label="Save") # criar botão 
        self.button.connect("clicked", self.salvar) # associar evento de clique ao botão
        box.pack_start(self.button, True, True, 0)

        # optional timer
        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox2.set_property("margin", 8) 
        self.lbl_timer = Gtk.Label(label="Time to shot (seconds): ")
        hbox2.pack_start(self.lbl_timer, True, True, 0)

        self.txt_timer = Gtk.Entry()
        self.txt_timer.set_text("0")
        hbox2.pack_start(self.txt_timer, True, True, 0)

        box.pack_start(hbox2, True, True, 0)

        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox1.set_property("margin", 8) 
        box.pack_start(hbox1, True, True, 0)

        self.lbl_filename = Gtk.Label(label="Filename: ")
        hbox1.pack_start(self.lbl_filename, True, True, 0)

        self.txt_filename = Gtk.Entry()
        self.txt_filename.set_text("screenshot-")
        hbox1.pack_start(self.txt_filename, True, True, 0)

        self.txt_filenumber = Gtk.Entry()
        self.txt_filenumber.set_text("SET")
        hbox1.pack_start(self.txt_filenumber, True, True, 0)

        hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox2.set_property("margin", 8) 
        box.pack_start(hbox2, True, True, 0)

        self.lbl_folder = Gtk.Label(label="Folder: ")
        hbox2.pack_start(self.lbl_folder, True, True, 0)

        self.txt_folder = Gtk.Entry()
        self.txt_folder.set_text(os.getcwd())
        hbox2.pack_start(self.txt_folder, True, True, 0)

        self.lbl_message = Gtk.Label(label="Welcome")
        box.pack_start(self.lbl_message, True, True, 0)

        # selection window
        self.w2 = Select() # instantiate select window
        self.w2.set_position(Gtk.WindowPosition.CENTER) # initial position
        self.w2.set_default_size(h,w) # default size of selection window        

    def area(self, widget):
        global just_show
        just_show = 0 # edition mode
        self.w2.show_all() # show select window
        self.w2.fullscreen() # expand to all screen

    def show_area(self, widget):
        global just_show
        just_show = 1 # read-only!
        self.w2.show_all() # show select window
        self.w2.fullscreen() # expand to all screen

    def salvar(self, widget):
        if self.txt_filenumber.get_text() == "SET":
            self.lbl_message.set_text("PLEASE SET THE file counter")
        else:
            # get time to sleep
            wait = int(self.txt_timer.get_text())
            time.sleep(wait)

            # get the file sequential number
            num = self.txt_filenumber.get_text()
            
            # take the screenshot!
            im = ig.grab(bbox=(x, y, x+w, y+h))  # X1,Y1,X2,Y2

            # prepare the image filename
            img_filename = self.txt_filename.get_text() + self.txt_filenumber.get_text() + '.png'

            # get the description
            buf = self.txt_description.get_buffer()
            bi = buf.get_start_iter()
            be = buf.get_end_iter()
            description = buf.get_text(bi, be, True)

            # prepare the newline (some default values)
            newline = "\n" + img_filename + "|" + description + "| 1,1 | 100, 100 | 110, 110"

            # prepare the sequencer filename
            txt_filename = self.txt_folder.get_text() + "/sequence.txt"
            
            # the file exists?
            if not os.path.exists(txt_filename):
                tag = 'w' # open for writing (create it)
            else:
                tag = 'a' # append the newline
            
            # include the newline!
            with open(txt_filename, tag) as file:
                file.write(newline)
            file.close()
            
            # save the screenshot
            im.save(img_filename)

            im.show()

            self.txt_filenumber.set_text(str(int(num) + 1)) # increment the counter
            self.txt_description.get_buffer().set_text("") # clear the description

            self.lbl_message = "screenshot SAVED!"

win = Shooter() # create window
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main() # start!