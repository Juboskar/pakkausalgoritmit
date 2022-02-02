"käyttöliittymän rakentava koodi"

from tkinter import ttk, filedialog, StringVar
from services.compressor import Compressor


class UI:
    "Käyttöliittymän rakentava luokka"

    def __init__(self, root, compressor=Compressor()):
        self.compressor = compressor
        self._root = root
        self.filename = StringVar()

    def start(self):
        "Lisää tekstielementit ja napit"
        label1 = ttk.Label(master=self._root, text="Valitse pakattava tiedosto")
        btn1 = ttk.Button(self._root, text='Avaa', command=self.upload_action)
        btn2 = ttk.Button(self._root, text='pakkaa (lempel-ziv)', command=self.compress_lz_action)
        btn3 = ttk.Button(self._root, text='pakkaa (huffman)', command=self.compress_huff_action)
        label2 = ttk.Label(master=self._root, textvariable=self.filename)
        btn4 = ttk.Button(self._root, text='pura (lempel-ziv)')
        btn5 = ttk.Button(self._root, text='pura (huffman)')

        label1.pack()
        btn1.pack()
        label2.pack()
        btn2.pack()
        btn3.pack()
        btn4.pack()
        btn5.pack()

    def upload_action(self):
        "Tallettaa valitun tiedoston nimen"
        self.filename.set(filedialog.askopenfilename())

    def compress_lz_action(self):
        "Antaa valitun tiedoston pakattavaksi Lempel-Ziv algoritmilla"
        self.compressor.compress_file(self.filename.get(), "lz")

    def compress_huff_action(self):
        "Antaa valitun tiedoston pakattavaksi Huffmanin algoritmilla"
        self.compressor.compress_file(self.filename.get(), "huff")
