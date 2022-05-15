from decorate import decorator2
from log_helper import *


@decorator2
def exper(str):
    print('in the exper module')
    logger.info("in the exper module")
    return str

print(exper('hello'))