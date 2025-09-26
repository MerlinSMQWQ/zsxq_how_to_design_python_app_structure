from models import Product, User, OrderStatus, Order
from service import create_order, pay_order, cancel_order
from repository import OrderRepository

def test_creat_order():
    # 我们创建一个商品 product001，它的库存是 10，价格是 20
    product = Product(product_id = 'product-001', stock = 10, price = 20)
    # 再创建一个用户
    user = User(user_id = 'user-001', balance = 100)
    # 然后创建订单，让用户购买了五个商品
    order = create_order(user=user, product=product, quantity=5, repository=OrderRepository())

    assert order.status == OrderStatus.UNPAID
    return order

def test_order_with_available_stock():
    # 我们创建一个商品 product001，它的库存是 10，价格是 20
    product = Product(product_id = 'product-001', stock = 10, price = 20)
    # 再创建一个用户
    user = User(user_id = 'user-001', balance = 100)
    order = Order(order_id = 'order-001', user = user, product = product, quantity = 5)
    pay_order(order, user, product, OrderRepository())
    assert order.status == OrderStatus.PAID
    assert user.balance == 0
    assert product.stock == 5
    return order

def test_cancel_order_1():
    order = test_order_with_available_stock()
    order = cancel_order(order, OrderRepository())
    assert order.status == OrderStatus.CANCELLED
    assert order.user.balance == 100
    assert order.product.stock == 10

def test_cancel_order_2():
    order = test_order_with_available_stock()
    order = cancel_order(order, OrderRepository())
    assert cancel_order(order, OrderRepository()) == order
    assert order.status == OrderStatus.CANCELLED
    assert order.user.balance == 100
    assert order.product.stock == 10
    