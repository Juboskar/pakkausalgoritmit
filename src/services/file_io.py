"lukee ja kirjoittaa tiedostoja"


class FileIO:
    "tiedoston lukemisen ja kirjoittamisen toteuttava luokka"

    def __init__(self):
        pass

    @staticmethod
    def read(*args, **kwargs):
        """saa parametreina tiedoston nimen, lukutyypin ja mahdollisen koodauksen lukee
        ja palauttaa tiedoston sisällön"""
        with open(*args, **kwargs) as rfile:  # pylint: disable=W1514
            return rfile.read()

    @staticmethod
    def write(filename, write_type, data):
        """saa parametreina tiedoston nimen, kirjoitustyypin ja kirjoitettavan datan ja
        kirjoittaa tiedostoon"""
        with open(filename, write_type) as decompressed:  # pylint: disable=W1514
            decompressed.write(data)
