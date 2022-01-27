from tkinter import Tk, ttk, filedialog


class UI:
    "käyttöliittymän rakentava koodi"

    def __init__(self, root):
        self._root = root
        self.filename = None

    def start(self):
        label = ttk.Label(master=self._root, text="Valitse pakattava tiedosto")
        button = ttk.Button(self._root, text='Open', command=self.upload_action)
        label.pack()
        button.pack()

    def upload_action(self, event=None):
        self.filename = filedialog.askopenfilename()