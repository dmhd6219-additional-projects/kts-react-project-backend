users_db = {}  # { "user1": "password", ... }

user_orders = {}  # { "user1": [order1, order2], ... }


def create_user(username: str, password: str):
    users_db[username] = password
    return username


def authenticate_user(username: str, password: str) -> bool:
    return users_db.get(username) == password


def save_order(user_id: str, order: dict):
    user_orders.setdefault(user_id, []).append(order)


def get_orders(user_id: str):
    return user_orders.get(user_id, [])
