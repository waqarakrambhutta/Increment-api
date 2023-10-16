from django.urls import path,include
from . import views
from counter.views import CounterHistoryView, incrementCounterView
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('counterhistory', views.CounterHistoryView, basename='counterhistory')



urlpatterns = [
    path('increment/', incrementCounterView.as_view(), name='increment_counter'),
    # path('counter-history/', CounterHistoryView.as_view(), name='counter_history'),

]+router.urls


