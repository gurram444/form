from django.urls import path
from sample.views import Home,form1,form2,form3

urlpatterns = [
                  path('', Home.as_view()),
                  path('form1',form1.as_view()),
    path('form2',form2.as_view()),
    path('form3',form3.as_view()),
]