import xml.etree.ElementTree as ET

path_xml = '/home/rresq/github/python-xml/country_data.xml'

tree = ET.parse(path_xml)
root = tree.getroot()
# print(f"A raiz do xml e: {root.tag}")
# print(f"Atributo da tag root: {root.attrib}")
# print(f"Acessando um valor de um no elemento: {root[0][1].text}")

# for child in root:
#     print(child.tag, child.attrib)
#     for childreen in child:
#         print(f"Tags dos filhos: tag: {childreen.tag} - atributo(s): {childreen.attrib} - valor: {childreen.text}")

# Iterando sobre um elemento especifico
for neighbor in root.iter('neighbor'):
    print(f"Atributos da uma tag especifica:  Cidade: {neighbor.attrib.get('name')} - Direcao: {neighbor.attrib.get('direction')}")

# Encontrando um tag especifica e extraindo o valor de seus nos filhos
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(f"NomeCidade: {name} - Classificacao: {rank}")
