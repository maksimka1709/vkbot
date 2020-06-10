import vk_api.vk_api
import requests
import vk_api
import json
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.bot_longpoll import VkBotEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

token = "70110deaffab97811118fd1f63cd74cd93883ec647eced87e643786bc5abddb9191db8dce90ea5cb7c25b"
vk_session = VkApi(token="70110deaffab97811118fd1f63cd74cd93883ec647eced87e643786bc5abddb9191db8dce90ea5cb7c25b")
longpoll = VkBotLongPoll(vk_session, 122549424)
vk = vk_session.get_api()

def bdcheck():
    data = json.load(open('/home/Maksimka17017/players.json'))
    if 'action' in event.object.message:
        if str(chat_id) in data:
            if str(event.type_id['info'] in data[str(chat_id)]:
                pass
            else:
                data[str(chat_id)][str(event.object.message['action']['member_id'])] = {
                    "user_id": event.object.message['action']['member_id'],
                    "member": "true",
                    "is_admin": "false",
                    "reports": "0",
                    "is_developer": "false",
                    "is_specadm": "false",
                    "warn": 0,
                    "ban": "false",
                    "ban_reason": "None",
                    "ban_by": "None"}
                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
        else:
            data5 = json.load(open('/home/Maksimka17017/players.json'))
            data5[str(chat_id)] = {}
            data5[str(chat_id)]['filter'] = {}
            data5[str(chat_id)]['rules'] = {}
            data5[str(chat_id)][str(user_id)] = {
                "user_id": str(user_id),
                "member": "true",
                "is_admin": "false",
                "reports": "0",
                "is_developer": "false",
                "is_specadm": "false",
                "warn": 0,
                "ban": "false",
                "ban_reason": "None",
                "ban_by": "None"}
            with open('/home/Maksimka17017/players.json', 'w') as outfile:
                json.dump(data5, outfile, indent=4)
    else:
        if str(chat_id) in data:
            if str(user_id) in data[str(chat_id)]:
                pass
            else:
                data[str(chat_id)][str(user_id)] = {
                    "user_id": str(user_id),
                    "member": "true",
                    "is_admin": "false",
                    "reports": "0",
                    "is_developer": "false",
                    "is_specadm": "false",
                    "warn": 0,
                    "ban": "false",
                    "ban_reason": "None",
                    "ban_by": "None"}
                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                    json.dump(data, outfile, indent=4)
        else:
            data4 = json.load(open('/home/Maksimka17017/players.json'))
            data4[str(chat_id)] = {}
            data4[str(chat_id)]['rules'] = {}
            data4[str(chat_id)][str(user_id)] = {
                "user_id": str(user_id),
                "member": "true",
                "is_admin": "false",
                "reports": "0",
                "is_developer": "false",
                "is_specadm": "false",
                "warn": 0,
                "ban": "false",
                "ban_reason": "None",
                "ban_by": "None"}
            with open('/home/Maksimka17017/players.json', 'w') as outfile:
                json.dump(data4, outfile, indent=4)

def bdcheck1():
    data_2 = vk.messages.getConversationMembers(peer_id=peer_id)['items']
    for item in data_2:
        if "is_owner" in item:
            data_1 = json.load(open('/home/Maksimka17017/players.json'))
            if str(user_id) == str(item['member_id']):
                if data_1[str(chat_id)][str(item['member_id'])]['is_specadm'] == "true":
                    vk.messages.send(chat_id=chat_id,
                        message='Вы уже зарегистрировались как основатель беседы.',
                        random_id=get_random_id())
                else:
                    data_1[str(chat_id)][str(item['member_id'])]['is_specadm'] = "true"
                    vk.messages.send(chat_id=chat_id,
                                        message='Вы зарегистрировались как основатель беседы. Доступ выдан.',
                                         random_id=get_random_id())
                    with open('/home/Maksimka17017/players.json', 'w') as outfile:
                            json.dump(data_1, outfile, indent=4)
                    data_5 = json.load(open('/home/Maksimka17017/players.json'))
                    l = []
                    for item in data_2:
                            if "member_id" in item:
                                l.append(item['member_id'])
                                for item in l:
                                    data_3 = str(item)
                                    data_5[str(chat_id)][data_3] = {
                                        "invite_by_user_id": str(user_id),
                                        "member": "true",
                                        "is_admin": "false",
                                        "reports": "0",
                                        "is_developer": "false",
                                        "is_specadm": "false",
                                        "nickname": "Пользователь",
                                        "messages": 0,
                                        "warn": 0,
                                        "ban": "false",
                                        "ban_reason": "None",
                                        "ban_by": "None"}
                                    with open('/home/Maksimka17017/players.json', 'w') as file:
                                        json.dump(data_5, file, indent=4)
                                    return True
                            else:
                                vk.messages.send(chat_id=chat_id,
                                                    message='Вы не являетесь основателем беседы.',
                                                    random_id=get_random_id())
while 1==1:
    try:
        for event in longpoll.listen():
            try:
                self_message = event.object.message['text']
                user_id = (event.object.message['from_id'])
                chat_id = int(event.object.message['peer_id']) - 2000000000
                data = json.load(open('/home/Maksimka17017/players.json'))
                peer_id = event.object.message['peer_id']
                print(event.type_id['info'])
            except TypeError:
                pass

            if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
                if (self_message[0:5] == '/kick' or self_message[0:5] == '!kick' or self_message[0:5] == '+kick') and (
                        data[str(chat_id)][str(user_id)]['is_admin'] == 'true' or data[str(chat_id)][str(user_id)][
                    'is_specadm'] == 'true'):
                    try:
                        self_message = event.object.message['text']
                        if "reply_message" in event.object.message:
                            data = json.load(open('/home/Maksimka17017/players.json'))
                            id1 = event.object.message['reply_message']['from_id']
                            if data[str(chat_id)][str(id1)]['is_admin'] != "true" and data[str(chat_id)][str(id1)][
                                'is_specadm'] != "true":
                                vk.messages.removeChatUser(chat_id=chat_id, user_id=int(id1))
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='kick: ok',
                                    random_id=get_random_id()
                                )
                            else:
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Вы не можете кикнуть администратора',
                                    random_id=get_random_id()
                                )
                        else:
                            id = self_message[9:self_message.index("|")]
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            data1 = json.load(open('/home/Maksimka17017/players.json'))
                            if data1[str(chat_id)][str(id)]['is_admin'] != 'true' and data1[str(chat_id)][str(id)][
                                'is_specadm'] != "true":
                                user_data = vk.users.get(user_ids=id, access_token=token)
                                vk.messages.removeChatUser(chat_id=chat_id, user_id=user_data[0]["id"])
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='kick: ok',
                                    random_id=get_random_id()
                                )
                            else:
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Вы не можете кикнуть администратора',
                                    random_id=get_random_id()
                                )
                    except:
                        pass



                if self_message[0:5] == '/help' or self_message[0:5] == '!help' or self_message[0:5] == '+help':
                        if (data[str(chat_id)][str(user_id)]['is_admin'] == 'true') or (data[str(chat_id)][str(user_id)]['is_specadm'] == 'true'):
                            self_message = event.object.message['text']
                            if data[str(chat_id)][str(user_id)]['is_admin'] == 'true':
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='User Commands:\n/randstatus - любой статус среди участников беседы.\n/roll - бросить кости.\n/q - выйти из беседы.\n/checkme - проверить, состою ли я в группе.\n/list - список участников беседы.\n/help - помощь.\nAdmin Commands:\n/kick - кикнуть пользователя\n/call - вызвать всех участников беседы.\n/ban - заблокировать пользователя\n/unban - разблокировать пользователя.\n/warn - выдать предупреждение.\n/unwarn - снять предупреждение.\n/filter - добавить слово в фильтр.\n/delfilter - убрать слово из фильтра.\n/flist - слова в фильтре.\n/fclear - полностью очистить фильтр.',
                                    attachment='wall-122549424_22',
                                    random_id=get_random_id()
                                )
                            elif data[str(chat_id)][str(user_id)]['is_specadm'] == 'true':
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='User Commands:\n/randstatus - любой статус среди участников беседы.\n/roll - бросить кости.\n/q - выйти из беседы.\n/checkme - проверить, состою ли я в группе.\n/list - список участников беседы.\n/help - помощь.\nAdmin Commands:\n/kick - кикнуть пользователя\n/call - вызвать всех участников беседы.\n/ban - заблокировать пользователя\n/unban - разблокировать пользователя.\n/warn - выдать предупреждение.\n/unwarn - снять предупреждение.\nSpecial Commands:\n/filecheck - чекнуть логи.\n/adm - назначить администратора\n/unadm - снять администратора\n/delphoto - удалить фото беседы.\n/title - изменить название беседы\n/unpin - открепить сообщение беседы.\n/filteradd - добавить слово в фильтр\n/filterdel - удалить слово из фильтра\n/warn - выдать предупреждение\n/unwarn - снять предупреждение\n/rule - активировать новое правило.\n/rlist - список доступных правил.',
                                    attachment='wall-122549424_22',
                                    random_id=get_random_id()
                                )
                        else:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=chat_id,
                                message='User Commands:\n/randstatus - любой статус среди участников беседы.\n/roll - бросить кости.\n/q - выйти из беседы.\n/checkme - проверить, состою ли я в группе.\n/list - список участников беседы.\n/help - помощь.\n',
                                attachment='wall-122549424_22',
                                random_id=get_random_id()
                            )
                        message = 'Пользователь Id: ' + str(user_id) + ', ввёл команду: ' + str(event.object.message['text'])
                        print(message)
                if self_message[0:4] == '/rep' or self_message[0:4] == '+rep' or self_message[0:4] == '!rep':
                    data1 = json.load(open('/home/Maksimka17017/players.json'))
                    if data1[str(chat_id)][str(user_id)]['reports'] == "1":
                        vk.messages.send(chat_id=chat_id, message="Вы уже отправили репорт, ожидайте ответа.", random_id=get_random_id())
                    else:
                        message="🗣Вам поступил репорт! Текст: " + str(self_message[5:len(self_message)]) + ". ID беседы: " + str(chat_id) + ". ID user: " + str(user_id)
                        print(message)
                        data1 = json.load(open('/home/Maksimka17017/players.json'))
                        vk.messages.send(user_id=341919526, message="Вам поступил репорт! Текст: " + str(self_message[5:len(self_message)]) + ". ID беседы: " + str(chat_id) + ". ID user: " + str(user_id), random_id=get_random_id())
                        keyboard = VkKeyboard(inline=True)
                        keyboard.add_button('Отменить', color=VkKeyboardColor.NEGATIVE)
                        vk.messages.send(
                            peer_id=peer_id,
                            message='✅ Ваш репорт отправлен разработчику!',
                            random_id=get_random_id(),
                            keyboard=keyboard.get_keyboard()
                        )
                        data1[str(chat_id)][str(user_id)]['reports'] = "1"
                        with open('/home/Maksimka17017/players.json', 'w') as outfile_1:
                            json.dump(data1, outfile_1, indent=4)
                if self_message == '[club122549424|@fogetbot] Отменить' or self_message == '[club122549424|Foget Bot] Отменить':
                    data1 = json.load(open('/home/Maksimka17017/players.json'))
                    if data1[str(chat_id)][str(user_id)]['reports'] == "1":
                        vk.messages.send(chat_id=chat_id,
                            message="Ваш репорт был отменён.",
                            random_id=get_random_id())
                        data1[str(chat_id)][str(user_id)]['reports'] = "0"
                        with open('/home/Maksimka17017/players.json', 'w') as outfile_1:
                            json.dump(data1, outfile_1, indent=4)
                        message="🗣Репорт был отозван." + ". ID беседы: " + str(chat_id) + ". ID user: " + str(user_id)
                        print(message)
                        vk.messages.send(user_id=341919526, message=message, random_id=get_random_id())
                    else:
                        vk.messages.send(chat_id=chat_id, message="Вы не отправляли репорт.", random_id=get_random_id())

                if self_message[0:5] == '!warn' or self_message[0:5] == '/warn' or self_message[0:5] == '+warn':
                    try:
                        if "reply_message" in event.object.message:
                            id = event.object.message['reply_message']['from_id']
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            user_id = user_data[0]["id"]
                            data = json.load(open('/home/Maksimka17017/players.json'))
                            data[str(chat_id)][str(user_id)]['warn'] += 1
                            if data[str(chat_id)][str(user_id)]['is_admin'] == 'true':
                                vk.messages.send(chat_id=chat_id,
                                                 message="Вы не можете выдать предупреждение администратору.",
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['is_specadm'] == 'true':
                                vk.messages.send(chat_id=chat_id,
                                                 message="Вы не можете выдать предупреждение спец.администратору.",
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['is_developer'] == 'true':
                                vk.messages.send(chat_id=chat_id,
                                                 message="Вы не можете выдать предупреждение этому пользователю.",
                                                 random_id=get_random_id())
                            else:
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                if data[str(chat_id)][str(user_id)]['warn'] == 3:
                                    vk.messages.removeChatUser(chat_id=chat_id, user_id=user_id)
                                    vk.messages.send(chat_id=chat_id,
                                                     message="Пользователь был исключен за 3 предупреждения.",
                                                     random_id=get_random_id())
                                    data[str(chat_id)][str(user_id)]['warn'] = data[str(chat_id)][str(user_id)]['warn'] - 3
                                    with open('/home/Maksimka17017/players.json', 'w') as outfile_1:
                                        json.dump(data, outfile_1, indent=4)
                                else:
                                    vk.messages.send(chat_id=chat_id,
                                                     message='⚠ Пользователь получил 1 предупреждение. ' + '[' + str(
                                                         data[str(chat_id)][str(user_id)]['warn']) + '/3]',
                                                     random_id=get_random_id())
                        else:
                            id = self_message[9:self_message.index("|")]
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            user_id = user_data[0]["id"]
                            data = json.load(open('/home/Maksimka17017/players.json'))
                            data[str(chat_id)][str(user_id)]['warn'] += 1
                            if data[str(chat_id)][str(user_id)]['is_admin'] == 'true':
                                vk.messages.send(chat_id=chat_id,
                                                 message="Вы не можете выдать предупреждение администратору.",
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['is_specadm'] == 'true':
                                vk.messages.send(chat_id=chat_id,
                                                 message="Вы не можете выдать предупреждение спец.администратору.",
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['is_developer'] == 'true':
                                vk.messages.send(chat_id=chat_id,
                                                 message="Вы не можете выдать предупреждение этому пользователю.",
                                                 random_id=get_random_id())
                            else:
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                if data[str(chat_id)][str(user_id)]['warn'] == 3:
                                    vk.messages.removeChatUser(chat_id=chat_id, user_id=user_id)
                                    vk.messages.send(chat_id=chat_id,
                                                     message="Пользователь был исключен за 3 предупреждения.",
                                                     random_id=get_random_id())
                                    data[str(chat_id)][str(user_id)]['warn'] = data[str(chat_id)][str(user_id)]['warn'] - 3
                                    with open('/home/Maksimka17017/players.json', 'w') as outfile_1:
                                        json.dump(data, outfile_1, indent=4)
                                else:
                                    vk.messages.send(chat_id=chat_id,
                                                     message='⚠ Пользователь получил 1 предупреждение. ' + '[' + str(
                                                         data[str(chat_id)][str(user_id)]['warn']) + '/3]',
                                                     random_id=get_random_id())

                        message = 'Пользователь Id: ' + str(user_id) + ', ввёл команду: ' + str(event.object.message['text'])
                        print(message)
                    except:
                        vk.messages.send(chat_id=chat_id,
                                         message='error',
                                         random_id=get_random_id())
                if self_message[0:7] == '!unwarn' or self_message[0:7] == '/unwarn' or self_message[0:7] == '+unwarn':
                    try:
                        if "reply_message" in event.object.message:
                            id = event.object.message['reply_message']['from_id']
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            user_id = user_data[0]["id"]
                            data = json.load(open('/home/Maksimka17017/players.json'))
                            if data[str(chat_id)][str(user_id)]['warn'] > 0:
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    data[str(chat_id)][str(user_id)]['warn'] = data[str(chat_id)][str(user_id)][
                                                                                        'warn'] - 1
                                    json.dump(data, outfile, indent=4)
                                vk.messages.send(chat_id=chat_id,
                                                 message='⚠ Вы сняли одно предупреждение. ' + '[' + str(
                                    data[str(chat_id)][str(user_id)]['warn']) + '/3]',
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['warn'] == 0:
                                vk.messages.send(chat_id=chat_id,
                                                 message='У пользователя нет предупреждений.',
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['warn'] < 0:
                                data[str(chat_id)][str(user_id)]['warn'] += 0
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                        else:
                            id = self_message[11:self_message.index("|")]
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            user_id = user_data[0]["id"]
                            data = json.load(open('/home/Maksimka17017/players.json'))
                            if data[str(chat_id)][str(user_id)]['warn'] > 0:
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    data[str(chat_id)][str(user_id)]['warn'] = data[str(chat_id)][str(user_id)][
                                                                                        'warn'] - 1
                                    json.dump(data, outfile, indent=4)
                                vk.messages.send(chat_id=chat_id,
                                                 message='⚠ Вы сняли одно предупреждение. ' + '[' + str(
                                                     data[str(chat_id)][str(user_id)]['warn']) + '/3]',
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['warn'] == 0:
                                vk.messages.send(chat_id=chat_id,
                                                 message='У пользователя нет предупреждений.',
                                                 random_id=get_random_id())
                            elif data[str(chat_id)][str(user_id)]['warn'] < 0:
                                data[str(chat_id)][str(user_id)]['warn'] += 0
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)

                    except:
                        vk.messages.send(chat_id=chat_id,
                            message='error',
                            random_id=get_random_id())
                if "action" in event.object.message:
                    try:
                        bdcheck()
                        check = vk.groups.isMember(group_id='fogetbot', user_id=event.object.message['action']['member_id'])
                        if check == 1:
                            pass
                        else:
                            vk.messages.removeChatUser(chat_id=chat_id, user_id=user_id)
                            vk.messages.send(chat_id=chat_id,
                                        message='Пользователь не является участником тестовой группы.',
                                        random_id=get_random_id())
                    except:
                        print(1)
                if self_message == '/start':
                    try:
                        bdcheck()
                        if bdcheck1() == True:
                            message = '🔔 ID ' + str(user_id) + ' был зарегистрирован как основатель беседы.'
                            print(message)
                            vk.messages.send(user_id=341919526, message=message, random_id=get_random_id())
                            data_5 = json.load(open('/home/Maksimka17017/players.json'))
                            data_2 = vk.messages.getConversationMembers(peer_id=peer_id)['items']
                            data[str(chat_id)][str(user_id)]['is_specadm'] = 'true'
                            with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                            l = []
                            for item in data_2:
                                if "member_id" in item:
                                    l.append(item['member_id'])
                                    for item in l:
                                        data_3 = str(item)
                                        data_5[str(chat_id)][data_3] = {
                                            "invite_by_user_id": str(user_id),
                                            "member": "true",
                                            "is_admin": "false",
                                            "reports": "0",
                                            "is_developer": "false",
                                            "is_specadm": "false",
                                            "nickname": "Пользователь",
                                            "messages": 0,
                                            "warn": 0,
                                            "ban": "false",
                                            "ban_reason": "None",
                                            "ban_by": "None"}
                                        data_5[str(chat_id)][str(user_id)]['is_specadm'] = "true"
                                        with open('/home/Maksimka17017/players.json', 'w') as file:
                                            json.dump(data_5, file, indent=4)

                    except:
                        vk.messages.send(chat_id=chat_id,
                                        message='Вы не выдали боту права администратора в беседе. Функционал ограничен.',
                                        random_id=get_random_id())
                if (self_message[0:4] == '/adm' or self_message[0:4] == '+adm' or self_message[0:4] == '!adm') and (data[str(chat_id)][str(user_id)]['is_specadm'] == 'true'):
                    try:
                        data = json.load(open('/home/Maksimka17017/players.json'))
                        if "reply_message" in event.object.message:
                            id = event.object.message['reply_message']['from_id']
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            if data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] == "true":
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь уже является администратором.',
                                    random_id=get_random_id()
                                )
                            elif data[str(chat_id)][str(user_data[0]['id'])]['is_specadm'] == "true":
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь уже является специальным администратором.',
                                    random_id=get_random_id()
                                )
                            else:
                                data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] = "true"
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='add adm: ok',
                                        random_id=get_random_id()
                                    )
                        else:
                            id = self_message[8:self_message.index("|")]
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            if data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] == "true":
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь уже является администратором.',
                                    random_id=get_random_id()
                                )
                            elif data[str(chat_id)][str(user_data[0]['id'])]['is_specadm'] == "true":
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь уже является специальным администратором.',
                                    random_id=get_random_id()
                                )
                            else:
                                data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] = "true"
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='add adm: ok',
                                        random_id=get_random_id()
                                    )
                    except:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='add adm: error',
                            random_id=get_random_id()
                        )
                if (self_message[0:6] == "!unadm" or self_message[0:6] == "/unadm" or self_message[0:6] == "+unadm") and (data[str(chat_id)][str(user_id)]['is_specadm'] == 'true'):
                    try:
                        data = json.load(open('/home/Maksimka17017/players.json'))
                        if "reply_message" in event.object.message:
                            id = event.object.message['reply_message']['from_id']
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            if data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] == "true":
                                data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] = "false"
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='unadm: ok',
                                        random_id=get_random_id()
                                    )
                            else:
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь не является администратором.',
                                    random_id=get_random_id()
                                )
                        else:
                            id = self_message[10:self_message.index("|")]
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            if data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] == "true":
                                data[str(chat_id)][str(user_data[0]['id'])]['is_admin'] = "false"
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='unadm: ok',
                                        random_id=get_random_id()
                                    )
                            else:
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь не является администратором.',
                                    random_id=get_random_id()
                                )

                    except:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='unadm: error',
                            random_id=get_random_id()
                        )
                if (self_message[0:5] == '!call' or self_message[0:5] == '/call' or self_message[0:5] == '+call') and (data[str(chat_id)][str(user_id)]['is_specadm'] == 'true' or data[str(chat_id)][str(user_id)]['is_admin'] == 'true'):
                    try:
                        a = self_message.split()
                        b = a[1:]
                        c = " ".join(b)
                        vk.messages.send(  # Отправляем собщение
                                chat_id=chat_id,
                                message='Вы были вызваны ' + '[id' + str(user_id) + '|администратором] беседы. Причина вызова: ' + str(c) + '. @all',
                                random_id=get_random_id()
                            )
                    except:
                        print('error')

                if self_message[0:4] == '!ban':
                    try:
                        message = self_message
                        res = message.split()
                        try:
                            if "reply_message" in event.object.message:
                                id = event.object.message['reply_message']['from_id']
                                try:
                                    if len(str(res[1])) >= 3:
                                        pass
                                    else:
                                        vk.messages.send(  # Отправляем собщение
                                            chat_id=chat_id,
                                            message='Причина от 3-ёх символов.',
                                            random_id=get_random_id()
                                        )
                                    data = json.load(open('/home/Maksimka17017/players.json'))
                                    user_data = vk.users.get(user_ids=id, access_token=token)
                                    if (data[str(chat_id)][str(user_data[0]['id'])]['is_specadm']) and (
                                    data[str(chat_id)][str(user_data[0]['id'])]['is_admin']) == "false":
                                        if data[str(chat_id)][str(user_data[0]['id'])]['ban'] == "false":
                                            data[str(chat_id)][str(user_data[0]['id'])]['ban'] = "true"
                                            data[str(chat_id)][str(user_data[0]['id'])]['ban_by'] = str(user_id)
                                            data[str(chat_id)][str(user_data[0]['id'])]['ban_reason'] = " ".join(res[1:])
                                            with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                                json.dump(data, outfile, indent=4)
                                                try:
                                                    vk.messages.removeChatUser(chat_id=chat_id,
                                                                                user_id=user_data[0]['id'])
                                                except:
                                                    pass
                                                vk.messages.send(  # Отправляем собщение
                                                    chat_id=chat_id,
                                                    message='ban: ok',
                                                    random_id=get_random_id()
                                                )
                                        else:
                                            vk.messages.send(  # Отправляем собщение
                                                chat_id=chat_id,
                                                message='Пользователь уже заблокирован.',
                                                random_id=get_random_id()
                                            )
                                    else:
                                        vk.messages.send(  # Отправляем собщение
                                            chat_id=chat_id,
                                            message='Вы не можете заблокировать администратора.',
                                            random_id=get_random_id()
                                        )
                                except IndexError:
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='Некорректная причина.',
                                        random_id=get_random_id()
                                    )

                            else:
                                try:
                                    if len(str(res[2])) >= 3:
                                        pass
                                    else:
                                        vk.messages.send(  # Отправляем собщение
                                            chat_id=chat_id,
                                            message='Причина от 3-ёх символов.',
                                            random_id=get_random_id()
                                        )
                                    data = json.load(open('/home/Maksimka17017/players.json'))
                                    id = self_message[8:self_message.index("|")]
                                    user_data = vk.users.get(user_ids=id, access_token=token)
                                    if (data[str(chat_id)][str(user_data[0]['id'])]['is_specadm']) and (
                                    data[str(chat_id)][str(user_data[0]['id'])]['is_admin']) == "false":
                                        if data[str(chat_id)][str(user_data[0]['id'])]['ban'] == "false":
                                            data[str(chat_id)][str(user_data[0]['id'])]['ban'] = "true"
                                            data[str(chat_id)][str(user_data[0]['id'])]['ban_by'] = str(user_id)
                                            data[str(chat_id)][str(user_data[0]['id'])]['ban_reason'] = " ".join(res[2:])
                                            with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                                json.dump(data, outfile, indent=4)
                                                try:
                                                    vk.messages.removeChatUser(chat_id=chat_id,
                                                                                user_id=user_data[0]['id'])
                                                except:
                                                    pass
                                                vk.messages.send(  # Отправляем собщение
                                                    chat_id=chat_id,
                                                    message='ban: ok',
                                                    random_id=get_random_id()
                                                )
                                        else:
                                            vk.messages.send(  # Отправляем собщение
                                                chat_id=chat_id,
                                                message='Пользователь уже заблокирован.',
                                                random_id=get_random_id()
                                            )
                                    else:
                                        vk.messages.send(  # Отправляем собщение
                                            chat_id=chat_id,
                                            message='Вы не можете заблокировать администратора.',
                                            random_id=get_random_id()
                                        )
                                except IndexError:
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='Некорректная причина.',
                                        random_id=get_random_id()
                                    )
                        except:
                            vk.messages.send(  # Отправляем собщение
                                chat_id=chat_id,
                                message='ban: error#1',
                                random_id=get_random_id()
                            )
                    except:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='ban: error#2',
                            random_id=get_random_id()
                        )
                if 'action' in event.object.message:
                    try:
                        if 'action' in event.object.message:
                            data_1 = json.load(open('/home/Maksimka17017/players.json'))
                            if event.object.message['action']['type'] == "chat_invite_user":
                                if data_1[str(chat_id)][str(event.object.message['action']['member_id'])]['ban'] == "true":
                                    vk.messages.removeChatUser(chat_id=chat_id,
                                                                user_id=event.object.message['action']['member_id'])
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='Пользователь находится в чёрном списке.\n Занёс в чёрный список - ' + '[id' + str(
                                            data_1[str(chat_id)][str(event.object.message['action']['member_id'])][
                                                'ban_by']) + '|модератор] беседы. Причина: ' + str(
                                            data_1[str(chat_id)][str(event.object.message['action']['member_id'])]['ban_reason']),
                                        random_id=get_random_id()
                                    )
                                else:
                                    pass
                            else:
                                pass
                        else:
                            pass
                    except:
                        print('error')

                if (self_message[0:6] == '+unban' or self_message[0:6] == '!unban' or self_message[0:6] == '/unban') and (data[str(chat_id)][str(user_id)]['is_specadm'] == 'true' or data[str(chat_id)][str(user_id)]['is_admin'] == 'true'):
                    try:
                        if "reply_message" in event.object.message:
                            id = event.object.message['reply_message']['from_id']
                            data = json.load(open('/home/Maksimka17017/players.json'))
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            if data[str(chat_id)][str(user_data[0]['id'])]['ban'] == "true":
                                data[str(chat_id)][str(user_data[0]['id'])]['ban'] = "false"
                                data[str(chat_id)][str(user_data[0]['id'])]['ban_by'] = "None"
                                data[str(chat_id)][str(user_data[0]['id'])]['ban_reason'] = "None"
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='unban: ok',
                                        random_id=get_random_id()
                                    )
                            else:
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь не заблокирован.',
                                    random_id=get_random_id()
                                )
                        else:
                            data = json.load(open('/home/Maksimka17017/players.json'))
                            id = self_message[10:self_message.index("|")]
                            user_data = vk.users.get(user_ids=id, access_token=token)
                            if data[str(chat_id)][str(user_data[0]['id'])]['ban'] == "true":
                                data[str(chat_id)][str(user_data[0]['id'])]['ban'] = "false"
                                data[str(chat_id)][str(user_data[0]['id'])]['ban_by'] = "None"
                                data[str(chat_id)][str(user_data[0]['id'])]['ban_reason'] = "None"
                                with open('/home/Maksimka17017/players.json', 'w') as outfile:
                                    json.dump(data, outfile, indent=4)
                                    vk.messages.send(  # Отправляем собщение
                                        chat_id=chat_id,
                                        message='unban: ok',
                                        random_id=get_random_id()
                                    )
                            else:
                                vk.messages.send(  # Отправляем собщение
                                    chat_id=chat_id,
                                    message='Пользователь не заблокирован.',
                                    random_id=get_random_id()
                                )

                    except:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='unban: error',
                            random_id=get_random_id()
                        )

                if self_message == '/q' or self_message == '+q' or self_message == '!q':
                    try:
                        data = json.load(open('/home/Maksimka17017/players.json'))
                        if data[str(chat_id)][str(user_id)]['is_specadm'] == 'true' or data[str(chat_id)][str(user_id)]['is_admin']:
                            vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='self.kick: denied',
                            random_id=get_random_id()
                        )
                        else:
                            vk.messages.removeChatUser(chat_id=chat_id, user_id=user_id)
                            vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='self kick: ok',
                            random_id=get_random_id()
                        )
                    except:
                        pass

                if (self_message[0:6] == '!title' or self_message[0:6] == '/title' or self_message[0:6] == '+title') and (data[str(chat_id)][str(user_id)]['is_specadm'] == 'true'):
                    change = vk.messages.editChat(chat_id=chat_id, title=self_message[7:len(self_message)])
                    if change == 1:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='title: ok',
                            random_id=get_random_id()
                        )
                    else:
                        vk.messages.send(  # Отправляем собщение
                            chat_id=chat_id,
                            message='title: error',
                            random_id=get_random_id()
                        )
            if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                if self_message[0:5] == '/drep':
                    data1 = json.load(open('/home/Maksimka17017/players.json'))
                    message = self_message.split()
                    osn = message[3:]
                    user = message[2]
                    chat_id = message[1]
                    b = " ".join(osn)
                    if data1[str(chat_id)][str(user)]['reports'] == "0":
                        print('Пользователь не отправлял репорт.')
                        vk.messages.send(user_id=341919526, message='Пользователь не отправлял репорт.', random_id=get_random_id())
                    else:
                        message1 ="Вам поступил ответ на репорт! Текст от разработчика: " + str(b) + ". ID пользователя, подававшего репорт: " + str(user)
                        a = ' 🗣 Ответ на репорт отправлен!\n Текст: ' + message1
                        print(a)
                        vk.messages.send(user_id=341919526, message=a, random_id=get_random_id())
                        data1 = json.load(open('/home/Maksimka17017/players.json'))
                        data1[str(chat_id)][str(user)]['reports'] = "0"
                        with open('/home/Maksimka17017/players.json', 'w') as outfile:
                            json.dump(data1, outfile, indent=4)
                        vk.messages.send(chat_id=chat_id, message="Вам поступил ответ на репорт! Текст от разработчика: " + str(b) + ". ID пользователя, подававшего репорт: " + str(user), random_id=get_random_id())

    except:
        pass
