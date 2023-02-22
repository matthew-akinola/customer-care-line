from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('contact-us/', views.contact_us, name="contact_us"),
    path('customer-care/post/', views.customer_care_create, name='customer-care'),
    path('logout/', views.logout_view, name="logout"),
    path('login/admin/', views.admin_page, name="admin-page"),
    path('forget_pass/', views.forget_pass, name="forget_pass"),
    path('forget_password/', views.forget_password, name="forget_password"),
    path('registration/', views.registration, name="registration"),
    path('helpline/', views.helpline, name="helpline"),
    # path('helpline_update/', views.helpline_update, name="helpline_update"),
    # path('home/'), 
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)