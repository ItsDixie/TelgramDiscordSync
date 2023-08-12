import disnake
from disnake import SyncWebhook
from telebot.async_telebot import AsyncTeleBot
import asyncio
from telebot import types

with open('token_webhook.txt', 'r') as file:
    token = file.readline().rstrip()
    urlhook = file.readline().rstrip()

webhook = SyncWebhook.from_url(urlhook)
bot = bot = AsyncTeleBot(token)

@bot.channel_post_handler(func=lambda message: True)
async def listen(post : types.Message):
    chat = await bot.get_chat(post.chat.id)
    emb = disnake.Embed(title='Содержание:', description=post.text, color=6591981)
    emb.set_author(name='Новый пост в телеграм канале!', url=chat.invite_link)
    webhook.send(embed=emb)

asyncio.run(bot.polling())
