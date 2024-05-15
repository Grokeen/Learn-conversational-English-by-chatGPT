# 202405141120 김용록 바코드 스캔 오픈 소스 (스택오버플로)
from pyzbar.pyzbar import decode
from PIL import Image

def decode_barcode(image_path):
    image = Image.open(image_path)
    
    # 디코드 작업
    barcodes = decode(image)
    
    # 결과 출력
    for barcode in barcodes:
        barcode_info = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        print(f"Decoded {barcode_type} barcode with data: {barcode_info}")

decode_barcode('image/barcode/IMG_7402.jpeg')