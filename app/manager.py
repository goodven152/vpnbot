from pymongo import MongoClient
from datetime import datetime
import os
from outline_vpn.outline_vpn import OutlineVPN
from pymongo.mongo_client import MongoClient

TELEGRAM_API_TOKEN = os.environ.get('TELEGRAM_API_TOKEN')
PAYMENT_PROVIDER_TOKEN = os.environ.get('PAYMENT_PROVIDER_TOKEN')
OUTLINE_VPN_CREDENTIAL = os.environ.get('OUTLINE_VPN_CREDENTIAL')
MONGO_INITDB_ROOT_USERNAME = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
MONGO_INITDB_ROOT_PASSWORD = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')


# Параметры подключения к MongoDB
mongo_port = 27017
mongo_username = MONGO_INITDB_ROOT_USERNAME
mongo_password = MONGO_INITDB_ROOT_PASSWORD


# Подключение к MongoDB
client = MongoClient(
    host='outline_database',
    port=mongo_port,
    username=mongo_username,
    password=mongo_password,
)

# Создание или подключение к базе данных
database_name = "vpn_server"
db = client[database_name]

tokens_collection = db['tokens']


class TokenManager:
    def add_token(self, id_user, token, datetime_started, datetime_end, quantity_mb):
        token_data = {
            'id_user': id_user,
            'token': token,
            'datetime_started': datetime_started,
            'datetime_end': datetime_end,
            'quantity_mb': quantity_mb
        }
        tokens_collection.insert_one(token_data)
        print("Токен успешно добавлен.")

    def remove_expired_tokens(self):
        current_datetime = datetime.now()
        tokens_collection.delete_many({'datetime_end': {'$lt': current_datetime}})
        print("Просроченные токены удалены.")

    def get_remaining_mb(self, id_user):
        total_mb = 0
        tokens = tokens_collection.find({'id_user': id_user})
        for token in tokens:
            total_mb += token['quantity_mb']
        return f"У пользователя осталось {total_mb} мегабайт."

    def get_remaining_tokens(self, id_user):
        tokens_count = tokens_collection.count_documents({'id_user': id_user})
        return f"У пользователя осталось {tokens_count} токенов."

    def get_remaining_tokensAll(self, id_user):
        tokens = tokens_collection.find({'id_user': id_user})
        remaining_tokens = []
        total_tokens = 0
        for token in tokens:
            remaining_tokens.append(token['token'])
            total_tokens += 1
        tokens_string = '\n'.join(remaining_tokens)
        return f"У пользователя осталось {total_tokens} токенов:\n{tokens_string}"


# # Пример использования
# manager = TokenManager()

# # # Добавление токена
# id_user = 123
# token = "abcdef123456"
# datetime_started = datetime(2023, 5, 1)
# datetime_end = datetime(2023, 5, 14)
# quantity_mb = 500
# manager.add_token(id_user, token, datetime_started, datetime_end, quantity_mb)

# # Удаление просроченных токенов
# manager.remove_expired_tokens()

# # Получение остатка мегабайт по id пользователя
# remaining_mb = manager.get_remaining_mb(id_user)
# print(remaining_mb)

# # Получение остатка токенов по id пользователя
# remaining_tokens = manager.get_remaining_tokens(id_user)
# print(remaining_tokens)
