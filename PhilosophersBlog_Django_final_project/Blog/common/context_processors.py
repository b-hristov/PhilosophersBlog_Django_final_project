from PhilosophersBlog_Django_final_project.Blog.main.models import Category


def categories(request):
    return {'categories': Category.objects.all()}
