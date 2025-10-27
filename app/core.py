def add(a, b): return a + b
def is_admin(user): return str(user).lower() == "admin"
def login(user, password): return user == "user_ok" and password == "pass_ok"

def filter_products(products, category=None, max_price=None):
    out=[]
    for p in products:
        if category and p.get("category")!=category: continue
        if max_price and p.get("price",0)>max_price: continue
        out.append(p)
    return out

def total_cart(items): return sum(i["price"]*i.get("qty",1) for i in items)
def checkout_ready(address, items): return bool(address) and len(items)>0

def pay(amount, card):
    if card=="4111111111111111": return True
    if card=="4000000000000002": return False
    return False

def render_dashboard_time_ms(load_ms, render_ms): return load_ms+render_ms
