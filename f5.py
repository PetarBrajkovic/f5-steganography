from PIL import Image
from tkinter import Tk, filedialog
STEP=3
def choose_image():
   root= Tk()
   root.withdraw()

   carrier_path=filedialog.askopenfilename(title="Izaberite sliku", filetypes=[("PNG files", "*.png")])
   output_path = input("Unesite naziv slike sa sakrivenim podacima (sa ekstenzijom na kraju): ")

   if carrier_path:
      print("Izabrana slika:",carrier_path)
      data_to_hide=input("Unesite tekst koji zelite da sakrijete:")
      f5_encode(carrier_path, data_to_hide, output_path)
      print(f5_decode(output_path,  len(data_to_hide)))
  

def f5_encode(carrier_path, data_to_hide, output_path):
 carrier = Image.open(carrier_path).convert('RGB')
 binary_data = [len(data_to_hide)] + [ord(char) for char in data_to_hide]
 pixels = list(carrier.getdata())
 positions = list(range(0, len(pixels), STEP))[:len(binary_data)]

 for i, position in enumerate(positions):
    pixel = list(pixels[position])
    pixel[0] = binary_data[i]
    pixels[position] = tuple(pixel)
    
 new_image = Image.new('RGB', (carrier.width, carrier.height))
 new_image.putdata(pixels)
 new_image.save(output_path)
 
def f5_decode(encoded_path, message_length):
    encoded_image = Image.open(encoded_path)
    pixels = list(encoded_image.getdata())
    decoded_data = ''
    pixel=pixels[0]
    message_length = pixel[0]
    for i in range(STEP, message_length*STEP+1,STEP):
        pixel=pixels[i]
        decoded_data+=chr(pixel[0])   
    return decoded_data
 
# Primer korišćenja
choose_image()
