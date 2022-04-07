from django.shortcuts import render
from django.views.generic import TemplateView,ListView,FormView
from .forms import ContactForm
from django.urls import reverse_lazy

# Create your views here.

class Home(FormView):
    template_name = "home.html"
    form_class = ContactForm
    success_url = reverse_lazy('blog_app:success')
    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)
    

'''class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)'''

'''class About(TemplateView):
    template_name = "about.html"'''

class About(TemplateView):
    template_name = "about.html"
    


class ContactSuccessView(TemplateView):
    template_name = 'success.html'