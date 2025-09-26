from models import User, Product, Order
from repository import OrderRepository

def create_order(user: User, product: Product, quantity: int, repository: OrderRepository):
    order = Order(order_id='order-001', user=user, product=product, quantity=quantity)
    repository.add(order)
    return order