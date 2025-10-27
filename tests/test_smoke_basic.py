import csv, json, pytest
from app.core import login, checkout_ready, render_dashboard_time_ms

pytestmark = pytest.mark.smoke

def test_login_ok(): assert login("user_ok","pass_ok")
def test_checkout_ready(): assert checkout_ready("Calle 1",[{"id":1,"price":10}])
def test_dashboard_perf_under_2s(): assert render_dashboard_time_ms(800,900) < 2000

def test_fixtures_exist_and_parse():
    with open("fixtures/users_demo.csv", newline="", encoding="utf-8") as f:
        rows=list(csv.DictReader(f))
        assert any(r["username"]=="user_ok" for r in rows)
    with open("fixtures/products_seed.json", encoding="utf-8") as f:
        data=json.load(f)
        assert isinstance(data,list) and len(data)>=1
