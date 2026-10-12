
import logging

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

logger.debug("data ")

logger.info("Hello ")

def sum_num(num1, num2):
    if isinstance(num1, int) and isinstance(num2, int):
        logger.info(num1 + num2, "successfully sum")
        return num1 + num2
    logger.error(f"num1 and num2 must be int")

sum_num(1, "2")
