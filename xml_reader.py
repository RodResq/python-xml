import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')
root = tree.getroot()
print(f"A raiz do xml e: {root.tag}")
print(f"Atributo da tag root: {root.attrib}")
print(f"Acessando um valor de um no elemento: {root[0][1].text}")

for child in root:
    print(child.tag, child.attrib)
    for childreen in child:
        print(f"Tags dos filhos: tag: {childreen.tag} - atributo(s): {childreen.attrib} - valor: {childreen.text}")
