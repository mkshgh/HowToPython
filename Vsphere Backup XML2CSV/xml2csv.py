# Dependencies
import xml.etree.ElementTree as ET
import csv

# Input: xml file exported from the vsphere firewall rules
# Output: csv file exported to csv
def vxml2csv(xml_locaion:str):
    # location for output csv
    ouput_csv = xml_locaion.split('.')[0]+'.csv'

    # creating a tree of the xml file
    tree = ET.parse(xml_locaion)
    # the third node has the index of the config
    # the second node of config has the sections that we want
    # [3][1]
    root = tree.getroot()[3][1]
    # store the data to store in the csv here
    csv_data = []
    
    with open(ouput_csv,"w", newline="") as csv_write:
        writer = csv.writer(csv_write)
        writer.writerow(['rule_group','rule_id','rule_name','rule_applied_zones','sources','destinations','ports_n_services','allow_deny','rule_disabled'])
        # start the parsing process here
        for sections in root:
            for items in sections:
                
                # skip is the description is encountered, this is just an empty string.
                # This is also the indication the new rule group has started.
                if(items.tag=='description'):
                    # print('description encoutered')
                    pass

                # If the rule has no name it starts with the action tag
                # In this case id is at [0]th position instead of the rule name
                elif(items[0].tag=='action'):
                    # print('Default Rule encoutered')
                    pass
                else:
                    # if first is name then it means that the parent node is here
                    rule_group = (sections.get('name'))
                    rule_id = (items.get('id'))
                    rule_disabled = (items.get('disabled'))
                    rule_name = (items[0].text)
                    allow_deny = (items[1].text)
                    
                    # which zones are the rules applied on, sources and destination 
                    # since they three level inside the root node use [][][] multidimensional list
                    # Also we don't know the exact number so we use len which gives us the count of the inner items
                    rule_applied_zones, sources, destinations, ports_n_services = [],[],[],[]
                    # Statically compare by tag name as some of them might be empty
                    print(rule_group)
                    for data in items:
                        if data.tag == 'appliedToList':
                            try:
                                [rule_applied_zones.append(data[i][0].text) for i in range(len(data))]
                            except:
                                pass
                        elif data.tag == 'sources':
                            try:
                                [sources.append(data[i][0].text) for i in range(len(data))]
                            except:
                                pass
                        elif data.tag == 'destinations':
                            try:
                                [destinations.append(data[i][0].text) for i in range(len(data))]
                            except:
                                pass
                        elif data.tag == 'services':
                            for services in data:
                                if services[0].text=='true':
                                    try:
                                        ports_n_services.append(services[3].text+':'+services[1].text)
                                        print(services[1].text+services[2].text+services[3].text)
                                    except:
                                        pass
                                else:
                                    ports_n_services.append(services[0].text)                  
                    # source ips are nested in group"
                    csv_data = [rule_group,rule_id,rule_name,rule_applied_zones,sources,destinations,ports_n_services,allow_deny,rule_disabled]
                    writer.writerow(csv_data)

print('start') 
# enter the xml file name here 
# put the file in the same directory for now
vxml2csv('firewall.xml')
print('finish')
