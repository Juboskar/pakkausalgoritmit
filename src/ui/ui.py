"""UI building code"""

from tkinter import ttk, filedialog, StringVar
from services.compressor import Compressor


class UI:
    """UI building class"""

    def __init__(self, root, compressor=Compressor()):
        self.compressor = compressor
        self._root = root
        self.filename = StringVar()

    def start(self):
        """Adds buttons and labels"""
        select_file_label = ttk.Label(master=self._root, text="Valitse pakattava tiedosto")
        filename_label = ttk.Label(master=self._root, textvariable=self.filename)
        open_file_btn = ttk.Button(self._root, text='Avaa', command=self.upload_action)

        lz_label = ttk.Label(master=self._root, text="Lempel-Ziv:")
        lz_compress_btn = ttk.Button(self._root, text='pakkaa', command=self.compress_lz_action)
        lz_decompress_btn = ttk.Button(self._root, text='pura', command=self.decompress_lz_action)
        huff_label = ttk.Label(master=self._root, text="Huffman:")
        huff_compress_btn = ttk.Button(self._root, text='pakkaa', command=self.compress_huff_action)
        huff_decompress_btn = ttk.Button(self._root, text='pura',
                                         command=self.decompress_huff_action)

        select_file_label.pack()
        open_file_btn.pack()
        filename_label.pack()
        lz_label.pack()
        lz_compress_btn.pack()
        lz_decompress_btn.pack()
        huff_label.pack()
        huff_compress_btn.pack()
        huff_decompress_btn.pack()

    def upload_action(self):
        """Saves name of selected file"""
        self.filename.set(filedialog.askopenfilename())

    def compress_lz_action(self):
        """Gives selected file to compressor for lempel-ziv compressing"""
        self.compressor.compress_file(self.filename.get(), "lz")

    def compress_huff_action(self):
        """Gives selected file to compressor for huffman compressing"""
        self.compressor.compress_file(self.filename.get(), "huff")

    def decompress_lz_action(self):
        """Gives selected file to compressor for lempel-ziv decompressing"""
        self.compressor.decompress_file(self.filename.get(), "lz")

    def decompress_huff_action(self):
        """Gives selected file to compressor for huffman decompressing"""
        self.compressor.decompress_file(self.filename.get(), "huff")
