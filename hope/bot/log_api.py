import logging

class BotLoger:    
    def addlog(self, path, message):
        logging.basicConfig(filename=f"hope/logs/{path}",
                format='%(asctime)s %(name)s %(levelname)s %(message)s',
                filemode='a',
                level=logging.INFO)
        logger = logging.getLogger()
        logger.info(message)
