from client import client
from config import message, chat_id

from loguru import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from telethon.errors import FloodWaitError, ChatWriteForbiddenError, UserBannedInChannelError

scheduler = AsyncIOScheduler()

async def distr_message():
    if message["media"]:
        try:
            client.send_message(entity=chat_id, message=message["text"])

        except FloodWaitError as flood:
            logger.error(f"Ошибка! КД на чат/общий флудвейт {flood.seconds}")
        except Exception as e:
            logger.error(e)
    else:
        try:
            client.send_file(entity=chat_id, file=message["media"], caption=message["text"])

        except ChatWriteForbiddenError as e:
            logger.error("Отсутствует право писать в чат! Возможен мут/бан")
        except UserBannedInChannelError as e:
            logger.error("Вы заблокированы в чате! Остановка.")
            scheduler.shutdown(wait=False)
        except FloodWaitError as flood:
            logger.error(f"Ошибка! КД на чат/общий флудвейт {flood.seconds}")
        except Exception:
            logger.error(e)