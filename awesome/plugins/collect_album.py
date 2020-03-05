import nonebot
from nonebot.typing import Context_T
from datetime import datetime
import pytz

bot = nonebot.get_bot()

@bot.on_message('group')
async def handle_group_message(ctx: Context_T):
    if 'albumData' in str(ctx['message']):
        if '新增' in str(ctx['message']):
            print('Got Album from:')
            print(ctx['sender']['nickname'])
            gid = ctx['group_id']
            member_info = await bot.get_group_member_info(group_id=gid, user_id=ctx['user_id'], no_cache='true')
            card = member_info['card']
            now = datetime.now(pytz.timezone('Asia/Shanghai'))
            with open('data.txt', 'a') as a_writer:
                msg = f'现在是{now.year}年{now.month}月{now.day}日 {now.hour}点{now.minute}分 ，群机器人0号已收到并记录{card}的群相册数据'
                a_writer.write(f'{now.year}/{now.month}/{now.day}')
                a_writer.write('\t')
                a_writer.write(f'{card}')
                a_writer.write('\t')
                a_writer.write(f'{gid}')
                a_writer.write('\n')
                await bot.send_group_msg(group_id=ctx['group_id'], message=msg)




