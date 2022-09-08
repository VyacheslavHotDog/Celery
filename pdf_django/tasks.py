
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
from .celery import app
from .settings import EMAIL_HOST_USER
from mainapp.utils import PdfGenerator

logger = get_task_logger(__name__)


@app.task(name='sample_task')
def sample_task(pdf_data):

    pdf = PdfGenerator().create(pdf_data)

    logger.info("Отправляю pdf.")
    mail = EmailMessage(
        'Склад',
        'Изменилось количество товаров на складе',
        EMAIL_HOST_USER,
        ['sl.burlakov@vk.com'],
        headers={'Reply-To':  'tihon4326@mail.ru'}
    )
    mail.attach('report.pdf', pdf)
    mail.send()
