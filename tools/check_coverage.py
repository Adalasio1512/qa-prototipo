import sys, xml.etree.ElementTree as ET

def compute_rate(xml_path: str) -> float:
    root = ET.parse(xml_path).getroot()

    # 1) Cobertura clásica (coverage.py) con atributo line-rate
    lr = root.attrib.get("line-rate")
    if lr is not None:
        try:
            return float(lr)
        except ValueError:
            pass

    # 2) Variante con lines-covered / lines-valid en la raíz
    covered = root.attrib.get("lines-covered")
    valid = root.attrib.get("lines-valid")
    if covered is not None and valid is not None:
        try:
            c = float(covered); v = float(valid)
            return 0.0 if v == 0 else c / v
        except ValueError:
            pass

    # 3) Último recurso: sumar líneas con hits desde nodos <line>
    covered = 0
    valid = 0
    # cobertura.xml de coverage.py suele tener <classes>/<class>/<lines>/<line hits="..">
    for line in root.iter("line"):
        valid += 1
        try:
            if int(line.attrib.get("hits", "0")) > 0:
                covered += 1
        except ValueError:
            pass
    return 0.0 if valid == 0 else covered / valid

if __name__ == "__main__":
    xml_path = sys.argv[1]
    threshold = float(sys.argv[2]) / 100.0  # p.ej. 70 -> 0.70
    rate = compute_rate(xml_path)
    pct = round(rate * 100, 2)
    print(f"Cobertura: {pct}% (umbral {threshold*100:.0f}%)")
    if rate < threshold:
        sys.exit(1)
