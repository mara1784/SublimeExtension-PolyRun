import sublime
import sublime_plugin
import subprocess
import platform

class RunPythonScriptsInMoreTerminalsCommand(sublime_plugin.WindowCommand):
    def run(self):
        view = self.window.active_view() # current file on display

        if view is None or view.file_name() is None:
            sublime.error_message("Before first load you must save the file")
            return

        view.run_command("save")
        file = view.file_name()

        match platform.system():
            case "Windows":
                cmd = [
                    "cmd.exe",
                    "/c",
                    "start",
                    "cmd",
                    "/k",
                    f'python3 -u "{file}"'
                ]

            case "Linux":
                cmd = [
                    "x-terminal-emulator",
                    "-e",
                    "bash",
                    "-ic",
                    # there you can costumize languages that run scripts:
                    '''
                    python3 -u "{file}";
                    echo;
                    read -p "Press Enter for close..."
                    '''.format(file=file)
                ]
            case "Darwin":
                script = (
                    f'tell application "Terminal" to do script '
                    f'"python3 -u \\"{file}\\"; echo; read -p \\"Press Enter to close...\\""'
                )
                cmd = ["osascript", "-e", script]
        subprocess.Popen(cmd)
