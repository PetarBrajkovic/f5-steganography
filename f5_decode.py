from PIL import Image
from tkinter import Tk, filedialog

STEP = 3

def f5_decode(encoded_path):
    encoded_image = Image.open(encoded_path).convert('RGB')

    pixels = list(encoded_image.getdata())
    message_length = pixels[0][0]
    decoded_data = ''
    
    for i in range(STEP, message_length * STEP + 1, STEP):
        pixel = pixels[i]
        decoded_data += chr(pixel[0])

    return decoded_data

def choose_image():
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(
        title="Izaberite sliku sa sakrivenim podacima",
        filetypes=[("PNG files", "*.png")]
    )

    if file_path:
        hidden_text = f5_decode(file_path)
        print("Skriveni tekst:", hidden_text)
    else:
        print("Nista nije izabrano")

choose_image()