from tkinter import *
from tkinter import ttk, messagebox

from dao.book_repository_json import BookRepositoryJson
from presentation.add_book_dialog import AddBookDialog
from utils.tkinter_utils import print_hierarchy, get_ceter_window_left_top

MAIN_WIDTH = 800
MAIN_HEIGHT = 600


class AppMainWindow:
    def __init__(self, root, application):
        self.application = application

        root.title("My Library")
        print(f"Windowing system: {root.tk.call('tk', 'windowingsystem')}") # return  x11, win32, aqua
        root.option_add('*tearOff', FALSE) # remove menu tear off ability
        left, top = get_ceter_window_left_top(root, MAIN_WIDTH, MAIN_HEIGHT)
        root.geometry(f"{MAIN_WIDTH}x{MAIN_HEIGHT}+{left}+{top}")
        self.mainframe = ttk.Frame(root, padding="3 3 12 12")
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S) )

        self.menubar = Menu(root)
        root['menu'] = self.menubar

        # File menu
        menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label="File", underline=0)
        menu_file.add_command(label='New', command = self.newFile, underline=0, accelerator="Alt+N")
        self.mainframe.bind("<Alt-N>", self.newFile)
        print(menu_file.entryconfigure(0))
        menu_file.add_command(label="Open ...", command = self.openFile)
        menu_file.add_command(label='Close', command = self.closeFile)
        menu_file.entryconfigure('Close', state=DISABLED)

        # Books menu
        menu_books = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_books, label="Books", underline=0)
        menu_books.add_command(label='New', command=self.onNewBook, underline=0)

    def onNewBook(self):
        self.application.addBook()

    def newFile(self):
        messagebox.showinfo(title="New File Dialog", message="Creating DB file ...")

    def openFile(self):
        messagebox.showinfo(title="File Open Dialog", message="Opening DB file ...")

    def closeFile(self):
        messagebox.showinfo(title="File Close Dialog", message="Closing DB file ...")


