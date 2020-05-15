import gi

gi.require_version("Gdk", "3.0")
gi.require_version("Gtk", "3.0")

from gi.repository import Gdk
from gi.repository import Gtk


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

button1 = Gtk.Button(label="Hello, world!")
button1.set_margin_bottom(50)
button1.set_margin_top(50)

box = Gtk.Box(spacing=50)
box.pack_start(button1, True, True, 50)

window = Gtk.Window(title="Hello World", name="toplevel")
screen = window.get_screen()
visual = screen.get_rgba_visual()
window.set_visual(visual)
window.add(box)
window.show_all()
window.connect("destroy", Gtk.main_quit)

Gtk.main()