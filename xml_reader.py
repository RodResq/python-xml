import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
print(f"A raiz do xml e: {root.tag}")
print(f"Atributo da tag root: {root.attrib}")
