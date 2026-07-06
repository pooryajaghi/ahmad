# from telethon import TelegramClient
# from telethon.network.connection import ConnectionTcpMTProxyAbridged
# import asyncio
# import os
# import time
# import socks
# import random
# mesagge = ["فلیمو عکسامو میفروشم","چنل فیلم بئیومه", "آزاد میخای پیوی", "هعی","کسی فیلم نمیخاد ؟", "حال میدم جوین شو","پایه حالم 🦋🦦 بئیو", "خسته شدم انقدر جق زدم -_-","خیسم بزن بیئو همه دارن میزنن","اوفف", "تصویری حال میدم بزن بئیو"]
# with open("C:\\Users\\Poorya\\OneDrive\\Desktop\\D (3)\\simple-telegram-bot-master\\Poorix - 2026+\\telegramBadGroupData.txt", "r", encoding="utf-8") as f:
#     items = [line.strip() for line in f if line.strip()]
# unused_items = items.copy()

# def get_random_item():
#     global unused_items

#     # اگر همه استفاده شدن → ریست
#     if not unused_items:
#         unused_items = items.copy()
#         print(" rest")

#     choice = random.choice(unused_items)
#     unused_items.remove(choice) 
#     return choice

# #Account Info
# api_id1 = 35406856
# api_hash1 = "9372343928a975540e2269bec088fd49"
# session1 = "my_account"

# # proxy = (socks.SOCKS5, "127.0.0.1", 9909)

# client = TelegramClient(session1, api_id1, api_hash1)
# asd = 0
# async def main():
#     await client.start()
#     while 1 :

        
#         # text = await asyncio.to_thread(input, "> ")
#         await asyncio.sleep(3)
#         choice1 = random.choice(mesagge)
#         await client.send_message(get_random_item(), choice1)
#         asd+=1
#         print(asd)

# asyncio.run(main())
from datetime import datetime
from telethon import TelegramClient, errors
import asyncio
import random
from telethon.tl.types import Message
import time
from _thread import start_new_thread
mesagge = [
    "فلیمو عکسامو میفروشم","چنل فیلم ","آزاد میخای پیوی",
    "هعی","کسی فیلم نمیخاد ؟","حال میدم جوین شو",
    "پایه حالم 🦋🦦 بئیو","خسته شدم انقدر جق زدم -_-",
    "خیسم بزن پروف همه دارن میزنن","اوفف","تصویری حال میدم بزن با اثبات بئیو","پورن کی میخاد",
    "خیس کردم", "جوون  بد داغم","کی بود گفت فیلملمو میخاد" , "کسی کانال پورن با کیفیت نمیخاد؟!"
]
# mesagge = """بیتام فقط حضوریم 
# اول پیش میگیرم بعد بدنمو نشون میدم 
# کرجم 22
# دنبال مفت و کم هزینه ای نیا چون بلاک میشی🚫
# اگه کلفت باشی شاید کمتر بگیرم
# """
with open(
    "C:\\Users\\Poorya\\OneDrive\\Desktop\\D (3)\\simple-telegram-bot-master\\Poorix - 2026+\\telegramBadGroupData.txt",
    "r", encoding="utf-8"
) as f:
    items = [
        int(line.strip()) if line.strip().lstrip("-").isdigit() else line.strip()
        for line in f
        if line.strip()
    ]

unused_items = items.copy()

def get_random_item():
    global unused_items
    if not unused_items:
        unused_items = items.copy()
        print(" rest")
    choice = random.choice(unused_items)
    unused_items.remove(choice)
    return choice

# Account Info
api_id1 = 34713998
api_hash1 = "47aed309091a66f137ab71226a0227f1"
session1 = "my_account2"
delay_r = [30,29,25,44,35,32,33,28,55,53,50]
client = TelegramClient(session1, api_id1, api_hash1)

# شمارنده پیام‌ها
asd = 0
def log(asd):
    jaghilog = open("Prime-AsliLOG.txt", "a")
    jaghilog.write(f"{asd} \n")

async def main():
    global asd
    await client.start()
    print("BOT STARTED ✅")
    start_new_thread(log , ("BOT STARTED",))
    while True:
        if asd == 10:
            asd = 0
            time.sleep(105)
        time.sleep(random.choice(delay_r))  # delay امن بین پیام‌ها
        choice1 = random.choice(mesagge)
        target = get_random_item()
        try:
            msg = await client.send_message(target, choice1)
            # if isinstance(msg, Message):
            #     pass
            # else:
            #     print(f"fail {target}")
            asd += 1
            print(f"[{asd}] Sent to: {target}  ---> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            start_new_thread(log , (f"[{asd}] Sent to: {target}  ---> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",))
        except errors.FloodWaitError as e:
            # اگر FloodWait اومد → صبر می‌کنیم به اندازه seconds که تلگرام گفته
            print(f'Flood wait {e.seconds}s, waiting...   ---> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            start_new_thread(log , (f'Flood wait {e.seconds}s, waiting...   ---> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',))
            await asyncio.sleep(e.seconds)
        except:
            print(f'X faill {target}   ---> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            start_new_thread(log , (f'X faill {target}   ---> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}' ,))

asyncio.run(main())
