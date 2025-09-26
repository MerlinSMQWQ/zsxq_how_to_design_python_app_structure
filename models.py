from datetime import datetime
from enum import Enum

class Product:
    def __init__(self, product_id: str, stock: int, price: float|int):
        self.product_id = product_id
        self.stock = stock
        self.price = price


class User:
    def __init__(self, user_id: str, balance: float|int):
        self.user_id = user_id
        self.balance = balance


class OrderStatus(Enum):
    UNPAID = 1
    PAID = 2
    CANCELLED = 3


class Order:
    def __init__(self, order_id: str, user: User, product: Product, quantity: int):
        self.order_id = order_id
        self.user = user
        self.product = product
        self.quantity = quantity
        self.created_time = datetime.now()
        self.status = OrderStatus.UNPAID
        # 不应该在这里处理商品库存，而应该在支付时处理

    def pay(self):
        # 计算一下价格
        self.total = self.product.price * self.quantity
        # 扣除用户余额
        self.user.balance -= self.total
        # 扣除商品库存
        self.product.stock -= self.quantity
        # 修改订单状态
        self.status = OrderStatus.PAID

    def cancel(self):
        self.product.stock += self.quantity
        if self.status == OrderStatus.PAID:
            self.user.balance += self.total
        self.status = OrderStatus.CANCELLED