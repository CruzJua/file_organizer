from rich import print
from tkinter import filedialog
import getpass
import os

user = getpass.getuser()

def select_folder_to_organize():
    folder_path = filedialog.askdirectory(
        title="Select Folder to Organize"
    )
    if folder_path:
        print(f"""
[bold cyan]Selected Folder:[/bold cyan] [green]{folder_path}[/green]
""")
        return folder_path
    else:
        print("[bold red]No folder selected.[/bold red]")
        return None

def organize_folder(folder_path: str = f"C:/Users/{user}/Downlads"):
    if not os.path.exists(folder_path):
        print(f"[bold red]Folder path does not exist: [blink]{folder_path}[blink][/bold red]")
        return
    else:
        print(f"[bold blue]Oganizing folder:[/bold blue] [green]{folder_path}[/green]")
        files = os.listdir(folder_path)
        print(f"[bold yellow]Found {len(files)} files in the folder.[/bold yellow]")
        print(f"these are the files: [magenta]{files}[/magenta]")
        return
    

if __name__ == "__main__":
    folder = select_folder_to_organize()
    organize_folder(folder)