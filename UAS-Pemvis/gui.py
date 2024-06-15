from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import gui1
import gui2
import gui3
import gui4

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Pemvis\New2\build\assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_celsius():
    gui1.show_celsius(window)

def show_fahrenheit():
    gui2.show_fahrenheit(window)

def show_reamur():
    gui4.show_reamur(window)

def show_kelvin():
    gui3.show_kelvin(window)

window = Tk()

window.geometry("1920x1080")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1080,
    width=1920,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=show_celsius,  # Show Celsius screen
    relief="flat"
)
button_1.place(
    x=164.0,
    y=208.0,
    width=816.0,
    height=132.8164825439453
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=show_fahrenheit,  # Show Fahrenheit screen
    relief="flat"
)
button_2.place(
    x=164.0,
    y=384.79547119140625,
    width=816.0,
    height=132.8164825439453
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    960.0,
    63.0,
    image=image_image_1
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=show_reamur,  # Show Reamur screen
    relief="flat"
)
button_3.place(
    x=164.0,
    y=561.5909423828125,
    width=816.0,
    height=132.8164825439453
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=show_kelvin,  # Show Kelvin screen
    relief="flat"
)
button_4.place(
    x=164.0,
    y=738.3863525390625,
    width=816.0,
    height=132.8164825439453
)

canvas.create_text(
    1108.0,
    208.0,
    anchor="nw",
    text="Aplikasi Konversi Suhu adalah alat digital yang \nmemudahkan konversi suhu antara \nCelcius, Kelvin, Fahrenheit, \ndan Reamur. Dengan antarmuka yang \nuser-friendly, pengguna dapat memasukkan \nnilai suhu dan \nmendapatkan hasil konversi instan. \nBerguna untuk pendidikan, penelitian, \ndan penggunaan sehari-hari, aplikasi ini \nmemastikan akurasi tinggi dan kemudahan penggunaan.",
    fill="#000000",
    font=("Poppins Medium", 32 * -1)
)

canvas.create_text(
    1108.0,
    709.0,
    anchor="nw",
    text="Creator:\nRafi \nIhsan\nYeru",
    fill="#000000",
    font=("Poppins Medium", 32 * -1)
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,  # Exit the application
    relief="flat"
)
button_5.place(
    x=1765.0,
    y=923.0,
    width=78.0,
    height=78.0
)
window.resizable(False, False)
window.mainloop()
