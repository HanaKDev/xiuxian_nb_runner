import os.path
import nonebot

from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter

from hanahime.other.datetime import StrTime
from hanahime.utils.logging_config import logger

nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins('echo')

nonebot.load_from_toml(os.path.join('.', 'pyproject.toml'))

if __name__ == "__main__":
    logger.debug(f'{StrTime()}')
    nonebot.run()
