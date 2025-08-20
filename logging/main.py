import logging


logger = logging.getLogger(__name__)


print(f'{logger.hasHandlers()=}')

#Default is WARNING=30
print(f'{logger.getEffectiveLevel()=}')

logger.debug('debug message')
logger.info('info message')
logger.error('error message')
logger.warning('warning message')


# OUTPUT

# logger.hasHandlers()=False
# logger.getEffectiveLevel()=30
# error message
# warning message
#
# Process finished with exit code 0