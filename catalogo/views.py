from django.shortcuts import get_object_or_404, render
from .models import Category, Product
from django.views.generic import ListView

class ProductList(ListView):
    model = Product
    template_name = 'catalogo/product_list.html'
    paginate_by = 3


class CategoryView(ListView):
    template_name = 'catalogo/category.html'
    paginate_by = 3

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {'product': product}
    return render(request, 'catalogo/product.html', context)



