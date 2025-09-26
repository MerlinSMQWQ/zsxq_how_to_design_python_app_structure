from models import User, Product, Order, OrderStatus
from repository import OrderRepository

def create_order(user: User, product: Product, quantity: int, repository: OrderRepository):
    order = Order(order_id='order-001', user=user, product=product, quantity=quantity)
    repository.add(order)
    return order


def pay_order(order: Order, user: User, product: Product, repository: OrderRepository):
    repository.paid(order, user, product)
    return order