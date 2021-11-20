from time import sleep

from celery import shared_task
from loguru import logger


@shared_task
def send_email(email, body, subject):
    for i in range(1, 6):
        logger.info(f"{i} sec...")
        sleep(1)

    logger.info("Email was sent")
    return "sent!"
