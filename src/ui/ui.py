from tkinter import ttk, filedialog, StringVar
import services.compressor as compressor


class UI:
    "käyttöliittymän rakentava koodi"

    def __init__(self, root):
        self._root = root
        self.filename = StringVar()

    def start(self):
        label1 = ttk.Label(master=self._root, text="Valitse pakattava tiedosto")
        button1 = ttk.Button(self._root, text='Avaa', command=self.upload_action)
        button2 = ttk.Button(self._root, text='pakkaa (lempel-ziv)', command=self.compress_lz_action)
        button3 = ttk.Button(self._root, text='pakkaa (huffman)', command=self.compress_huff_action)
        label2 = ttk.Label(master=self._root, textvariable=self.filename)

        label1.pack()
        button1.pack()
        label2.pack()
        button2.pack()
        button3.pack()

    def upload_action(self):
        self.filename.set(filedialog.askopenfilename())

    def compress_lz_action(self):
        compressor.compress_file(self.filename.get(), "lz")

    def compress_huff_action(self):
        compressor.compress_file(self.filename.get(), "huff")
