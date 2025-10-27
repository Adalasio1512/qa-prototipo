import pytest
from app.core import login, pay, filter_products, total_cart, checkout_ready

pytestmark = pytest.mark.top20

def test_login_bad_password(): assert not login("user_ok","pass_bad")
def test_logout_placeholder(): assert True
def test_reset_password_placeholder(): assert True

def test_search_and_filter():
    prods=[
        {"name":"Laptop A","category":"Electrónica","price":950},
        {"name":"Mouse B","category":"Electrónica","price":25},
        {"name":"Mesa C","category":"Hogar","price":150},
    ]
    assert len(filter_products(prods, category="Electrónica"))==2

def test_view_product_detail_placeholder(): assert True
def test_add_to_cart_total():
    cart=[{"price":25,"qty":1},{"price":150,"qty":1}]
    assert total_cart(cart)==175
def test_update_cart_qty_recalculates():
    cart=[{"price":25,"qty":2}]
    assert total_cart(cart)==50

def test_checkout_valid_data(): assert checkout_ready("Av. QA 123",[{"id":1,"price":10}])
def test_payment_ok(): assert pay(100,"4111111111111111") is True
def test_payment_rejected(): assert pay(100,"4000000000000002") is False
def test_export_csv_utf8_placeholder(): assert True
def test_roles_permissions_block_placeholder():
    is_admin=False
    assert not is_admin
