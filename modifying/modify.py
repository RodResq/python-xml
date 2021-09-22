import xml.etree.ElementTree as ET

path_xml = '/home/rresq/github/python-xml/country_data.xml'

tree = ET.parse(path_xml)
root = tree.getroot()

# Modificando o valor de um xml e seu criando um atributo de uma tag
for rank in root.iter('rank'):
    new_rank = int(rank.text) + 1
    rank.text = str(new_rank) # alterando o valor
    rank.set('update', 'yes') # setando um atributo

tree.write('output.xml')
