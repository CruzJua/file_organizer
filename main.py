import getpass
import os
from rich import print, print_json
from tkinter import filedialog
from pathlib import Path



user = getpass.getuser()
extension_destination = {".txt": "Notes", 
".pdf": "Documents"}

def select_folder_to_organize(verbose: bool = True) -> Path | None:
    folder_path = filedialog.askdirectory(
        title="Select Folder to Organize"
    )
    if folder_path:
        if verbose is True:
            print(f"""
[bold cyan]Selected Folder:[/bold cyan] [green]{folder_path}[/green]
""")
        return Path(folder_path)
    else:
        print("[bold red]No folder selected.[/bold red]")
        return None

def organize_folder(folder_path: Path = Path(f"C:/Users/{user}/Downloads"), verbose: bool = True):
    if not os.path.exists(folder_path):
        if verbose is True:
            print(f"[bold red]Folder path does not exist: [blink]{folder_path}[blink][/bold red]")
        return
    else:
        files = folder_path.iterdir()
        if verbose is True:
            pass
        return
    

if __name__ == "__main__":
    # folder = select_folder_to_organize(verbose=False)
    organize_folder()
    # print(extension_destination)