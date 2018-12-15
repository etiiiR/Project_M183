from django.urls import path
from django.contrib.auth.decorators import login_required, permission_required
from .views import UserListView, UserchangeListView, AccountCreate, SignUp, Friendspay, abheben

urlpatterns = [
    path('', (UserListView.as_view(template_name='bankaccoount_list.html')), name='article-list'),
    path('change/', (UserchangeListView.as_view(template_name='change_list.html')), name='article-list'),
    path('create/', AccountCreate.as_view(), name='create_account'),
    path('user/abheben/<int:pk>', abheben.as_view(), name='create_account'),
    path('user/einzahlen/', AccountCreate.as_view(), name='create_account'),
    path('user/friendspay/', Friendspay.as_view(template_name='user_friendspay.html'), name='friendspay'),
    path('mitarbeiter/einzahlungen/', AccountCreate.as_view(), name='create_account'),
    path('mitarbeiter/bankeröffnung/', (AccountCreate.as_view(template_name='mitarbeiter_bankeröffnung.html', success_url="/app/")), name='Kontoeröffnen'),
    path('mitarbeiter/accounteröffnen/', (SignUp.as_view(template_name='mitarbeit_accounteröffnen.html', success_url="/app/")), name='Kontoeröffnen'),
]