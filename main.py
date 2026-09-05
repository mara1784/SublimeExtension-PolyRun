import sublime
import sublime_plugin
import subprocess
import os

class RunPythonScriptsInMoreTerminalsCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view() # current file on display

        if view is None or view.file_name() is None:
            sublime.error_message("Before first load you must save the file")
            return

        view.run_command("save")
        file = view.file_name()

        cmd = [
            "x-terminal-emulator",
            "-e",
            "bash",
            "-c",
            # there you can costumize languages that run scripts:
            f'''
            python3 -u "{file}";
            echo;
            read -p "Press Enter for close..."
            '''
        ]

        subprocess.Popen(cmd)
