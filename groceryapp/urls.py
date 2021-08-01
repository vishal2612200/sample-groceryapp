from django.urls import path
from .views import register_request, login_request, homepage,\
                     update_form, add_form, logout_request, delete_form

app_name = "groceryapp"   


urlpatterns = [
    path("", homepage, name="homepage"),
    path("register/", register_request, name="register"),
    path("login/", login_request, name="login"),
    path("add/", add_form, name="add"),
    path("update/<grocery_id>/", update_form, name="update"),
    path("delete/<grocery_id>/", delete_form, name="delete"),
    path("logout/", logout_request, name="logout"),
]
