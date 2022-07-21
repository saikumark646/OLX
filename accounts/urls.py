from django.urls import path
#from django.contrib.auth import login

from django.contrib.auth import views as auth_views


app_name = 'accounts'

urlpatterns = [
    #path('login/', login ,  {'template_name':'accounts/registration/login.html'}, name = 'name')
    # path('login/',auth_views.LoginView.as_view() , name = 'login'),
    # #path('logout/',auth_views.LogoutView.as_view() , name = 'logout'),
    # path('password_change/',auth_views.PasswordChangeView.as_view() , name = 'password_change'),
    # path('password_change/done/',auth_views.PasswordChangeDoneView.as_view() , name = 'password_change_done'),
    # path('password_reset/',auth_views.PasswordResetView.as_view() , name = 'password_reset'),
    # path('password_reset/done/',auth_views.PasswordResetDoneView.as_view() , name = 'password_reset_done')

]
