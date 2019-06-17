from django.views.generic import TemplateView, FormView, CreateView
from catalogo.models import Category
from .forms import Form
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy, reverse

User = get_user_model()

class Index(TemplateView):
    template_name = 'index.html'
    extra_context = {
        'title': 'Django e-commerce',
        'texts': ['Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent convallis gravida leo at dapibus. '
                 'Nunc non nulla lobortis sem vulputate rhoncus. Quisque et neque vitae ex vulputate ultricies. '
                 'Nunc augue massa, porttitor ut dolor vitae, ullamcorper viverra ligula. Nullam hendrerit mi quis lacus efficitur venenatis.'
                ],
        'categories': Category.objects.all()

    }

class Contato(FormView):
    template_name = 'contact.html'
    form_class = Form

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            return self.form_invalid(form)

    def form_valid(self, request, form):
        if form.is_valid:
            form.save(commit=True)
        return super().form_valid(form)

    def get_success_url(self):
        return HttpResponseRedirect('/')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    model = User
    success_url = reverse_lazy('login')
