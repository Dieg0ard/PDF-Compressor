from PIL import Image
import io

def comprimirJPEG(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img.save(img_comprimida, optimize=True, format="JPEG", quality=50)
    img_comprimida.seek(0)
    return img_comprimida.getvalue()

def comprimirPNG(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img = img.convert("P", palette=Image.ADAPTIVE, colors=100)  # Reducir colores
    img.save(img_comprimida, format='PNG', optimize=True)
    img_comprimida.seek(0)
    return img_comprimida.getvalue()

def comprimirTIFF(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img.save(img_comprimida, format='TIFF', compress_level=9)
    img_comprimida.seek(0)
    return img_comprimida.getvalue()

def comprimirRAW(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img.save(img_comprimida, optimize=True, format="JPEG", quality=50)
    img_comprimida.seek(0)
    return img_comprimida.getvalue()

def comprimirWEBP(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img.save(img_comprimida, format='WEBP', quality=50)
    img_comprimida.seek(0)
    return img_comprimida.getvalue()

def comprimirBMP(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img.save(img_comprimida, format='BMP')
    img_comprimida.seek(0)
    return img_comprimida.getvalue()

def comprimirGIF(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img.save(img_comprimida, format='GIF', optimize=True)
    img_comprimida.seek(0)
    return img_comprimida.getvalue()






# def comprimirJPEG2000(datos):
#     img = imagecodecs.imread(io.BytesIO(datos))
#     img_comprimida = io.BytesIO()
#     imagecodecs.imwrite(img_comprimida, img, codec='jp2')
#     img_comprimida.seek(0)
#     return img_comprimida.getvalue()