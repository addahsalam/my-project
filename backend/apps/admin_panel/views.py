from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from apps.users.models import UserProfile
from apps.courses.models import Course
from apps.attendance.models import AttendanceSession, Attendance

def is_admin(user):
    return user.is_staff or (hasattr(user, 'profile') and user.profile.role == 'admin')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    context = {
        'total_users': UserProfile.objects.count(),
        'total_courses': Course.objects.count(),
        'total_sessions': AttendanceSession.objects.count(),
        'total_attendance': Attendance.objects.count(),
    }
    return render(request, 'admin_panel/dashboard.html', context)
