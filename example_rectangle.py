# https://stackoverflow.com/questions/28512092/cairo-and-gdk-window-with-gtk-drawingarea-using-python-gobject-introspection-and

from gi.repository import Gtk, Gdk
import cairo


surface = None


def clear_surface():
    global surface

    cr = cairo.Context(surface)
    cr.set_source_rgb(1,1,1)
    cr.paint()

    del cr


def configure_event_cb(wid,evt):
    global surface

    if surface is not None:
        del surface
        surface = None

    win = wid.get_window()
    width = wid.get_allocated_width()
    height = wid.get_allocated_height()

    surface = win.create_similar_surface(
        cairo.CONTENT_COLOR,
        width,
        height)

    clear_surface()
    return True


def draw_cb(wid,cr):
    global surface

    cr.set_source_surface(surface,0,0)
    cr.paint()
    return False


def draw_brush(wid,x,y):
    global surface

    cr = cairo.Context(surface)
    cr.set_source_rgb(0,0,0)
    cr.rectangle(x-3,y-3,6,6)
    cr.fill()
    del cr

    wid.queue_draw_area(x-3,y-3,6,6)


def button_press_event_cb(wid,evt):
    global surface

    if surface is None:
        return False

    if evt.button == Gdk.BUTTON_PRIMARY:
        draw_brush(wid,evt.x,evt.y)
    elif evt.button == Gdk.BUTTON_SECONDARY:
        clear_surface()
        wid.queue_draw()

    return True


def motion_notify_event_cb(wid,evt):
    global surface

    if surface is None:
        return False

    if evt.state & Gdk.EventMask.BUTTON_PRESS_MASK:
        draw_brush(wid,evt.x,evt.y)

    return True


def close_window(wid):
    global surface

    if surface is not None:
        del surface
        surface = None

    Gtk.main_quit()


if __name__ == '__main__':
    win = Gtk.Window()
    win.set_title('Drawing Area')
    win.connect('destroy',close_window)
    win.set_border_width(8)

    frame = Gtk.Frame()
    frame.set_shadow_type(Gtk.ShadowType.IN)
    win.add(frame)

    da = Gtk.DrawingArea()
    da.set_size_request(100,100)
    frame.add(da)

    da.connect('draw',draw_cb)
    da.connect('configure-event',configure_event_cb)

    da.connect('motion-notify-event',motion_notify_event_cb)
    da.connect('button-press-event',button_press_event_cb)
    da.set_events(da.get_events() | Gdk.EventMask.BUTTON_PRESS_MASK | Gdk.EventMask.POINTER_MOTION_MASK)

    win.show_all()
    Gtk.main()