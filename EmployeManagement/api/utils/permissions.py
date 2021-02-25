from rest_framework.permissions import BasePermission, DjangoObjectPermissions
from django.contrib.auth.models import Group, Permission

class AccountsManagementPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser or request.user.groups.filter(name='Manager').exists():
            return True
        return False