from rest_framework import permissions
from rest_framework.exceptions import NotFound

class IsStaffOnly(permissions.BasePermission):
    """Allows only staff users to access."""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'staff'

class IsStaffOrGuardianReadOnly(permissions.BasePermission):
    """Allows staff and guardians read-only access. Staff has full access."""
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS and request.user.is_authenticated or request.user.role == 'staff'

class HomeworkAccessPermission(permissions.BasePermission):
    """Restricts homework visibility for guardians. Staff has full access."""
    def has_object_permission(self, request, view, obj):
        if request.user.role == 'staff':
            return True

        if request.user.role == 'guardian':
            # Correct way to access related students (using related_name)
            student_classes = request.user.students.values_list('class_id', flat=True)

            if obj.class_id in student_classes:
                return True
            raise NotFound()  # Raise NotFound if not related to guardian

        return False  # Or return a 403 if you prefer not to reveal existence