from django.conf.urls import url, include
from users.views import dashboard, register, home

urlpatterns = [
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^oauth/", include("social_django.urls")),
    url(r"^register/", register, name="register"),
    url(r'^auth/', home, name="home")

]
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = 'home'
