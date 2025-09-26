from models import User, Product, Order
from repository import OrderRepository

def create_order(user: User, product: Product, quantity: int, repository: OrderRepository):
    repository._init_table()
    order = Order(order_id='order-001', user=user, product=product, quantity=quantity)
    repository.add(order)
    return order


def pay_order(order: Order, user: User, product: Product, repository: OrderRepository):
    # 然后创建订单，让用户购买了五个商品
    repository.pay(order, user, product)
    return order