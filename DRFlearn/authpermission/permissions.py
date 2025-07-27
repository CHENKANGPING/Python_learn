from rest_framework import permissions

class MyPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.META.get('HTTP_REFERER'):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if '长沙' in obj.name:
            return True
        else:
            return False