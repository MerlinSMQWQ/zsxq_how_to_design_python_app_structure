from abc import ABC, abstractmethod
import sqlite3
from models import Order


class AbstractOrderRepository(ABC):

    @abstractmethod
    def add(self, order: Order):
        pass
    
    @abstractmethod
    def cancle(self, order: Order):
        pass

class OrderRepository(AbstractOrderRepository):
    """订单仓库 - 负责订单的数据访问"""

    def __init__(self, db_path: str = 'orders.db'):
        self.db_path = db_path

    def _init_table(self):
        """初始化数据库表结构"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                order_id TEXT PRIMARY KEY,
                user_id TEXT,
                product_id TEXT,
                quantity INTEGER,
                status TEXT,
                created_time TEXT
            )
        ''')
        conn.commit()
        conn.close()

    def add(self, order: Order):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # 插入订单数据
        cursor.execute('''
            INSERT INTO orders (order_id, user_id, product_id, quantity, status, created_time)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            order.order_id,
            order.user.user_id,
            order.product.product_id,
            order.quantity,
            order.status.name,
            order.created_time
        ))

        conn.commit()
        conn.close()
