import json
import xml.etree.ElementTree as ET
from heapq import nlargest


def get_list_json():
    words_list = []
    with open('files/newsafr.json', encoding='utf8') as datafile:
      json_data = json.load(datafile)
      for i in json_data['rss']['channel']['items']:
         g = i['description'].split()
         for a in g:
             if len(a) > 6:
                 words_list.append(a.lower())
    words_list.sort()
    return words_list


def get_list_xml():
    words_list = []
    parser = ET.XMLParser(encoding='cp1251')
    tree = ET.parse('files/newsafr.xml', parser)
    root = tree.getroot()
    xml_items = root.findall("channel/item")
    for xmli in xml_items:
        str = xmli.find("description").text.split()
        for word in str:
            if len(word) > 6:
                words_list.append(word.lower())
    words_list.sort()
    return words_list


def show_top_words(words_list):
    counter = {}
    for word in words_list:
        counter[word] = counter.get(word, 0) + 1
    doubles = {element: count for element, count in counter.items() if count > 1}
    three_largest = nlargest(10, doubles, key=doubles.get)
    return three_largest


if __name__ == '__main__':
    print('ТОП 10 из newsafr.json:', show_top_words(get_list_json()))
    print('ТОП 10 из newsafr.xml:', show_top_words(get_list_xml()))
