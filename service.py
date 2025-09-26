from models import User, Product, Order, OrderStatus
from repository import OrderRepository

def create_order(user: User, product: Product, quantity: int, repository: OrderRepository):
    order = Order(order_id='order-001', user=user, product=product, quantity=quantity)
    repository.add(order)
    return order


def pay_order(order: Order, user: User, product: Product, repository: OrderRepository):
    # 然后创建订单，让用户购买了五个商品
    repository.pay(order, user, product)
    # 库存和余额扣减应该在 repository.pay 中处理，避免重复扣减
    return order