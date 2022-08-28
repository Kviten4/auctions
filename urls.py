from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createnewlot", views.newlot, name="newlot"),
    path("categories", views.categories, name="categories"),
    path("categories/<str:title>", views.catview, name="catview"),
    path("lot<int:lotID>", views.lotpage, name="lotpage"),
    path("watchlist", views.mywatchlist, name="mywatchlist"),
]
