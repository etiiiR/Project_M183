from lib2to3.fixes.fix_input import context
import logging

logger = logging.getLogger(__name__)
from .models import Bankaccoount
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Permission, User
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from ipware import get_client_ip


@method_decorator(login_required, name='dispatch')
class abheben(PermissionRequiredMixin, ListView):
    permission_required = 'bankaccount.can_see_bankaccount'



@method_decorator(login_required, name='dispatch')
class UserListView(PermissionRequiredMixin, ListView):
    permission_required = 'bankaccount.can_see_bankaccount' 
    model = Bankaccoount
    template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'object_list'  # Default: object_list
    paginate_by = 10
    queryset = Bankaccoount.objects.all()
    logger.info("Log of Queryset in UserlistView %s", queryset)



@method_decorator(login_required, name='dispatch')
class UserchangeListView(PermissionRequiredMixin, ListView):
    permission_required = 'bankaccount.can_change_bankaccount' 
    model = Bankaccoount
    template_name = 'core/user_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'object_list'  # Default: object_list
    paginate_by = 10
    queryset = Bankaccoount.objects.all()
    logger.info("Log of Queryset in UserchangeListView %s", queryset)
    
@method_decorator(login_required, name='dispatch')
class AccountCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'bankaccount.can_change_bankaccount' 
    model = Bankaccoount
    fields = ['Money', 'User']
    logger.info("Account Created", fields)
         