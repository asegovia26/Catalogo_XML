from pathlib import Path
import xml.etree.ElementTree as ET


def main():
    # Rutas de entrada y salida
    ruta_entrada = Path("datos") / "catalogo.xml"
    if not ruta_entrada.exists():
        ruta_entrada = Path("catalogo.xml")

    ruta_salida = Path("datos") / "salida" / "catalogo_actualizado.xml"
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)

    # Cargar y parsear el documento XML
    arbol = ET.parse(ruta_entrada)
    raiz = arbol.getroot()

    # ==========================================
    # PREGUNTA 4: Añadir y modificar información
    # ==========================================

    # Apartado A: Añadir nuevo libro (L004)
    nuevo_libro = ET.SubElement(raiz, "libro", id="L004", disponible="true")

    sub_titulo = ET.SubElement(nuevo_libro, "titulo")
    sub_titulo.text = "Persistencia con Python"

    sub_autor = ET.SubElement(nuevo_libro, "autor")
    sub_autor.text = "Carlos Gómez"

    sub_precio = ET.SubElement(nuevo_libro, "precio", moneda="EUR")
    sub_precio.text = "31.75"

    sub_stock = ET.SubElement(nuevo_libro, "stock")
    sub_stock.text = "6"

    print("Libro L004 añadido correctamente.")

    # Apartado B: Modificar libro L001
    libro_l001 = raiz.find(".//libro[@id='L001']")
    if libro_l001 is not None:
        libro_l001.set("disponible", "false")
        precio_l001 = libro_l001.find("precio")
        if precio_l001 is not None:
            precio_l001.text = "24.95"
            precio_l001.set("oferta", "true")
        print("Libro L001 modificado (disponible='false', precio=24.95, oferta='true').")

    # ===================================================
    # PREGUNTA 5: Eliminar, guardar y comparar formatos
    # ===================================================

    # Apartado A: Eliminar libros cuyo stock sea igual a cero
    libros_eliminados = []
    for libro in list(raiz.findall("libro")):
        stock_elem = libro.find("stock")
        if stock_elem is not None and stock_elem.text is not None:
            if int(stock_elem.text.strip()) == 0:
                libros_eliminados.append(libro.get("id"))
                raiz.remove(libro)

    print(f"Libros eliminados por stock 0: {libros_eliminados}")

    # Apartado B: Guardar resultado en /datos/salida/catalogo_actualizado.xml
    ET.indent(arbol, space="    ")
    arbol.write(ruta_salida, encoding="utf-8", xml_declaration=True)
    print(f"Catálogo actualizado guardado exitosamente en: {ruta_salida}")


if __name__ == "__main__":
    main()
