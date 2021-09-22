import xml.etree.ElementTree as ET
import re

path_xml = '/home/rresq/github/python-xml/country_data.xml'
regex = re.compile(r'country')

try:
    tree = ET.parse(path_xml)
    root = tree.getroot()
    print(regex.search(root))
except FileNotFoundError:
    print('Arquivo nao encontrado')
else:
    for country in root.findall('country'):
        rank = int(country.find('rank').text)
        if rank > 50:
            root.remove(country)

    tree.write('output.xml')


a = ET.Element('a')
b = ET.SubElement(a, 'b')
c = ET.SubElement(a, 'c')
d = ET.SubElement(c, 'd')
ET.dump(a)
