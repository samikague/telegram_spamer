import os
from dotenv import load_dotenv
from loguru import logger

# Чат куда будет вестись рассылка
chat_id = -1001725160790

"""
Сама рассылка.

text - текст рассылки.
media - фотка/гифка/видос/документ и так далее. Вставлять в виде - путь/к/файлу | https://ссылка.нафайл/ | ID Файла
"""
message = {
    "text": "123123 @GreedyGARANTbot",
    "media": ""
}

def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        logger.success("[ENV] API_ID API_HASH загружены")
    else:
        logger.error("[ENV] Файл .env не найден!")

    api_id = os.getenv("APP_ID")
    api_hash = os.getenv("APP_HASH")

    if not api_id or not api_hash:
        logger.error("[AUTH] APP_ID или APP_HASH не заданы!")
        exit(1)
    return int(api_id), api_hash 