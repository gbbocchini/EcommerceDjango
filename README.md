# EcommerceDjango
Ecommerce completo em Django. Pagamentos via API Paypal!


Instalação:

- clone o projeto;
- faça um VirtualEnv com os requirements.txt;
- faça as migrations necessárias (python manage.py migrate, python manage.py makemigrations e python manage.py migrate novamente);
- RUNSERVER


PS: gere uma "SECRET KEY" para o projeto funcionar e inclua em "settings.py". Abra um console Python e:


- import random

- result = "".join([random.choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for i in range(50)])

- print(result)


Será necessário também chaves API Paypal (SandBox ou produção): https://developer.paypal.com 