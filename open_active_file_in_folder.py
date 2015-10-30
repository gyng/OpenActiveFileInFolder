import sublime
import sublime_plugin
import os

class OpenActiveFileInFolderCommand(sublime_plugin.WindowCommand):
    def run(self):
        active_file = self.window.active_view().file_name()
        directory = os.path.dirname(active_file)

        self.window.run_command('new_window')
        new_window = sublime.active_window()

        new_folder_settings = { 'folders': [{ 'path': directory }] }
        new_window.set_project_data(new_folder_settings)
        new_window.open_file(active_file)
