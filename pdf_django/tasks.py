
from celery.utils.log import get_task_logger
from django.core.mail import EmailMessage
from .celery import app
from .settings import EMAIL_HOST_USER
logger = get_task_logger(__name__)
from mainapp.utils import PdfGenerator


@app.task(name='sample_task')
def sample_task(pdf_data):

    pdf = PdfGenerator().create(pdf_data)

    logger.info("Отправляю pdf.")
    mail = EmailMessage(
        'subject',
        'content',
        EMAIL_HOST_USER,
        ['sl.burlakov@vk.com'],
        headers={'Reply-To':  'tihon4326@mail.ru'}
    )
    mail.attach('report.pdf', pdf)
    mail.send()
