from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView

from news_project.custom_permissions import OnlyLoggedSuperUser
from .models import News, Category
from .forms import ContactForm, CommentForm


def news_list(request):
    # news_list = News.objects.filter(status = News.Status.Published)
    news_list = News.published.all()

    context = {
        'news_list': news_list
    }

    return render(request,'news/news_list.html',context)


# @login_required()
def news_detail_view(request,news):
    news = get_object_or_404(News, slug = news, status = News.Status.Published)
    comments = news.comments.filter(active=True)
    new_comment = None
    comment_count = len(comments)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=False)
            new_comment.news = news
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()



    else:
        comment_form = CommentForm()


    context = {
        "news" : news,
        'comments' : comments,
        'new_comment': new_comment,
        'comment_form' : comment_form,
        'comment_count' : comment_count,
    }

    return render(request,"news/news_detail.html",context)

def homepageview(request):
    news = News.objects.filter(status = News.Status.Published).order_by('-publish_time')[6]
    news_rec = News.published.all().order_by('-publish_time')[:5]
    local_one = News.objects.filter(category__name='Mahalliy').order_by('-publish_time')[0]
    local_news = News.objects.filter(category__name='Mahalliy').order_by('-publish_time')[1:6]

    categories = Category.objects.all()


    context = {
        "news" : news,
        "news_rec" : news_rec,
        'local_news' : local_news,
        'local_one' : local_one,
        'categories' : categories
    }
    return render(request, 'news/home.html',context)

class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['news'] = News.objects.filter(status = News.Status.Published).order_by('-publish_time')[:10]
        context['news_rec'] = News.published.all().order_by('-publish_time')[:5]
        context['local_news'] = News.published.filter(category__name = 'Mahalliy').order_by('-publish_time')[:5]
        context['global_news'] = News.published.filter(category__name = 'Xorij').order_by('-publish_time')[:5]
        context['techno_news'] = News.published.filter(category__name = 'Texnologiya').order_by('-publish_time')[:5]
        context['sport_news'] = News.published.filter(category__name = 'Sport').order_by('-publish_time')[:5]

        return context
def contactview(request):
    form = ContactForm(request.POST)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur</h2>")

    context = {
        'form' : form
    }
    return render(request,'news/contact.html',context)
def aboutview(request):
    context = {

    }
    return render(request,'news/about.html',context)


def sportnewsview(request):
    # news = News.objects.filter(category = Category.name.Sport)
    sport_news = News.objects.filter(category__name='Sport')
    context = {
        'news' : sport_news
    }
    return render(request, 'news/sport.html', context)
def localnewsview(request):
    # news = News.objects.filter(category = Category.name.Sport)
    local_news = News.objects.filter(category__name='Mahalliy')
    context = {
        'news' : local_news
    }
    return render(request, 'news/local.html', context)

def texnonewsview(request):
    # news = News.objects.filter(category = Category.name.Sport)
    local_news = News.objects.filter(category__name='Texnologiya')
    context = {
        'news' : local_news
    }
    return render(request, 'news/techno.html', context)

def siyosiynewsview(request):
    # news = News.objects.filter(category = Category.name.Sport)
    local_news = News.objects.filter(category__name='Siyosat')
    context = {
        'news' : local_news
    }
    return render(request, 'news/siyosiy.html', context)

def xorijnewsview(request):
    # news = News.objects.filter(category = Category.name.Sport)
    local_news = News.objects.filter(category__name='Xorij')
    context = {
        'news' : local_news
    }
    return render(request, 'news/xorij.html', context)


def jamiyat_view(request):
    jamiyat_news = News.objects.filter(category__name = 'Jamiyat')

    context = {
        "news":jamiyat_news
    }

    return render(request, 'news/jamiyat.html', context)


class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request,'news/contact.html',context)

    def post(self, request, *args,**kwargs ):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur</h2>")
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)


class NewsUpdateView(OnlyLoggedSuperUser, UpdateView):
    model = News
    fields = ('title','body','category','status')
    template_name = 'crud/update.html'

class NewsCreateView(OnlyLoggedSuperUser,  CreateView):
    model = News
    fields = ('title','slug','image','body','category','status')
    template_name = 'crud/create.html'



class NewsDeleteView(OnlyLoggedSuperUser, DeleteView):
    model = News
    template_name = 'crud/detele.html'
    success_url = reverse_lazy('home_page')


class SearchResultsList(ListView):
    model = News
    template_name = 'news/search_results.html'
    context_object_name = 'barcha_yangiliklar'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return News.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

