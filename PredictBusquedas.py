from pathlib import Path
import xml.etree.ElementTree as ET


ruta = Path("datos") / "catalogo.xml"

arbol = ET.parse(ruta)
raiz = arbol.getroot()

print(raiz.tag)

libros = raiz.findall("libro")
print(len(libros))

primer_libro = raiz.find("libro")
print(primer_libro.get("id"))

titulo = primer_libro.findtext("titulo")
print(titulo)

disponibles = raiz.findall(
    ".//libro[@disponible='true']"
)
print(len(disponibles))