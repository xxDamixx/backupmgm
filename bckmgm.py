#Autor: Damian Popławski



import tkinter as tk
from tkinter import filedialog
import shutil
import schedule

class Backup:
    def __init__(self, master):
        self.master = master
        master.title("Backup")

        self.source_label = tk.Label(master, text="Wybierz plik lub katalog, który chcesz skopiować:")
        self.source_label.pack()

        self.source_button = tk.Button(master, text="Wybierz plik", command=self.choose_file)
        self.source_button.pack()

        self.dest_label = tk.Label(master, text="Wybierz miejsce, gdzie chcesz zapisać kopię:")
        self.dest_label.pack()

        self.dest_button = tk.Button(master, text="Wybierz katalog", command=self.choose_directory)
        self.dest_button.pack()

        self.time_label = tk.Label(master, text="Wybierz godzinę, o której ma zostać wykonana kopia:")
        self.time_label.pack()

        self.time_entry = tk.Entry(master)
        self.time_entry.pack()

        self.backup_button = tk.Button(master, text="Wykonaj kopię", command=self.backup)
        self.backup_button.pack()

        self.schedule_button = tk.Button(master, text="Zaplanuj kopię zapasową", command=self.start_schedule)
        self.schedule_button.pack()

    def choose_file(self):
        self.source_path = filedialog.askopenfilename()
        self.source_label.config(text=f"Wybrany plik/katalog: {self.source_path}")

    def choose_directory(self):
        self.dest_path = filedialog.askdirectory()
        self.dest_label.config(text=f"Wybrany katalog: {self.dest_path}")

    def backup(self):
        try:
            shutil.copy(self.source_path, self.dest_path)
            print("Kopia zapasowa wykonana!")
        except FileNotFoundError:
            print("Nie wybrano pliku/katalogu do skopiowania!")
        except AttributeError:
            print("Nie wybrano katalogu, gdzie ma być zapisana kopia!")
        except:
            print("Wystąpił nieznany błąd!")

    def schedule_backup(self):
        schedule.every().day.at(self.time_entry.get()).do(self.backup)
        while True:
            schedule.run_pending()

    def start_schedule(self):
        self.backup_button.config(state="disabled")
        self.source_button.config(state="disabled")
        self.dest_button.config(state="disabled")
        self.time_entry.config(state="disabled")
        self.schedule_backup()

root = tk.Tk()
my_gui = Backup(root)
root.mainloop()
