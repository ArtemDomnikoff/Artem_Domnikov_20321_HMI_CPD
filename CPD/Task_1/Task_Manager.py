# https://metanit.com/python/tkinter/4.1.php
import tkinter as tk
from tkinter import ttk
import psutil


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.sort_col = 0
        self.sort_rev = False
        self.title("TSKMNGR")
        self.geometry("600x560")
        self.procs = []

        # Настройка Scrollbar
        self.scrollbar = ttk.Scrollbar(self, orient="vertical")
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        # Создание Treeview
        self.tree = ttk.Treeview(self, columns=("Name", "PID", "CPU", "Memory"), yscrollcommand=self.scrollbar.set,
                                 show="headings")  # yscrollcommand=self.scrollbar.set
        self.tree.heading("Name", text="Name", command=lambda: self.sort(0))
        self.tree.heading("PID", text="PID", command=lambda: self.sort(1))
        self.tree.heading("CPU", text="CPU", command=lambda: self.sort(2))
        self.tree.heading("Memory", text="Memory", command=lambda: self.sort(3))
        self.tree.column("Name", width=300)
        self.tree.column("PID", width=30)
        self.tree.column("CPU", width=50)
        self.tree.column("Memory", width=50)
        self.update()
        self.tree.grid(row=0, column=0, sticky="nsew")

        # Связываем полосу прокрутки с Treeview
        self.scrollbar.config(command=self.tree.yview)  # Метод yview управляет вертикальной прокруткой в Treeview.

        # Кнопка удаления
        self.delete_button = ttk.Button(self, text="Terminate process", command=self.terminate_process)
        self.delete_button.grid(row=1, column=0, columnspan=2, pady=20)
        # Задаем вес столбцов и строк, чтобы Treeview мог растягиваться
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def update(self):
        index = self.tree.index(self.tree.selection())
        self.tree.delete(*self.tree.get_children())
        pids = psutil.pids()
        for pid in pids:
            try:
                p = psutil.Process(pid)
                p.cpu_affinity([])
                self.tree.insert('', tk.END,
                                 values=(p.name(),
                                         p.pid,
                                         p.cpu_percent(0.1),
                                         round(p.memory_percent(), 3),
                                         )
                                 )
            except:
                pass
        self.sort(self.sort_col)
        self.tree.selection_add(self.tree.get_children()[index])
        self.after(2000, self.update)

    def terminate_process(self):
        selected_item = self.tree.selection()[0]
        pid = int(self.tree.set(selected_item, 1))
        p = psutil.Process(pid)
        self.tree.delete(selected_item)
        p.kill()

    def sort(self, col):
        l = [(self.tree.set(k, col), k) for k in self.tree.get_children()]
        l.sort()
        for index, (_, k) in enumerate(l):
            self.tree.move(k, "", index)
        self.tree.heading(col, command=lambda: self.sort(col))
        self.sort_col = col


if __name__ == "__main__":
    app = App()
    app.mainloop()
