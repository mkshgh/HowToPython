# XML2CSV V1.0

To automate the process of coverting the vsphere firewall backup into usable csv data.

## Basic Working
It uses xmlutil to traverse through the data and provides scrapes the useful data that you need. You can modify the code and create an custom view of the data for your project
```

Input: xml backup of firewall with unnecessary data
Output: rule_group,rule_id,rule_name,rule_applied_zones,sources,destinations,ports_n_services,allow_deny

```

## Overview

- Basic Logging Feature to test your automation
- Automated Login/Logout Feature

## Mockup

preview of the exported data

![Packtoo](/img/data_preview.png)

## Libraries

- [xmlutil](https://docs.python.org/3/library/xml.etree.elementtree.html#module-xml.etree.ElementTree)
- csv

## Use case

Run the script

```
# Run the script
PS C:\Users\Mukesh\Desktop\xml2csvPython> python xml2csv.py
start
finish

```

where to change the file name
```
# change the file name accordingly
# enter the xml file name here 
# put the file in the same directory for now
vxml2csv('your_xml_file_here')

```

## Future Improvements

- A lot to be done.
- Boom Boom Boom, Let it explode :)