import tkinter as tk
import json

class json_grid_app(tk.Frame):
    def __init__(self, master=None, filename=None):
        super().__init__(master)
        self.master = master
        self.filename = filename
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        # Read in JSON file
        with open(self.filename) as f:
            data = json.load(f)

        # Create labels for each key in the JSON data
        for i, key in enumerate(data.keys()):
            label = tk.Label(self, text=key)
            label.grid(row=i, column=0)

            # Create labels for each value in the JSON data
            for j, value in enumerate(data[key]):
                label = tk.Label(self, text=value)
                label.grid(row=i, column=j+1)

if __name__ == "__main__":
    # Create Tkinter app instance
    root = tk.Tk()
    app = json_grid_app(master=root, filename="data.json")
    app.mainloop()
