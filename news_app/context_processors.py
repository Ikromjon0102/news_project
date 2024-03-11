from news_app.models import Category
from news_app.models import News


def latest_news(request):
    latest_news = News.published.all().order_by('-publish_time')[:10]
    categories = Category.objects.all()
    context = {
        "latest_news": latest_news,
        "categories": categories
    }

    return context