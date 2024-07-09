import os
import pymupdf 
import io
from PIL import Image

def comprimirImagen(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    img.save(img_comprimida, optimize=True, format="JPEG", quality=50)
    img_comprimida.seek(0)
    return img_comprimida.getvalue()

def comprimirPng(datos):
    img = Image.open(io.BytesIO(datos))
    img_comprimida = io.BytesIO()
    #img = img.convert("P", palette=Image.ADAPTIVE, colors=65)
    img.save(img_comprimida,format= 'JPEG', optimize = True)
    img_comprimida.seek(0)
    return comprimirImagen(img_comprimida.getvalue())

def obtener_nombre_salida(archivo_entrada, directorio_salida):
    nombre_base, extension = os.path.splitext(os.path.basename(archivo_entrada))
    nombre_salida = f"{nombre_base}_compressed.pdf"
    contador = 1

    while os.path.exists(os.path.join(directorio_salida, nombre_salida)):
        nombre_salida = f"{nombre_base}_compressed({contador}).pdf"
        contador += 1

    return nombre_salida

def comprimir(entrada, directorio_salida):
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    nombre_salida = obtener_nombre_salida(entrada, directorio_salida)
    archivo_salida = os.path.join(directorio_salida, nombre_salida)

    doc = pymupdf.open(entrada)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        page_images = page.get_images(full=True)

        for img_info in page_images:
            xref = img_info[0]
            img_dict = doc.extract_image(xref)
            data = img_dict["image"]
            ext = img_dict["ext"]
            if ext == "jpg" or ext == "jpeg":
                img_r = comprimirImagen(data)
            elif ext == "png":
                img_r = comprimirPng(data)

            page.replace_image(xref, stream=img_r)

    doc.set_metadata({})
    doc.save(archivo_salida, garbage=4, deflate=True, clean=True)
    doc.close()

# Uso de la función
entrada = "/home/diego/Documentos/Proyectos/Python-Projects/files/Archivos-de-prueba/Matemáticas I. Cálculo dife_ (Z-Library).pdf"
directorio_salida = "/home/diego/Documentos/Proyectos/Python-Projects/files"
comprimir(entrada, directorio_salida)
