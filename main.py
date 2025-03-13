import os
import schedule
import time
import requests
import asyncio
import telegram
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()
print("gogogo")

# Настройки GitLab, загружаемые из переменных окружения
GITLAB_URL = os.getenv('GITLAB_URL')
GITLAB_PRIVATE_TOKEN = os.getenv('GITLAB_PRIVATE_TOKEN')

# Настройки Telegram, загружаемые из переменных окружения
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

print(f"GitLab URL: {GITLAB_URL}")
print(f"GitLab Private Token: {GITLAB_PRIVATE_TOKEN}")

# Переменная для отслеживания отправки сообщения
last_notified_mrs = set()

def get_merge_requests():
    # Формируем URL для запроса к API GitLab
    url = f"{GITLAB_URL}/api/v4/merge_requests/?scope=assigned_to_me&state=opened"
    headers = {"Private-Token": GITLAB_PRIVATE_TOKEN}
    response = requests.get(url, headers=headers)

    # Проверяем успешность запроса
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch merge requests: {response.status_code}")

def check_merge_requests():
    # Получаем список MR и фильтруем те, которые не начинаются с 'wip'
    mrs = get_merge_requests()
    mrs_without_wip = [mr for mr in mrs if not mr['title'].lower().startswith('wip')]
    return mrs_without_wip

def send_telegram_message(message):
    print("send_telegram_message")
    # Создаем экземпляр бота и отправляем сообщение в указанный чат
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    asyncio.run(bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message))
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message))
    #loop.close()

def job():
    global last_notified_mrs
    mrs_without_wip = check_merge_requests()
    current_mrs = {mr['iid'] for mr in mrs_without_wip}

    # Найти новые MR, которые еще не были уведомлены
    new_mrs = current_mrs - last_notified_mrs

    if new_mrs:
        message = "Найдены новые MR без статуса WIP:\n"
        print(message)
        for mr in mrs_without_wip:
            if mr['iid'] in new_mrs:
                message += f"- {mr['title']} (#{mr['iid']}) {mr['web_url']}\n"
                print(mr)
        send_telegram_message(message)
        last_notified_mrs.update(new_mrs)

# Запускаем задачу каждую минуту
schedule.every(1).minute.do(job)

if __name__ == "__main__":
    send_telegram_message("gitlab-mr-notificator init")
    while True:
        schedule.run_pending()
        time.sleep(1)
