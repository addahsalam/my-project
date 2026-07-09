from rest_framework import serializers
from .models import AttendanceSession, Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['id', 'session', 'student', 'scanned_at']

class AttendanceSessionSerializer(serializers.ModelSerializer):
    attendances = AttendanceSerializer(many=True, read_only=True)
    
    class Meta:
        model = AttendanceSession
        fields = ['id', 'course', 'session_date', 'created_by', 'is_active', 'attendances', 'created_at']
