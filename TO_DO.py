import tkinter as tk
DATA_FILE = "tasks.txt"

def load_tasks():
  #  """Loads tasks from the text file into the listbox when the app starts."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            for line in file:
                # strip() removes the newline character (\n) from each line
                listbox.insert(tk.END, line.strip())
def save_tasks():
   # """Overwrites the text file with the current listbox items."""
    with open(DATA_FILE, "w") as file:
        # Get all tasks currently in the listbox
        all_tasks = listbox.get(0, tk.END)
        for task in all_tasks:
            file.write(task + "\n")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0,tk.END)
        save_tasks()
def delet_task():
    listbox.delete(tk.ANCHOR)
    save_tasks()

root = tk.Tk()
root.title("TO-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

listbox = tk.Listbox(root, width=40)
listbox.pack(padx=15, pady=15)

tk.Button(root, text="Add", command=add_task).pack()
tk.Button(root, text="Delete", command=delet_task).pack()
root.mainloop()
