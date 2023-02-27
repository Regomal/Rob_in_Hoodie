from django.shortcuts import render
from django.urls import reverse
from apps.blog.forms import CommentFormLogin
from apps.blog.models import BlogCategory, Article, Tag, CommentArticle


def blog_category_list(request):
    blog_categories = BlogCategory.objects.all()
    breadcrumbs = {'current': 'Блог'}
    return render(request, 'blog/category_list.html', {"categories": blog_categories, "breadcrumbs": breadcrumbs})


def article_list(request, category_id):
    articles = Article.objects.filter(category_id=category_id)
    category = BlogCategory.objects.get(id=category_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        'current': category.name
    }
    return render(
        request,
        'blog/article_list.html',
        {'articles': articles, 'category': category, 'breadcrumbs': breadcrumbs}
    )


def article_view(request, category_id, article_id):
    category = BlogCategory.objects.get(id=category_id)
    article = Article.objects.get(id=article_id)
    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        reverse('blog_article_list', args=[article.category_id]): article.category,
        reverse('blog_article_view', args=[article.category_id, article_id]): article.title,
        'current': 'Добавление комментария'
    }
    if request.method == "POST":
        data = request.POST.copy()
        data.update(article=article)
        if request.user.is_authenticated:
            data.update(is_checked=True, email=request.user.email, username=request.user.username)
        request.POST = data
        form = CommentFormLogin(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/comment_created.html', {'article': article, 'breadcrumbs': breadcrumbs})
    comments = CommentArticle.objects.filter(article=article)

    breadcrumbs = {
        reverse('blog_category_list'): 'Блог',
        reverse('blog_article_list', args=[article.category_id]): article.category,
        'current': article.title
    }
    return render(request,
                  'blog/article_view.html',
                  {
                      'category': category,
                      'article': article,
                      'breadcrumbs': breadcrumbs,
                      'comments': comments
                  }
                  )


def tag_article(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    articles = Article.objects.filter(tags__name__icontains=tag.name)
    breadcrumbs = {reverse('blog_category_list'): 'Блог', 'current': f"#{tag.name}"}
    return render(request, 'blog/tag_article.html', {'articles': articles, 'tag': tag, 'breadcrumbs': breadcrumbs})
