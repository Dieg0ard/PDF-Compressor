import os
import pymupdf 
import images as im

def comprimir(entrada, directorio_salida):
    jpeg_extensions = ["jpg", "jpeg"]
    # jpeg2000_extensions = ["jpx", "jp2", "j2k", "jpf"]

    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)

    nombre_salida = obtener_nombre_salida(entrada, directorio_salida)
    archivo_salida = os.path.join(directorio_salida, nombre_salida)

    doc = pymupdf.open(entrada)
    for page_num in range(len(doc)):
        print(page_num)
        page = doc.load_page(page_num)
        page_images = page.get_images(full=True)

        for img_info in page_images:
            xref = img_info[0]
            img_dict = doc.extract_image(xref)
            data = img_dict["image"]
            ext = img_dict["ext"]

            if ext in jpeg_extensions:
                img_r = im.comprimirJPEG(data)
                page.replace_image(xref, stream=img_r)
            elif ext == "png":
                img_r = im.comprimirPNG(data)
                page.replace_image(xref, stream=img_r)
            # elif ext in jpeg2000_extensions:
            #     img_r = im.comprimirJPEG2000(data)
            elif ext == "tif":
                img_r = im.comprimirTIFF(data)
                page.replace_image(xref, stream=img_r)

            

    doc.set_metadata({})
    doc.save(archivo_salida, garbage=4, deflate=True, clean=True)
    doc.close()

def obtener_nombre_salida(archivo_entrada, directorio_salida):
    nombre_base, extension = os.path.splitext(os.path.basename(archivo_entrada))
    nombre_salida = f"{nombre_base}_compressed.pdf"
    contador = 1

    while os.path.exists(os.path.join(directorio_salida, nombre_salida)):
        nombre_salida = f"{nombre_base}_compressed({contador}).pdf"
        contador += 1

    return nombre_salida

# Uso de la función
entrada = "/home/diego/Documentos/Proyectos/Python-Projects/prueba/entradas/m.pdf"
directorio_salida = "/home/diego/Documentos/Proyectos/Python-Projects/prueba/salidas"
comprimir(entrada, directorio_salida)


# Uso de la función
entrada = "/home/diego/Documentos/Proyectos/Python-Projects/files/Archivos-de-prueba/Matemáticas I. Cálculo dife_ (Z-Library).pdf"
directorio_salida = "/home/diego/Documentos/Proyectos/Python-Projects/files"
comprimir(entrada, directorio_salida)
