# Используйте базовый образ Python
FROM python:3.9

# Установим переменные среды
ENV TELEGRAM_API_TOKEN=${TELEGRAM_API_TOKEN}
ENV PAYMENT_PROVIDER_TOKEN=${PAYMENT_PROVIDER_TOKEN}
ENV OUTLINE_VPN_CREDENTIAL=${OUTLINE_VPN_CREDENTIAL}
ENV MONGO_INITDB_ROOT_USERNAME=${MONGO_INITDB_ROOT_USERNAME}
ENV MONGO_INITDB_ROOT_PASSWORD=${MONGO_INITDB_ROOT_PASSWORD}

WORKDIR /app

# Установим зависимости
RUN pip install python_telegram_bot==20.1 pexpect~=4.8.0 pymongo outline-vpn-api


CMD [ "python", "bot.py"]