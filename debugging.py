import logging
import datetime
import sentry_sdk


def __startsentry(level):
    sentry_sdk.init(
    dsn="https://8324d572a6c64c8fac5e8429724bb9d8@o570645.ingest.sentry.io/6631912",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0 if level == 'debug' else 1.0
    )


def __startlogger(level, filename):
    logger = logging.getLogger(level)
    logger.basicConfig(filename=filename, filemode='w', format="""%(name)s - %(asctime)s - %(levelname)s - %(message)s""")


def initialize_debug_services(level='debug', filename=f'{datetime.now().strftime}.log'):
    logger = __startlogger(level, filename)
    __startsentry(level)
    return logger
