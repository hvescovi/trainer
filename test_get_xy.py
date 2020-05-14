import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def on_button_clicked(widget):
  popup = Gtk.Window(type=Gtk.WindowType.POPUP)
  # optionally you may set an appropriate type hint, but it's not required.
  popup.set_attached_to(entry)
  popup.set_transient_for(window)

  gdk_window = entry.get_window()
  gdk_window_origin = gdk_window.get_origin()
  x = gdk_window_origin[1]
  y = gdk_window_origin[2]
  allocation = entry.get_allocation()
  x += allocation.x
  y += allocation.y + allocation.height

  #popup.move(x, y)
  popup.move(400, 500)
  print(x, y)
  popup.show_all()

button = Gtk.Button(label="Hello")
button.connect('clicked', on_button_clicked)
entry = Gtk.Entry()
layout = Gtk.VBox()
layout.pack_start(button, False, True, 0)
layout.pack_start(entry, False, True, 0)

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)
window.add(layout)
window.show_all()

Gtk.main()