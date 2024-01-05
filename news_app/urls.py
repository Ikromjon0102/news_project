from django.urls import path
from .views import news_list, homepageview, contactview, aboutview, ContactPageView, sportnewsview, \
    HomePageView, NewsUpdateView, NewsDeleteView, NewsCreateView, localnewsview, news_detail_view, siyosiynewsview, \
    texnonewsview, xorijnewsview

urlpatterns = [
    path('', HomePageView.as_view(), name="home_page"),
    # path('', newstopfive, name="home_page"),
    path('news/', news_list, name="all_news_list"),
    path('news/create/', NewsCreateView.as_view(), name="create_view"),
    path('news/<slug:news>/', news_detail_view, name="news_detail"),
    path('news/<slug>/update/', NewsUpdateView.as_view(), name="update_view"),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name="delete_view"),

    path('contact/', ContactPageView.as_view(), name="contact_page"),
    path('about/', aboutview, name="about_page"),
    path('sport/', sportnewsview, name="sportnews_page"),
    path('local/', localnewsview, name="local_page"),
    path('siyosiy/', siyosiynewsview, name="siyosiy_page"),
    path('texnologiya/', texnonewsview, name="texno_page"),
    path('xorij/', xorijnewsview, name="xorij_page"),
]

