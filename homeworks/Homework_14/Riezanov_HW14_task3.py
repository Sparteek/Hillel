#Task3

import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

xml = "G:/Hillel/homeworks/Homework_14/groups.xml"

def find_incoming_by_group_number(xml, group_number):
    tree = ET.parse(xml)
    root = tree.getroot()

    for group in root.iter('group'):
        number = group.find('number').text
        if number == str(group_number):
            timings = group.find('timingExbytes')

            if timings is not None:
                incoming = timings.find('incoming')
                if incoming is not None:
                    logging.info(f"{group_number} is incoming by {incoming.text}")
                    return incoming.text
                else:
                    logging.info(f"Group {group_number} has no incoming timings")
                    return None
            else:
                logging.info(f"Group {group_number} teg timingExbytes not found")
                return None
    logging.info(f"Group {group_number} not found")
    return None


find_incoming_by_group_number(xml, 0)
find_incoming_by_group_number(xml, 2)
find_incoming_by_group_number(xml, 1)
find_incoming_by_group_number(xml, 99)
