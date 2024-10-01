import xml.etree.ElementTree as ET

def __register_all_namespaces(filename):
    namespaces = dict([node for _, node in ET.iterparse(filename, events=['start-ns'])])
    for ns in namespaces:
        ET.register_namespace(ns, namespaces[ns])
    return namespaces

def __replaceInFile(filename):
    with open(filename, 'r') as file:
        content = file.read()
        content = content.replace(':ns0', '').replace('ns0:', '')
        with open(filename, 'w') as file:
            file.write(content)
    return

def parseXML(xmlfile): 
    namespaces = __register_all_namespaces(xmlfile)
    tree = ET.parse(xmlfile) 
    namespaces[""] = "http://www.imsglobal.org/xsd/imscp_v1p1"
    namespaces["fu"] = "http://www.imsglobal.org/xsd/imscp_v1p1"
  
    root = tree.getroot()

    organization = root.find(".//fu:organization", namespaces)
    
    if organization is not None:
        for child in organization.findall("imsss:sequencing", namespaces):
            organization.remove(child)
            
        items = organization.find("fu:item", namespaces)
        for child in items.findall("fu:metadata", namespaces):
            items.remove(child)

        for child in organization.findall("fu:metadata", namespaces):
            organization.remove(child)
        
        for item in organization.findall("fu:item", namespaces):
            for subchild in item.findall("imsss:sequencing", namespaces):
                item.remove(subchild)
                
    schemaversion = root.find(".//fu:schemaversion", namespaces)
    if schemaversion is not None:
        schemaversion.text = "2004 4th Edition"
    # Datei schreiben
    tree.write(xmlfile)

    __replaceInFile(xmlfile)
    

