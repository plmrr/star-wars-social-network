import json
import networkx as nx


def get_data(path):
    with open(path, 'r') as file:
        data = json.load(file)

    names = []
    for node in data['nodes']:
        names.append(node['name'])

    edges = []
    for link in data['links']:
        edges.append([names[link['source']], names[link['target']], link['value']])

    return names, edges


def get_names(first, names_list):
    names = []
    for name in first:
        names.append(name)

    for element in names_list:
        for name in element:
            if name not in names:
                if name == 'GOLD FIVE':
                    pass
                else:
                    names.append(name)
            else:
                continue
    return names


def get_rest_data():
    with open('data/sw.json', 'r') as file:
        data = json.load(file)

    names_ = []
    for node in data['nodes']:
        names_.append(node['name'])

    edges = []
    for link in data['links']:
        edges.append([names_[link['source']], names_[link['target']], link['value']])
    return edges


def character_die(graph):
    d1 = ['QUI-GON', 'TC-14', 'DOFINE', 'TEY HOW', 'DARTH MAUL']
    d2 = ['SHMI', 'JANGO FETT', 'CLIEGG']
    d3 = ['NUTE GUNRAY', 'RUNE', 'TARPALS', 'PADME', 'MACE WINDU', 'KI-ADI-MUNDI', 'COUNT DOOKU', 'POGGLE', 'PLO KOON',
          'GENERAL GRIEVOUS', 'CLONE COMMANDER GREE']
    d4 = ['OBI-WAN', 'GREEDO', 'BAIL ORGANA', 'OWEN', 'BERU', 'CAPTAIN ANTILLES', 'BIGGS', 'MOTTI', 'TARKIN',
          'GOLD LEADER',
          'RED LEADER', 'RED TEN']
    d5 = ['JABBA', 'ZEV', 'OZZEL', 'DACK', 'NEEDA']
    d6 = ['EMPEROR', 'ANAKIN', 'YODA', 'BOBA FETT', 'DARTH VADER', 'PIETT', 'JERJERROD']
    d7 = ['HAN', 'LOR SAN TEKKA', 'ELLO ASTY']

    if graph.has_node('BRAVO THREE'):
        try:
            for name in d1:
                graph.remove_node(name)
        except nx.NetworkXError:
            pass
    if graph.has_node('PLO KOON'):
        try:
            for name in d2:
                graph.remove_node(name)
        except nx.NetworkXError:
            pass
    if graph.has_node('DARTH VADER'):
        try:
            for name in d3:
                graph.remove_node(name)
        except nx.NetworkXError:
            pass
    if graph.has_node('RED TEN'):
        try:
            for name in d4:
                graph.remove_node(name)
        except nx.NetworkXError:
            pass
    if graph.has_node('LANDO'):
        try:
            for name in d5:
                graph.remove_node(name)
        except nx.NetworkXError:
            pass
    if graph.has_node('ADMIRAL ACKBAR'):
        try:
            for name in d6:
                graph.remove_node(name)
        except nx.NetworkXError:
            pass
    if graph.has_node('NIV LEK'):
        try:
            for name in d7:
                graph.remove_node(name)
        except nx.NetworkXError:
            pass


def main():
    names1, edges1 = get_data('data/ep1.json')
    names2, edges2 = get_data('data/ep2.json')
    names3, edges3 = get_data('data/ep3.json')
    names4, edges4 = get_data('data/ep4.json')
    names5, edges5 = get_data('data/ep5.json')
    names6, edges6 = get_data('data/ep6.json')
    names7, edges7 = get_data('data/ep7.json')
    all_names = [names2, names3, names4, names5, names6, names7]
    names = get_names(names1, all_names)
    edges = get_rest_data()
    return names, edges



