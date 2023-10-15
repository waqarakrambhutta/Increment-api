from django.urls import path,include
from . import views
from counter.views import CounterHistoryView, incrementCounterView


urlpatterns = [
    path('increment/', incrementCounterView.as_view(), name='increment_counter'),
    path('counter-history/', CounterHistoryView.as_view(), name='counter_history'),

]


