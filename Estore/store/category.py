from CategoryApp.models import Category
def category_list(request):
    """
    Returns a dictionary of categories available to all templates.
    """
    return {
        'categories': Category.objects.all()
    }
