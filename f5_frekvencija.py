from PIL import Image
from tkinter import Tk, filedialog 
STEP=3

def get_frequencies(image):
    frequencies = {}
    pixels = list(image.getdata())
    for pixel in pixels:
        key = tuple(pixel)
        frequencies[key] = frequencies.get(key, 0) + 1
    return frequencies
 
def choose_pixel(frequencies, used_pixels):
    sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    for pixel, _ in sorted_frequencies:
        if pixel not in used_pixels:
            return pixel

def f5_decode(encoded_path, message_length,positions):
   
    encoded_image = Image.open(encoded_path)
    pixels = list(encoded_image.getdata())
    decoded_data = ''
    for i in positions:
        pixel=pixels[i]
        decoded_data+=chr(pixel[0])   
    return decoded_data

def f5_encode(carrier_path, data_to_hide, output_path):
 carrier = Image.open(carrier_path)
 binary_data =[ord(char) for char in data_to_hide]
 pixels = list(carrier.getdata())
 used_pixels = set()
 new_image = Image.new('RGB', (carrier.width, carrier.height))
 positions =list()
 for i in range(len(binary_data)):
        pixel = choose_pixel(get_frequencies(carrier), used_pixels)
        used_pixels.add(pixel)
        position = pixels.index(pixel)
        positions.append(position)
        pixel = list(pixel)       
        pixel[0] = binary_data[i]
        pixels[position]=tuple(pixel)
 new_image.putdata(pixels)
 new_image.save(output_path)
 return positions

def choose_image():
   root= Tk()
   root.withdraw()
   carrier_path=filedialog.askopenfilename(title="Izaberite sliku", filetypes=[("Slike","*.png")])
   output_path = input("Unesite naziv slike sa sakrivenim podacima:")
   if carrier_path:
      print("Izabrana slika:",carrier_path)
      data_to_hide=input("Unesite tekst koji zelite da sakrijete:")
      positions=f5_encode(carrier_path, data_to_hide, output_path)
      print(f5_decode(output_path,  len(data_to_hide),positions))

choose_image()
