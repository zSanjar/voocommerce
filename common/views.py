from django.views.generic import TemplateView

from products.models import Category



class HomeView(TemplateView):
    template_name = 'index.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        categories = Category.objects.all()
        
        context['title'] = 'VooCommerce'
        context['categories'] = categories
        # print(categories[1].image.url)
        return  context
    

class ContactView(TemplateView):
    template_name = 'contact.html'
    
    def get_contact_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'VooComerce | Contact Us'
        return context