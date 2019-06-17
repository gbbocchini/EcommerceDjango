# EcommerceDjango
Ecommerce completo em Django. Pagamentos via API Paypal!


Instala��o:

- clone o projeto;
- fa�a um VirtualEnv com os requirements.txt;
- fa�a as migrations necess�rias (python manage.py migrate, python manage.py makemigrations e python manage.py migrate novamente);
- RUNSERVER


PS: gere uma "SECRET KEY" para o projeto funcionar e inclua em "settings.py". Abra um console Python e:


- import random

- result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

- print(result)


Ser� necess�rio tamb�m chaves API Paypal (SandBox ou produ��o): https://developer.paypal.com 