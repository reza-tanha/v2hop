from aiohttp_socks import ProxyType, ProxyConnector
from datetime import datetime
from aiohttp import ClientSession
import asyncio
import aiosqlite
import os
import environ


db_name = "db.sqlite3"
environ.Env.read_env('.env')
TOKEN = os.environ.get('TOKEN')
proxy_ip, proxy_port = os.environ.get('PROXY_SOCKS').split(":")

async def get_users():
    """Get all users from db where ads msg is not sent"""
    async with aiosqlite.connect(db_name) as db:
        cursor = await db.cursor()
        #query = "SELECT user_id FROM account_user WHERE is_superuser=1"
        query = "SELECT user_id FROM account_user WHERE is_sent_ads=0"
        await cursor.execute(query,)
        all_users = await cursor.fetchall()
        return all_users


async def update_ads(chat_id: int):
    """Update the ads status for user"""
    async with aiosqlite.connect(db_name) as db:
        try:
            cursor = await db.cursor()
            time_now = datetime.now()
            query = f"UPDATE account_user SET is_sent_ads=1, sent_ads_time='{time_now}' WHERE user_id={chat_id}"
            await cursor.execute(query)
            await db.commit()
            all_users = await cursor.fetchall()
            return all_users
        except Exception as err:
            print(err)
            await db.rollback()


async def send_copy_message(user, chat_id: int, message_id: int, semaphore: object):
    """Send message to user"""
    send_msg_url = f"https://api.telegram.org/bot{TOKEN}/copyMessage"
    connector = ProxyConnector(
        proxy_type=ProxyType.SOCKS5,
        host=proxy_ip,
        port=proxy_port,
        rdns=True
    )
    async with ClientSession(connector=connector) as session:
        async with semaphore:
            data = {
                "chat_id": user,
                "from_chat_id": chat_id,
                "message_id": message_id
            }
            try:
                async with session.get(send_msg_url, timeout=20, params=data) as response:
                    json = await response.json()
                    if json['ok']:
                        await update_ads(user)
                        print(f"Send msg: {message_id} to user: {user}")
            except Exception as err:
                print("error, ", err)


async def main(from_chat_id: int, message_id: int):
    semaphore = asyncio.Semaphore(10)
    users = await get_users()
    tasks = []
    for user in users:
        tasks.append(
            asyncio.create_task(
                send_copy_message(
                    user[0],
                    from_chat_id,
                    message_id,
                    semaphore
                )
            )
        )
    await asyncio.wait(tasks)


from_chat_id = int(input("from_chat_id >: "))
message_id = int(input("message_id >: "))
asyncio.run(main(from_chat_id, message_id))