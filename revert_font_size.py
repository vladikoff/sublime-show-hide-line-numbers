import sublime
import sublime_plugin

def is_sublime_text_3():
    """Returns True if this plugin is currently being run in Sublime Text 3."""
    try:
        return int(sublime.version()) >= 3000
    except ValueError:
        return sys.hexversion >= 0x030000F0

def plugin_loaded():
    """Called when this plugin is loaded; Sublime Text 3 API."""
    pass

def plugin_unloaded():
    """Called when this plugin is unloaded; Sublime Text 3 API."""
    pass

class ShowHideLineNumbers(sublime_plugin.ApplicationCommand):
    """

    Based on code by bizoo
    http://www.sublimetext.com/forum/viewtopic.php?f=3&t=9508
    """
    def run(self):
        preferences = sublime.load_settings("Preferences.sublime-settings")
        preferences.set("line_numbers", not preferences.get("line_numbers"))
        sublime.save_settings("Preferences.sublime-settings")

