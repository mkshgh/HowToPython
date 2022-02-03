# Dependencies
import xml.etree.ElementTree as ET
import csv
import os

# Input: xml file exported from the vsphere firewall rules
# Output: csv file exported to csv
def vxml2csv(xml_locaion:str):
    # location for output csv
    ouput_csv_location = xml_locaion.split('.')[0]+'.csv'
    # creating a tree of the xml file
    tree = ET.parse(xml_locaion)
    layer3section_index = get_index_of_child_node_by_name(tree.getroot(),'layer3Sections')
    layer3node = tree.getroot()[layer3section_index]
    convert_xml_to_csv(ouput_csv_location,layer3node)
    return os.path.abspath(ouput_csv_location)
    
    
# function to iterate through the xml tree and get the data list of children of the root node
def get_index_of_child_node_by_name(root,children_node_name)->int:  
    for index, child in enumerate(root):
        if child.tag == children_node_name:
            return index
    return None

# function to iterate through the xml tree and get the data list of children of the root node
def get_index_list_of_child_node_by_name(root,children_node_name):
    return [
        index
        for index, child in enumerate(root)
        if child.tag == children_node_name
    ]
    
# function to iterate through the xml tree and get the data list of children of the root node
def get_all_child_nodes_and_index(root):
    return {
        child.tag:index
        for index, child in enumerate(root)   
    }

def childs_into_str(data):
    try:                    
        return str([data[i][0].text for i in range(len(data))])
    except:
        return []

def convert_xml_to_csv(ouput_csv,layer3Sections_xml_node) -> str:
    csv_data = []
    with open(ouput_csv,"w", newline="") as csv_write:
        writer = csv.writer(csv_write)
        writer.writerow(['rule_group','rule_id','rule_name','rule_applied_zones','sources','destinations','ports_n_services','allow_deny','rule_disabled'])
        # start the parsing process here
        for sections in layer3Sections_xml_node:
            for items in sections:
                # skip is the description is encountered, this is just an empty string.
                # This is also the indication the new rule group has started.
                if items.tag != 'description' and items[0].tag != 'action':
                    child_nodes = get_all_child_nodes_and_index(items)
                    # if first is name then it means that the parent node is here
                    rule_group = (sections.get('name'))
                    rule_id = (items.get('id'))
                    rule_disabled = (items.get('disabled'))
                    rule_name = (items[get_index_of_child_node_by_name(items,'name')].text)
                    allow_deny = (items[get_index_of_child_node_by_name(items,'action')].text)

                    # which zones are the rules applied on, sources and destination 
                    # since they three level inside the root node use [][][] multidimensional list
                    # Also we don't know the exact number so we use len which gives us the count of the inner items
                    rule_applied_zones, sources, destinations, ports_n_services = "","","",[]
                    # Statically compare by tag name as some of them might be empty
                    for data in items:
                        if data.tag == 'appliedToList':
                            rule_applied_zones = childs_into_str(data)
                        elif data.tag == 'sources':
                            sources = childs_into_str(data)
                        elif data.tag == 'destinations':
                            destinations = childs_into_str(data)
                        elif data.tag == 'services':
                            for services in data:
                                    
                                if get_index_of_child_node_by_name(services,'destinationPort') != None:
                                    protocol_index = get_index_of_child_node_by_name(services,'protocolName')
                                    destinationPort_index:int = get_index_of_child_node_by_name(services,'destinationPort')
                                    ports_n_services.append(services[protocol_index].text+':'+services[destinationPort_index].text) 
                                    
                                elif get_index_of_child_node_by_name(services,'name') != None:
                                    ports_n_services.append(services[0].text)    
                                
                                else:
                                    print(get_all_child_nodes_and_index(services))
                                    print(services[1].text,services[2].text)              
                                    
                    # source ips are nested in group"
                    csv_data = [rule_group,rule_id,rule_name,rule_applied_zones,sources,destinations,ports_n_services,allow_deny,rule_disabled]
                    writer.writerow(csv_data)
    return(os.path.abspath(ouput_csv))

# enter the xml file name here 
# put the file in the same directory for now
file_path = vxml2csv('firewall.xml')
print(file_path)
