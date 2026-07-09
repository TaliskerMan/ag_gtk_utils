import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gtk

class BaseWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        app = kwargs.pop('app', None)
        application = kwargs.pop('application', None)
        if app is not None:
            kwargs['application'] = app
        elif application is not None:
            kwargs['application'] = application
            
        title = kwargs.pop('title', None)
        if title is not None:
            kwargs['title'] = title
            
        default_width = kwargs.pop('default_width', None)
        default_height = kwargs.pop('default_height', None)
        
        super().__init__(**kwargs)
        
        if default_width is not None:
            self.set_default_size(default_width, default_height or 600)
            
    def set_theme(self, scheme, save=False):
        style_manager = Adw.StyleManager.get_default()
        style_manager.set_color_scheme(scheme)
