# https://stackoverflow.com/questions/28512092/cairo-and-gdk-window-with-gtk-drawingarea-using-python-gobject-introspection-and

from gi.repository import Gtk

def draw_cb(widget, cr):
  cr.set_source_rgba(0,0,0,0.5)
  cr.rectangle(50,75,100,100)
  cr.fill()
  return False

win = Gtk.Window()

win.set_title("test")
win.set_default_size(800,600)
win.connect('delete-event', Gtk.main_quit)
da=Gtk.DrawingArea()
da.connect('draw', draw_cb)
win.add(da)
win.show_all()
Gtk.main()