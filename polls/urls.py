# coding:utf-8

from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex:/polls/
    url('^$', views.IndexView.as_view(), name='index'),

    # ex: /polls/5
    url('(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # ex:/polls/5/results
    url('(?P<pk>[0-9]+)/results/', views.ResultView.as_view(), name='results'),

    # ex:/polls/5/vote
    url('(?P<question_id>[0-9]+)/vote/', views.vote, name='vote')

]
