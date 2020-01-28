from datetime import datetime

import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError


@nonebot.scheduler.scheduled_job('interval', minutes=1)
async def _():
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        # await bot.send_group_msg(group_id=201520794,
        #                         message=f'现在{now.hour}点{now.minute}分啦！')
        await bot.send_private_msg(user_id=2529223739,
                                 message=f'现在{now.hour}点{now.minute}分啦！')
    except CQHttpError:
        print("Error")
