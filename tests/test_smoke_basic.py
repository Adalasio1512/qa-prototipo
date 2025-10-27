import csv, json, pytest
from app.core import login, checkout_ready, render_dashboard_time_ms

pytestmark = pytest.mark.smoke

def test_login_ok():
    assert login("user_ok", "pass_ok")

def test_dashboard_perf_under_2s():
    assert render_dashboard_time_ms(800, 900) < 2000

def test_fixtures_exist_and_parse():
    # Abrimos con utf-8-sig para eliminar BOM si existe
    with open("fixtures/users_demo.csv", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        # Por seguridad, limpiamos posibles \ufeff en los headers
        if reader.fieldnames:
            reader.fieldnames = [h.lstrip("\ufeff") for h in reader.fieldnames]
        rows = list(reader)
    assert any(r.get("username") == "user_ok" for r in rows)

def test_products_seed_parses():
    # También en JSON por si lleva BOM
    with open("fixtures/products_seed.json", encoding="utf-8-sig") as f:
        data = json.load(f)
    assert isinstance(data, list) and len(data) >= 1
