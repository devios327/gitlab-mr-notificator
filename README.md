# GitLab Telegram Notifier

Этот проект представляет собой бота, который проверяет наличие `Merge Requests (MR) без статуса WIP` в `GitLab` и отправляет уведомления в `Telegram`. Бот проверяет MR каждую минуту и отправляет сообщение только один раз для каждого нового MR без статуса WIP.

## Описание переменных окружения

```
GITLAB_URL: URL вашего экземпляра GitLab.
GITLAB_PRIVATE_TOKEN: Ваш приватный токен для доступа к GitLab API.
TELEGRAM_BOT_TOKEN: Токен вашего Telegram бота.
TELEGRAM_CHAT_ID: ID чата, куда будут отправляться сообщения.
```

## Установка

`pip install -r requirements.txt`
