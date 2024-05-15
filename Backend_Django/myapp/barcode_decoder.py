from pyzbar.pyzbar import decode
from PIL import Image

def decode_barcode(image_path):
    image = Image.open(image_path)
    barcodes = decode(image)
    results = []
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        results.append(f"Decoded {barcode_type} barcode with data: {barcode_info}")
    return results