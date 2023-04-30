import logging
from pyrogram import Client, filters
import random
import config

# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем клиента Pyrogram
Api_id = config.api_id
Api_hash = config.api_hash
#bot_token = 'YOUR_BOT_TOKEN_HERE'
app = Client('my_bot', Api_id, Api_hash)


# обработчик команды /get_users
@app.on_message(filters.command('get_users'))
async def get_users_command_handler(client, message):
    print('l')
    # получаем список всех пользователей в группе
    memebers = []
    group_id = message.chat.id
    async for member in app.get_chat_members(group_id):
        memebers.append(member)
    group_members = memebers
    # создаем список всех имен пользователей
    users = []
    for member in group_members:
        user = member.user
        if user:
            name = user.first_name
            if user.last_name:
                name += f' {user.last_name}'
            users.append(name)

    # отправляем список пользователей обратно в чат
    if users:
        await message.reply(f'Переможець - {random.choice(users)}! 🥳🍾🎁')
    else:
        await message.reply('Пользователей нет')

###
if __name__ == '__main__':
    app.run()