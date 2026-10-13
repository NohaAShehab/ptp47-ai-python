


import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("scoopyDoooo")

name = "Ahmed"

logger.info(f"variable with name > name ={name}")
print(name)

try:
    name = int(name)
except Exception as e:
    logger.error(f"variable with name > variable was not converted")
else:
    logger.warning(f"Are you playing")


logger.critical(f"variable with name > name was converted")