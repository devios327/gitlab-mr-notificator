# GitLab Telegram Notifier

Этот проект представляет собой бота, который проверяет наличие `Merge Requests (MR) без статуса WIP` в `GitLab` и отправляет уведомления в `Telegram`. Бот проверяет MR каждую минуту и отправляет сообщение только один раз для каждого нового MR без статуса WIP.

## Особенности

- Проверка MR каждую минуту.
- Отправка уведомлений в Telegram только для новых MR без статуса WIP.
- Легкая настройка с помощью переменных окружения.

## Требования

- Docker
- Docker Compose

## Установка

1. **Клонируйте репозиторий**:

   ```bash
   git clone <URL вашего репозитория>
   cd <директория проекта>
   ```

2. Создайте файл `.env` в корневой директории проекта на основе `.env.example` и добавьте туда следующие переменные окружения:

```
GITLAB_URL=https://gitlab.example.com
GITLAB_PRIVATE_TOKEN=your_gitlab_private_token
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_telegram_chat_id
```

3. Соберите и запустите Docker-контейнер:

`docker compose up --build --force-recreate`

## Использование

После запуска контейнера бот начнет проверять MR каждую минуту. Если будет найден новый MR без статуса WIP, бот отправит уведомление в указанный чат Telegram.

## Остановка

Чтобы остановить контейнер, выполните команду:

`docker-compose down`

## Описание переменных окружения

```
GITLAB_URL: URL вашего экземпляра GitLab.
GITLAB_PRIVATE_TOKEN: Ваш приватный токен для доступа к GitLab API.
TELEGRAM_BOT_TOKEN: Токен вашего Telegram бота.
TELEGRAM_CHAT_ID: ID чата, куда будут отправляться сообщения.
```
