import nonebot
from nonebot.typing import Context_T
from datetime import datetime
import pytz

bot = nonebot.get_bot()

@bot.on_message('group')
async def handle_group_message(ctx: Context_T):
    if 'albumData' in str(ctx['message']):
        print('Got Album from:')
        print(ctx['sender']['nickname'])
        member_info = await bot.get_group_member_info(group_id=ctx['group_id'], user_id=ctx['user_id'], no_cache='true')
        card = member_info['card']
        now = datetime.now(pytz.timezone('Asia/Shanghai'))
        with open('data.txt', 'a') as a_writer:
            msg = f'现在是{now.year}/{now.month}/{now.day} {now.hour}:{now.minute} ，群机器人0已收到{card}的数据'
            a_writer.write(f'{now.year}/{now.month}/{now.day}')
            a_writer.write('\t')
            a_writer.write(f'{now.hour}:{now.minute}')
            a_writer.write('\t')
            a_writer.write(f'{card}')
            a_writer.write('\n')
            await bot.send_group_msg(group_id=ctx['group_id'], message=msg)




