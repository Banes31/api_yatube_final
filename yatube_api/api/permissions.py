from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthoredOrReadOnly(BasePermission):
    """
    Permission.
    Который проверяет является ли пользователь автором поста или комментария,
    а также какой метод запроса применен к эндпоинту.
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.method in SAFE_METHODS
