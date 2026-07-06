from telethon import TelegramClient
import asyncio
import time
import random
from datetime import datetime
from _thread import start_new_thread
numbers = list(range(3, 149))  # اعداد 3 تا 141
used = []

def get_random_number():
    global numbers, used

    # اگر همه استفاده شدن → ریست
    if not numbers:
        numbers = used.copy()
        used = []
        print("🔄 لیست ریست شد")

    choice = random.choice(numbers)
    numbers.remove(choice)
    used.append(choice)

    return choice

def log(asd):
    jaghilog = open("Prime-003LOG.txt", "a")
    jaghilog.write(f"{asd} \n")
api_id = 34713998
api_hash = "47aed309091a66f137ab71226a0227f1"

# from_chat = -1003225118957
to_chat = "https://t.me/jon_bav1"
source = -1003225118957


# target = "https://t.me/joinchat/tA2WT3W17S5lNGE0"

bot = "@PostBot"
# message_id = 3  

async def main():
    client = TelegramClient("my_account3", api_id, api_hash)
    await client.start()
    while 1:

        await client.send_message(bot, "Create post")
        time.sleep(1)
        await client.send_message(bot, "Not now")
        time.sleep(1)
        msg = await client.get_messages(source, ids=get_random_number())

        if not msg:
            print("not found")
            continue

    
        # if msg.text:
        #     await client.send_message(target, msg.text)
        if msg.media:
            await client.send_file(bot, msg.media, caption=msg.text)
        time.sleep(2)
        # await client.send_message(bot, "🆗 Not needed")
        # time.sleep(2)
        messages = await client.get_messages(bot, limit=2)
        last_msg = messages[0]

        await client.forward_messages(
        entity=to_chat,
        messages=last_msg,
        from_peer=bot
        )
        start_new_thread(log , (f' Posted--> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',))
        print(f' Posted--> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        time.sleep(680)
        

asyncio.run(main())