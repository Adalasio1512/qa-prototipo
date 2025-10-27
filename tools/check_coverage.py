import sys, xml.etree.ElementTree as ET
xml_path = sys.argv[1]; threshold = float(sys.argv[2])/100.0
line_rate = float(ET.parse(xml_path).getroot().attrib.get("line-rate","0"))
pct = round(line_rate*100,2)
print(f"Cobertura: {pct}% (umbral {threshold*100}%)")
if line_rate < threshold: sys.exit(1)
