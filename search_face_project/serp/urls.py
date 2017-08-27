import views
from django.conf.urls import url
from serp.views import SearchView, GotoView, LogView, ResultsView

urlpatterns = [
    url(r'^$', SearchView.as_view()),
    url(r'^search/$', SearchView.as_view(), name='serp-search'),
    url(r'^goto/$', GotoView.as_view(), name='serp-goto'),
    url(r'^log/$', LogView.as_view(), name='serp-log'),
    url(r'^results/$', ResultsView.as_view(), name='serp-results'),


]