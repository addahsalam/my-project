from django.db import models
from apps.attendance.models import AttendanceSession

class QRCode(models.Model):
    session = models.OneToOneField(AttendanceSession, on_delete=models.CASCADE, related_name='qr_code')
    code_data = models.TextField()
    qr_image = models.ImageField(upload_to='qrcodes/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"QR Code for {self.session.course.code}"
