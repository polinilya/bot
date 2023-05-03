from javascript import require, On, AsyncTask
from time import sleep

minefalyer = require('mineflayer')
isFishing = False

# для запуска на локальный мир в значение port указать ваш порт
# для запуска на сервер удалить ключ port и в host записать ip сервера

bot = minefalyer.createBot({
    'host': '12347qfb.aternos.me',
    'username': 'Observer',
    'version': '1.19.3'
})


@On(bot._client, 'sound_effect')
def sound_handler(this, packet, *args):
    global isFishing
    if isFishing == True:
        soundId = packet
        if soundId['soundId'] == 272:
            bot.activateItem()
            isFishing = False


@On(bot, 'spawn')
def spawn(*args):
    bot.chat(bot.username)


@On(bot, 'chat')
def msgHandler(this, user, message, *args):
    print(message)
    if message == 'fish':
        bot.equip(bot.registry.itemsByName.fishing_rod.id, 'hand')

        @AsyncTask(start=True)
        def fishing(task):
            global isFishing
            while True:
                if isFishing == False:
                    sleep(1)
                    bot.activateItem()
                    isFishing = True
