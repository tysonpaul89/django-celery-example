# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery.decorators import task
from django.core.mail import send_mail
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@task
def send_feedback_email(from_email, message):
    """
    Send email in the background
    """
    logger.info("Sent feedback email")
    return send_mail(
        'Feedback', # Subject
        message, # Message
        from_email, # From Email
        ['tyson.paul@digitalmesh.com'], # To email
        fail_silently=False,
    )