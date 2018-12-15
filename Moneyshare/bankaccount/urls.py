from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import UserListView, UserchangeListView, AccountCreate

urlpatterns = [
    path('', (UserListView.as_view(template_name='bankaccoount_list.html')), name='article-list'),
    path('change/', (UserchangeListView.as_view(template_name='change_list.html')), name='article-list'),
    path('create/', AccountCreate.as_view(), name='create_account'),
    path('user/abheben/', AccountCreate.as_view(), name='create_account'),
    path('user/einzahlen/', AccountCreate.as_view(), name='create_account'),
    path('user/friendspay/', AccountCreate.as_view(), name='create_account'),
    path('mitarbeiter/einzahlungen/', AccountCreate.as_view(), name='create_account'),
    path('mitarbeiter/bankeröffnung/', AccountCreate.as_view(), name='create_account')
]