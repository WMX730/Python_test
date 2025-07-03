import logging
from loguru import logger

''''
两种使用方法：
import logging
from loguru import logger
'''

'''
logging用法
'''

# 简单日志
# 默认等级为WARNING，低于WARNING的日志不会输出
logging.basicConfig(level=logging.INFO)

# 不同级别的日志
logging.debug("这是调试信息")
logging.info("这是一般信息")
logging.warning("这是警告信息")
logging.error("这是错误信息")
logging.critical("这是严重错误")

# 日志写入文件  
logging.basicConfig(
    filename='example.log', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
    )

logging.info("这是调试信息，写入文件")

'''
format参数说明: %(asctime)s:当前时间
               %(levelname)s:日志等级
               %(message)s:日志内容
'''

# 手动构造日志
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 输出到控制台
console = logging.StreamHandler()
console.setLevel(logging.INFO)

# 输出到文件
file = logging.FileHandler('all.log', encoding='utf-8')
file.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
file.setFormatter(formatter)

logger.addHandler(console)
logger.addHandler(file)

logger.debug("调试")
logger.info("信息")
logger.warning("警告")


'''
logger用法
'''
# 打印到终端
logger.debug("调试信息")
logger.info("普通信息")
logger.warning("警告信息")
logger.error("错误信息")
logger.critical("严重错误")
# 输出到文件
logger.add("name.log")
logger.info("这是写入文件的日志信息")
