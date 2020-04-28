# pip3 install pyscreenshot
#  pip3 install pynput
# pip3 install wxpython

import pyscreenshot as ig
import gi
from pynput.mouse import Listener
import logging

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# https://discourse.gnome.org/t/top-level-window-transparency-in-newer-versions-of-gtk/2210

from gi.repository import Gdk

CSS = b"""
#toplevel {
    background-color: rgba(0, 255, 255, 0.5);
}
"""

style_provider = Gtk.CssProvider()
style_provider.load_from_data(CSS)

Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(),
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)




logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

the_click = True

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))
    print("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, pressed):
    if pressed and the_click:
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
    
    else:
        pass

    the_click = not the_click

class Shooter(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Trainer: shooter")
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        box.set_property("margin", 8) # adicionar uma borda na janela
        self.add(box) # inserir o layout na janela
        
        self.msg = Gtk.Label("Descrição da tela: ") # criar um rótulo na janela
        box.pack_start(self.msg, True, True, 0)
        
        self.descricao = Gtk.Entry()# caixa de entrada
        box.pack_start(self.descricao, True, True, 0)
        
        self.btn_area = Gtk.Button(label="Area") # criar botão "Ok"
        self.btn_area.connect("clicked", self.area) # associar evento de clique ao botão
        box.pack_start(self.btn_area, True, True, 0)

        self.button = Gtk.Button(label="Salvar") # criar botão 
        self.button.connect("clicked", self.salvar) # associar evento de clique ao botão
        box.pack_start(self.button, True, True, 0)

    def area(self, widget):
        with Listener(on_move=on_move, on_click=on_click) as listener:
            listener.join()

    def salvar(self, widget):
        im = ig.grab(bbox=(10, 10, 510, 510))  # X1,Y1,X2,Y2
        # im.save('screenshot.png')
        im.show()





win = Shooter() # instanciar janela

win.connect("destroy", Gtk.main_quit) # encerrar o programa ao fechar a janela
win.set_position(Gtk.WindowPosition.CENTER) # centralizar janela
win.show_all() # exibir janela
Gtk.main() # início do gtk (loop contínuo)