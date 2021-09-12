from django.urls import path
from . import views
from .views import Detail
app_name='listings'
urlpatterns = [
    path("*aw*/",views.product_list,name='product_list'),
    path("",views.List,name='product_list2'),
    path("add/",views.Add,name='Add'),
    path("about/",views.about,name='About'),
    path("policy/",views.policy,name='policy'),
    path("search/",views.Search,name='search'),
    path("contact/",views.Contact_us,name='contact'),
    path("search_icons/",views.Search_icons,name='search_icons'),
    path("<int:pk>",Detail.as_view(),name='detail'),
    path('<slug:category_slug>',views.product_list,name='product_list_by_category'),
  
]
