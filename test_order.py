from models import Product, User, OrderStatus, Order

def test_order_with_available_stock():
    # 我们创建一个商品 product001，它的库存是 10，价格是 20
    product = Product(product_id = 'product-001', stock = 10, price = 20)
    # 再创建一个用户
    user = User(user_id = 'user-001', balance = 100)
    # 然后创建订单，让用户购买了五个商品
    order = Order(order_id = 'order-001', user = user, product = product, quantity = 5)

    # 最后验证商品的库存是否是5个
    assert product.stock == 5
    # 以及订单的状态是否是未支付，我需要使用一个枚举类来包装订单状态
    assert order.status == OrderStatus.UNPAID


def test_pay_order():
    # 依然是创建和刚才一样的商品用户和订单
    product = Product(product_id = 'product-001', stock = 10, price = 20)
    user = User(user_id = 'user-001', balance = 100)
    order = Order(order_id = 'order-001', user = user, product = product, quantity = 5)

    # 然后用户支付订单
    order.pay()

    # 验证订单是否已支付
    assert order.status == OrderStatus.PAID
    # 验证用户余额是否减少
    assert user.balance == 100 - 5 * 20


def test_cancel_order():
    product = Product(product_id = 'product-001', stock = 10, price = 20)
    user = User(user_id = 'user-001', balance = 100)
    order = Order(order_id = 'order-001', user = user, product = product, quantity = 5)

    order.cancel()

    assert order.status == OrderStatus.CANCELLED
    assert product.stock == 10


def test_cancel_payed_order():
    product = Product(product_id = 'product-001', stock = 10, price = 20)
    user = User(user_id = 'user-001', balance = 100)
    order = Order(order_id = 'order-001', user = user, product = product, quantity = 5)
    order.pay()

    order.cancel()

    assert order.status == OrderStatus.CANCELLED
    assert product.stock == 10
    assert user.balance == 100

