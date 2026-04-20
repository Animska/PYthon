from .forms import ProductForm

def add_product_form(request):
    return {
        'add_product_form': ProductForm()
    }
