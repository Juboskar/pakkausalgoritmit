"Sovelluksen käynnistävä koodi"
from tkinter import Tk
from ui.ui import UI


def main():
    "Käyttöliittymän käynnistävä funktio"
    window = Tk()
    window.title('Pakkaamo')
    ui = UI(window)
    ui.start()
    window.mainloop()


if __name__ == "__main__":
    main()
