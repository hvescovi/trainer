# pip3 install pyscreenshot
#  pip3 install pynput
# pip3 install wxpython

import pyscreenshot as ig
import gi
# from pynput.mouse import Listener
import logging

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import os

# https://discourse.gnome.org/t/top-level-window-transparency-in-newer-versions-of-gtk/2210

#from gi.repository import Gdk

# default positions and height/width
x = 0
y = 0
h = 400
w = 500

class Select(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self) #, title="Selection window")

        # self.set_decorated(False)        
        
        #box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box = Gtk.Box()
        box.set_property("margin", 30) # border
        self.add(box) 
        
        #self.msg = Gtk.Label("Select the area to screenshot")
        #box.pack_start(self.msg, True, True, 0)

        self.btn_select = Gtk.Button(label="Ok")
        self.btn_select.connect("clicked", self.select_action)
        box.pack_start(self.btn_select, True, True, 0)

        # 4 commands to provide transparency
        self.set_opacity(0.4)
        scr = self.get_screen()
        vis = scr.get_rgba_visual()
        self.set_visual(vis)
        
    def select_action(self, widget):
        #Listener.stop

        # get size
        global w
        w = self.get_size()[0]
        global h
        h = self.get_size()[1]

# https://developer.gnome.org/pygtk/stable/class-gtkwindow.html#method-gtkwindow--get-position

        # get coordinates
        global x
        x = self.get_position()[0]
        global y
        y = self.get_position()[1]
        #print(x, y)

        self.hide() # hide the select window  

# https://pynput.readthedocs.io/en/latest/mouse.html
# https://nitratine.net/blog/post/how-to-get-mouse-clicks-with-python/

# logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

'''
def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))
    print("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed:
        logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))

        button1 = Gtk.Button(label="Hello, world!")
        button1.set_margin_bottom(50)
        button1.set_margin_top(50)

        box = Gtk.Box(spacing=50)
        box.pack_start(button1, True, True, 50)

        window = Gtk.Window(title="Selection box", name="toplevel")
        screen = window.get_screen()
        visual = screen.get_rgba_visual()
        window.set_visual(visual)
        window.add(box)
        window.show_all()
        window.connect("destroy", Gtk.main_quit)

'''

class Shooter(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Trainer: shooter")

        self.set_default_size(300, 250)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.set_property("margin", 8) # adicionar uma borda na janela
        self.add(box) # inserir o layout na janela
        
        self.msg = Gtk.Label("Screenshot description: ") # criar um rótulo na janela
        box.pack_start(self.msg, True, True, 0)
        
        self.txt_description = Gtk.TextView()# caixa de entrada
        self.txt_description.set_wrap_mode(Gtk.WrapMode.CHAR) # wrap as you type
        #self.descricao.get_buffer().set_text("enter \n your \n description")
        #self.descricao.set_width_chars(30)
        #self.descricao.set_text("enter \n your \n description")
        box.pack_start(self.txt_description, True, True, 0)
        
        self.btn_area = Gtk.Button(label="Area") # criar botão "Ok"
        self.btn_area.connect("clicked", self.area) # associar evento de clique ao botão
        box.pack_start(self.btn_area, True, True, 0)

        self.button = Gtk.Button(label="Save") # criar botão 
        self.button.connect("clicked", self.salvar) # associar evento de clique ao botão
        box.pack_start(self.button, True, True, 0)

        hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        hbox1.set_property("margin", 8) 
        box.pack_start(hbox1, True, True, 0)

        self.lbl_filename = Gtk.Label("Filename: ")
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

        self.lbl_folder = Gtk.Label("Folder: ")
        hbox2.pack_start(self.lbl_folder, True, True, 0)

        self.txt_folder = Gtk.Entry()
        self.txt_folder.set_text(os.getcwd())
        hbox2.pack_start(self.txt_folder, True, True, 0)


        self.lbl_message = Gtk.Label("Welcome")
        box.pack_start(self.lbl_message, True, True, 0)

        # selection window
        self.w2 = Select() # instanciar janela de seleção
        self.w2.set_position(Gtk.WindowPosition.CENTER) # initial position
        self.w2.set_default_size(h,w) # default size of selection window        

    def area(self, widget):

        self.w2.show_all() # show select window

        #with Listener(on_move=on_move, on_click=on_click) as listener:
        #    listener.join()

    def salvar(self, widget):
        if self.txt_filenumber.get_text() == "SET":
            self.lbl_message.set_text("PLEASE SET THE file counter")
        else:
            num = self.txt_filenumber.get_text()
            
            titlebarheight = 40 # 50 pixels for titlebar size
            im = ig.grab(bbox=(x, y, x+w, y+h+titlebarheight))  # X1,Y1,X2,Y2

            # prepare the image filename
            img_filename = self.txt_filename.get_text() + self.txt_filenumber.get_text() + '.png'

            # get the description
            buf = self.txt_description.get_buffer()
            bi = buf.get_start_iter()
            be = buf.get_end_iter()
            description = buf.get_text(bi, be, True)

            # prepare the newline
            newline = "\n" + img_filename + "|" + description + "| 1,1 | 100, 100"

            # prepare the sequencer filename
            txt_filename = self.txt_folder.get_text() + "/sequencer.txt"
            
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

            # im.show()

            self.txt_filenumber.set_text(str(int(num) + 1)) # increment the counter
            self.txt_description.get_buffer().set_text("") # clear the description

            self.lbl_message = "screenshot SAVED!"

win = Shooter() # instanciar janela

win.connect("destroy", Gtk.main_quit) # encerrar o programa ao fechar a janela
# win.set_position(Gtk.WindowPosition.CENTER) # centralizar janela
win.show_all() # exibir janela
Gtk.main() # início do gtk (loop contínuo)