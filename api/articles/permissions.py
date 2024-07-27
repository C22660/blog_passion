from rest_framework.permissions import BasePermission

from blog.articles.models import Article

class ArticleAdministrationPermissions(BasePermission):
    """The article creation or modification is limited to the admin or
    its author"""

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

    def has_object_permission(self, request, view, obj):
        # Si Admin tous pouvoirs
        if request.user.is_staff:
            return True

        author = obj.author
        if request.user == author:
            return True

        return False