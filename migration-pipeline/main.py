from logger import get_logger
from config import Config

def main():
    config = Config()
    logger = get_logger(config.app_name)
    logger.info("Migration pipeline started.")
    logger.info("configurtion loaded.")
    #logger.info(f"Starting {config.app_name} with log level {config.log_level}")
    # Further migration pipeline logic would go here

if __name__ == "__main__":
    main()