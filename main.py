import asyncio
from loguru import logger
from client import client, get_client_info
from scheduler import scheduler, distr_message


async def main():
    await client.start()
    me = await get_client_info()
    logger.debug(f"\n[INFO] ID Аккаунта: {me['id']}\n"
                 f"[INFO] Инициалы аккаунта: {me['first_name']} {me['last_name']}\n"
                 f"[INFO] Телефон: {me['phone']}\n"
                 f"[INFO] Юзернейм: {me['username']}\n"
                 f"[INFO] Спам: {me['spam']}")
    
    # Здесь изменять интервал рассылки. Вписывать - seconds/minutes/hours=X
    scheduler.add_job(distr_message, 'interval', minutes=60)
    scheduler.start()

    while True:
        await asyncio.Event().wait()

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())