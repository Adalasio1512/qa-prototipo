import pytest
from app.core import login, checkout_ready, pay, render_dashboard_time_ms

@pytest.mark.unit
def test_login_ok(): 
    assert login("user_ok","pass_ok")

@pytest.mark.unit
def test_login_bad(): 
    assert not login("otro","x")

@pytest.mark.unit
def test_checkout_ready_true(): 
    assert checkout_ready("Av. QA 123", [{"id":1,"price":10}])

@pytest.mark.unit
def test_checkout_ready_false(): 
    assert not checkout_ready("", [])

@pytest.mark.unit
def test_pay_ok(): 
    assert pay(10, "4111111111111111") is True

@pytest.mark.unit
def test_pay_reject(): 
    assert pay(10, "4000000000000002") is False

@pytest.mark.unit
def test_render_dashboard_time_ms():
    assert render_dashboard_time_ms(500,700) == 1200
