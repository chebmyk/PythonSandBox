import logging
import logging.config
import yaml

logger = logging.getLogger('app')


def configure_logger():
    with open('logger_config.yml') as config:
        config = yaml.safe_load(config)

    logging.config.dictConfig(config)



def main():
    for i in range(1,100):
        logger.debug("debug message")
        logger.info("info message")
        logger.warning("warning message")

if __name__ == "__main__":
    configure_logger()
    main()