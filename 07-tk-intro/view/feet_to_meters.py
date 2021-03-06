from tkinter import *
from tkinter import ttk

from controller.calculator_controller import CalculatorController
from view.command.feet_to_meters_command import FeetToMetersCommand
from view.utils.tkinter_utils import print_hierarchy


class FeetToMeters(ttk.Frame):
    def __init__(self, root, controller: CalculatorController):
        super().__init__(root, padding="3 3 12 12")
        self.root = root
        self.controller = controller
        self.feet = StringVar() # View Models (following MVVM architecture)
        self.meters = StringVar() # View Models (following MVVM architecture)
        self.createWidgets()
        print_hierarchy(root)

    def createWidgets(self):
        self.root.title('Feet to Meters Convertor')
        self.grid(column=0, row=0, sticky=(N, W, E, S))

        feet_entry = ttk.Entry(self, width=7, textvariable=self.feet)
        feet_entry.grid(column=1, row=1, columnspan=2, ipadx=15, ipady=15, sticky=(W, E))

        ttk.Label(self, textvariable=self.meters).grid(column=1, row=2, sticky=(W, E))

        # ttk.Button(self, text="Calculate", command=partial(self.calculate, suffix="m")).grid(column=3, row=3, sticky=(W))
        # ttk.Button(self, text="Calculate", command=lambda *args, **kwargs: self.calculate("m", *args, **kwargs))\
        ttk.Button(self, text="Calculate", command=FeetToMetersCommand(self.controller)).grid(column=2, row=3, sticky=(W, N))
        self.bind_all("<Return>", FeetToMetersCommand(self.controller))


        for child in self.winfo_children():
            child.grid_configure(padx=50, pady=10)

        rows, cols = self.grid_size()
        print(rows, cols)
        for row in range(rows):
            self.rowconfigure(row, weight=1, minsize=30, pad=30)
        for col in range(cols):
            self.columnconfigure(col, weight=1, minsize=50, pad=30)

    # def calculate(self, suffix="m"):
    #     try:
    #         self.meters.set(str(self.service.feet_to_meters(self.feet.get())) + suffix)
    #     except ValueError:
    #         self.show_error_dialog()

