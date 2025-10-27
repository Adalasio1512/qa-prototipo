import pytest
from app.core import add, is_admin, filter_products, total_cart

@pytest.mark.unit
def test_add(): assert add(2,3)==5

@pytest.mark.unit
def test_is_admin():
    assert is_admin("admin")
    assert not is_admin("guest")

@pytest.mark.unit
def test_filter_products():
    prods=[{"name":"A","category":"X","price":10},{"name":"B","category":"Y","price":50}]
    out=filter_products(prods, category="X", max_price=30)
    assert len(out)==1 and out[0]["name"]=="A"

@pytest.mark.unit
def test_total_cart():
    cart=[{"price":10,"qty":2},{"price":5,"qty":1}]
    assert total_cart(cart)==25
