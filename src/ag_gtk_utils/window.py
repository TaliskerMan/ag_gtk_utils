import gi
gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Adw, Gio, Gtk, GLib

class BaseWindow(Adw.ApplicationWindow):
    """
    Base GTK application window providing common functionality like theme switching,
    about dialogs, and basic layout structure.
    """
    def __init__(self, app, title="App", default_width=800, default_height=600):
        super().__init__(application=app, title=title)
        self.set_default_size(default_width, default_height)
        
        self.split_view = Adw.OverlaySplitView()
        
        # We use a ToastOverlay in case subclasses want to show toasts
        self.toast_overlay = Adw.ToastOverlay()
        self.toast_overlay.set_child(self.split_view)
        self.set_content(self.toast_overlay)

    def _show_toast(self, message):
        """Creates and renders an Adw.Toast banner notification."""
        toast = Adw.Toast.new(message)
        self.toast_overlay.add_toast(toast)

    def show_message_dialog(self, heading, message):
        """Display a basic alert dialog box with a message."""
        dialog = Adw.MessageDialog(
            transient_for=self,
            heading=heading,
            body=message
        )
        dialog.add_response("ok", "OK")
        dialog.present()

    def set_theme(self, scheme, config_module=None, save=True):
        """
        Apply the selected Adw.ColorScheme.
        If config_module is provided and save is True, saves the preference.
        """
        manager = Adw.StyleManager.get_default()
        manager.set_color_scheme(scheme)
        if save and config_module and hasattr(config_module, 'set_theme_preference'):
            config_module.set_theme_preference(scheme)

    def build_theme_menu(self):
        """Returns a Gio.Menu with standard theme switching options."""
        theme_menu = Gio.Menu()
        theme_menu.append("System", "win.theme-system")
        theme_menu.append("Light", "win.theme-light")
        theme_menu.append("Dark", "win.theme-dark")
        return theme_menu

    def setup_theme_actions(self, config_module=None):
        """Sets up actions for theme switching."""
        action_system = Gio.SimpleAction.new("theme-system", None)
        action_system.connect("activate", lambda a, p: self.set_theme(Adw.ColorScheme.DEFAULT, config_module))
        self.add_action(action_system)

        action_light = Gio.SimpleAction.new("theme-light", None)
        action_light.connect("activate", lambda a, p: self.set_theme(Adw.ColorScheme.FORCE_LIGHT, config_module))
        self.add_action(action_light)

        action_dark = Gio.SimpleAction.new("theme-dark", None)
        action_dark.connect("activate", lambda a, p: self.set_theme(Adw.ColorScheme.FORCE_DARK, config_module))
        self.add_action(action_dark)

    def setup_base_layout(self, sidebar_title="Sidebar", content_title="Content"):
        """
        Sets up the base sidebar and content boxes for the split view.
        Returns (sidebar_box, content_box).
        """
        # Sidebar
        self.sidebar_page = Adw.NavigationPage(title=sidebar_title, tag="sidebar")
        sidebar_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.sidebar_header = Adw.HeaderBar(show_end_title_buttons=False)
        sidebar_box.append(self.sidebar_header)

        # Scrolled window for list in sidebar
        self.listbox = Gtk.ListBox()
        self.listbox.set_selection_mode(Gtk.SelectionMode.SINGLE)
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_child(self.listbox)
        scrolled.set_vexpand(True)
        sidebar_box.append(scrolled)

        self.sidebar_page.set_child(sidebar_box)
        self.split_view.set_sidebar(self.sidebar_page)
        self.split_view.set_min_sidebar_width(250)

        # Content
        self.content_page = Adw.NavigationPage(title=content_title, tag="content")
        content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.content_header = Adw.HeaderBar()
        content_box.append(self.content_header)

        self.content_page.set_child(content_box)
        self.split_view.set_content(self.content_page)

        return sidebar_box, content_box
