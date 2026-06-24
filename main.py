import time

from loguru import logger
from prefect import flow


@flow
def hello_world():
    logger.info("Hello World!")
    time.sleep(5)
    return "Hello World!"
