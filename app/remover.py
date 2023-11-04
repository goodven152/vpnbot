from pymongo import MongoClient
import time

# Подключение к MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['token_db']
users_collection = db['users']

class UserManager:
    def __init__(self):
        self.delete_users()

    def delete_users(self):
        while True:
            current_time = time.time()
            users = users_collection.find({'delete_at': {'$lt': current_time}})
            for user in users:
                # Код для удаления пользователя или дополнительных действий
                users_collection.delete_one({'_id': user['_id']})
            time.sleep(3600)  # Пауза в 1 час

# Запуск менеджера удаления пользователей
if __name__ == "__main__":
    manager = UserManager()
