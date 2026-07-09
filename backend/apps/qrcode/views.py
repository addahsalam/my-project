from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.files.base import ContentFile
import qrcode
from io import BytesIO
from .models import QRCode
from .serializers import QRCodeSerializer
from apps.attendance.models import AttendanceSession

class QRCodeViewSet(viewsets.ModelViewSet):
    queryset = QRCode.objects.all()
    serializer_class = QRCodeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['post'])
    def generate(self, request):
        session_id = request.data.get('session_id')
        
        try:
            session = AttendanceSession.objects.get(id=session_id)
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(str(session.id))
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            
            img_io = BytesIO()
            img.save(img_io, format='PNG')
            img_io.seek(0)
            
            qr_code = QRCode.objects.create(
                session=session,
                code_data=str(session.id),
            )
            qr_code.qr_image.save(
                f'qrcode_{session.id}.png',
                ContentFile(img_io.getvalue())
            )
            
            serializer = QRCodeSerializer(qr_code)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except AttendanceSession.DoesNotExist:
            return Response({'error': 'Session not found'}, status=status.HTTP_404_NOT_FOUND)
