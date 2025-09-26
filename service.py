from models import User, Product, Order, OrderStatus
from repository import OrderRepository

def create_order(user: User, product: Product, quantity: int, repository: OrderRepository):
    order = Order(order_id='order-001', user=user, product=product, quantity=quantity)
    repository.add(order)
    print("订单创建成功！")
    return order


def pay_order(order: Order, repository: OrderRepository):
    repository.paid(order)
    print("支付成功！")
    return order

def cancel_order(order: Order, repository: OrderRepository):
    repository.canceled(order)
    print("取消成功！")
    return order