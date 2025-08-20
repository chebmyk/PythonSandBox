import logging
import logging.config
import yaml

logger = logging.getLogger('app')


def configure_logger():
    with open('logger_config.yml') as config:
        config = yaml.safe_load(config)

    logging.config.dictConfig(config)


class CustomLogFilter(logging.Filter):

    def __init__(self, arg_name = None, arg_threshold = None):
        self.arg_name = arg_name
        self.arg_threshold = arg_threshold

    def filter(self, record):

        return (
            self.arg_name is not None
            and self.arg_threshold is not None
            and hasattr(record, self.arg_name)
            and getattr(record, self.arg_name) >= self.arg_threshold
        )



def main():
    for i in range(1,2):
        logger.debug("debug message")
        logger.info("info message", extra={'param': 100})
        logger.warning("warning message", extra={'param': 300} )

if __name__ == "__main__":
    configure_logger()
    main()