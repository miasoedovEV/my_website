from django.shortcuts import render
from django.urls import reverse
from django.views.generic import FormView
from .forms import FeedbackForm
from .models import Feedback
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .config import PASSWORD

SERVER = 'smtp.mail.ru'
ADD_FROM = "stincs01@mail.ru"
RECIPIENT = "stincs369@mail.ru"


def send_email(name, email, phone_number, text):
    subject = f'Приглашение от {name} с почтой {email} и номером {phone_number}'
    html = '<html><head></head><body><p>' + text + '</p></body></html>'
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = ADD_FROM
    msg['To'] = RECIPIENT
    part_text = MIMEText(text, 'plain')
    part_html = MIMEText(html, 'html')
    msg.attach(part_text)
    msg.attach(part_html)
    email = smtplib.SMTP_SSL(SERVER)
    email.login(ADD_FROM, PASSWORD)
    email.sendmail(from_addr=ADD_FROM, to_addrs=RECIPIENT, msg=msg.as_string())
    email.quit()


# Create your views here.

def main_page(request):
    return render(request, 'index.html')


def page_about_me(request):
    return render(request, 'about_me.html')


def page_skills(request):
    return render(request, 'skills.html')


def page_cause(request):
    return render(request, 'causes.html')


class FeedbackCreateView(FormView):
    form_class = FeedbackForm
    template_name = 'feedback.html'

    def form_valid(self, form):
        name = self.request.POST['name'],
        phone_number = self.request.POST['phone_number'],
        email = self.request.POST['email'],
        text = self.request.POST['text']
        Feedback.objects.create(
            name=name,
            phone_number=phone_number,
            email=email,
            text=text
        )
        send_email(name, phone_number, email, text)
        return super(FeedbackCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('main')
