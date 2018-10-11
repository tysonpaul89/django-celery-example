from django.shortcuts import render
from .tasks import send_feedback_email

def test(request):
    email_status = None
    if (request.method == 'POST'):
        data = request.POST
        send_feedback_email.delay(data['from'], data['message'])
        email_status = True
    return render(request, 'demo/test.html', { 'email_status': email_status })