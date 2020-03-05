import nonebot
from nonebot.typing import Context_T
from datetime import datetime
import pytz


bot = nonebot.get_bot()

@bot.on_notice()
async def handle_group_evevt(ctx: Context_T):
    print('Group Event Get')
    print('ctx:', ctx)
    if str(ctx['file']):
        print('Got File from:')
        print(ctx['user_id'])
        if not ctx['user_id'] == 150452076:
            gid = ctx['group_id']
            member_info = await bot.get_group_member_info(group_id=gid, user_id=ctx['user_id'], no_cache='true')
            card = member_info['card']
            now = datetime.now(pytz.timezone('Asia/Shanghai'))
            with open('data.txt', 'a') as a_writer:
                msg = f'现在是{now.year}年{now.month}月{now.day}日 {now.hour}点{now.minute}分 ，群机器人0号已收到并记录{card}的群文件数据'
                a_writer.write(f'{now.year}/{now.month}/{now.day}')
                a_writer.write('\t')
                a_writer.write(f'{card}')
                a_writer.write('\t')
                a_writer.write(f'{gid}')
                a_writer.write('\n')
                await bot.send_group_msg(group_id=ctx['group_id'], message=msg)

