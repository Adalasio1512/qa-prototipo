import sys, xml.etree.ElementTree as ET
xml_path = sys.argv[1]; max_flaky_pct = float(sys.argv[2])
root = ET.parse(xml_path).getroot()
fails = int(root.attrib.get("failures","0")) + int(root.attrib.get("errors","0"))
flaky_pct = 0.0 if fails==0 else 100.0
print(f"Flakiness estimada: {flaky_pct}% (umbral {max_flaky_pct}%)")
if flaky_pct > max_flaky_pct: sys.exit(1)
