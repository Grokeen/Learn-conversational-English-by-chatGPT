

from pyzbar.pyzbar import decode
from PIL import Image

def decode_barcode(image_path):
    # Load the image
    image = Image.open(image_path)
    
    # Decode the barcode(s)
    barcodes = decode(image)
    
    # Print the results
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(f"Decoded {barcode_type} barcode with data: {barcode_info}")

# Example usage
decode_barcode('path_to_your_image.jpg')