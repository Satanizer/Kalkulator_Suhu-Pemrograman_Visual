from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, Entry

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"F:\Pemvis\New2\build\assets\frame3")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def on_button_click(input_text, text):
    if text.isdigit() or (text == "." and "." not in input_text.get()):
        input_text.insert("end", text)
    elif text == "delete":
        input_text.delete(len(input_text.get()) - 1, "end")
    elif text == "Ac":
        input_text.delete(0, "end")
    elif text == "konversi Fahrenheit":
        kelvin = float(input_text.get().replace(" K", ""))
        fahrenheit = (kelvin - 273.15) * 9/5 + 32
        input_text.delete(0, "end")
        input_text.insert(0, f"{fahrenheit:.2f}")
        input_text.insert("end", " °F")
    elif text == "konversi Reamur":
        kelvin = float(input_text.get().replace(" K", ""))
        reamur = (kelvin - 273.15) * 4/5
        input_text.delete(0, "end")
        input_text.insert(0, f"{reamur:.2f}")
        input_text.insert("end", " °Ré")
    elif text == "konversi Celcius":
        kelvin = float(input_text.get().replace(" K", ""))
        celcius = kelvin - 273.15
        input_text.delete(0, "end")
        input_text.insert(0, f"{celcius:.2f}")
        input_text.insert("end", " °C")
    elif text == "E":
        input_text.delete(0, "end")
        input_text.insert(0, str(eval(input_text.get())))

def back_to_gui(window):
    window.destroy()  # Menutup jendela saat ini

    # Buka kembali GUI sebelumnya (ganti dengan nama file dan fungsi yang sesuai)
    from gui import main_gui
    main_gui()


def show_kelvin(window):
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

    input_text = Entry(window, font=("Poppins Bold", 48), justify="right", bg="#616161", bd=0)
    input_text.place(x=1600, y=363, anchor="ne", width=420)

    buttons = [
        ("button_1.png", ".", (1018.0, 707.0)),
        ("button_2.png", "delete", (602.0, 544.0)),
        ("button_3.png", "konversi Fahrenheit", (1381.0, 870.0)),
        ("button_4.png", "konversi Reamur", (1382.0, 544.0)),
        ("button_5.png", "konversi Celcius", (1559.0, 542.0)),
        ("button_6.png", "E", (1559.0, 794.0)),
        ("button_7.png", "Ac", (1018.0, 544.0)),
        ("button_8.png", "7", (602.0, 713.0)),
        ("button_9.png", "4", (225.0, 871.0)),
        ("button_10.png", "1", (413.0, 871.31494140625)),
        ("button_11.png", "0", (1020.0, 875.0)),
        ("button_12.png", "2", (602.066650390625, 871.31494140625)),
        ("button_13.png", "3", (789.50341796875, 871.31494140625)),
        ("button_14.png", "5", (227.0, 713.0)),
        ("button_15.png", "6", (416.0, 713.0)),
        ("button_16.png", "8", (790.0, 713.0)),
        ("button_17.png", "9", (227.0, 544.0)),
        ("button_18.png", "back", (47.0, 167.0))
    ]

    # Simpan referensi gambar di dalam list
    button_images = []

    for image_filename, text, position in buttons:
        image_image = PhotoImage(file=relative_to_assets(image_filename))
        button_images.append(image_image)
        if text == "back":
            button = Button(
                image=image_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda: back_to_gui(window),  # Panggil fungsi back_to_gui
                relief="flat"
            )
        else:
            button = Button(
                image=image_image,
                borderwidth=0,
                highlightthickness=0,
                command=lambda t=text: on_button_click(input_text, t),
                relief="flat"
            )
        button.image = image_image
        button.place(x=position[0], y=position[1], width=image_image.width(), height=image_image.height())

    # Simpan referensi gambar sebagai atribut global
    global image_image_1, image_image_2
    image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
    canvas.create_image(960.0, 63.0, image=image_image_2)

    image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
    canvas.create_image(959.0, 204.0, image=image_image_1)

    canvas.create_rectangle(225.0, 292.0, 1702.0, 506.0, fill="#606060", outline="")
