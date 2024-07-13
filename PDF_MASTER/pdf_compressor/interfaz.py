import flet 
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    Page,
    Column,
    Row,
    Text,
    alignment,
    SnackBar,
    icons,
)
from compressor import comprimir, entrada, directorio_salida

def main(page: Page):
    page.window_width = 800
    page.window_height = 600
    
    # Seleccionar archivos(entrada)
    page.title = "PDF MASTER: Compresor de pdf"
    page.vertical_alignment = flet.MainAxisAlignment.CENTER
    def pick_files_result(e: FilePickerResultEvent):
        selected_files.value = (
            ", ".join(map(lambda f: f.name, e.files)) if e.files else "Cancelado"
        )
        if e.files:
            entrada.clear()
            entrada.extend([f.path for f in e.files])
        selected_files.update()

    pick_files_dialog = FilePicker(on_result=pick_files_result)
    selected_files = Text()

    # Abrir directorio (salida)
    def get_directory_result(e: FilePickerResultEvent):
        directory_path.value = e.path if e.path else "Cancelado"
        if e.path:
            directorio_salida.clear()
            directorio_salida.append(e.path)
        directory_path.update()

    get_directory_dialog = FilePicker(on_result=get_directory_result)
    directory_path = Text()

    #Boton para comprimir archivos
    def on_compress_click(e):
        if entrada and directorio_salida:
            for archivo in entrada:
                comprimir(archivo, directorio_salida[0])
            page.snack_bar = SnackBar(Text("Compresión completada con éxito"))
            page.snack_bar.open = True
            page.update()    
        else:
            print("Por favor seleccione los archivos y el directorio de salida")

    # hide all dialogs in overlay
    page.overlay.extend([pick_files_dialog, get_directory_dialog])

    page.add(
           Column(
            [
                Row(
                    [
                        ElevatedButton(
                            "Seleccionar Archivos",
                            icon=icons.UPLOAD_FILE,
                            on_click=lambda _: pick_files_dialog.pick_files(
                                allow_multiple=True
                            ),
                        ),
                        selected_files,
                    ],
                    alignment="center" # type: ignore
                ),
                Row(
                    [
                        ElevatedButton(
                            "Seleccionar Carpeta",
                            icon=icons.FOLDER_OPEN,
                            on_click=lambda _: get_directory_dialog.get_directory_path(),
                            disabled=page.web,
                        ),
                        directory_path,
                    ],
                    alignment="center" # type: ignore
                ),
                Row(
                    [
                        ElevatedButton(
                            "Comprimir",
                            icon=icons.COMPRESS,
                            on_click=on_compress_click,
                        ),
                    ],
                    alignment="center" # type: ignore
                ),
            ],
            alignment="center", # type: ignore
            horizontal_alignment="center", # type: ignore
            expand=True
        )
    )
flet.app(target=main)