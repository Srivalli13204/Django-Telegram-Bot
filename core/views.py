from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .tasks import send_welcome_email
from django.core.mail import send_mail

@api_view(['GET'])
def public_api(request):
    return Response({"message": "This is a public endpoint."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_api(request):
    return Response({"message": f"Hello {request.user.username}, this is a protected endpoint."})

@api_view(['POST'])
def trigger_email(request):
    email = request.data.get("email")
    send_welcome_email.delay(email)
    return Response({"status": f"Email sent to {email}!"})

@api_view(['POST'])
def test_email(request):
    email = request.data.get("email")
    try:
        send_mail(
            subject='Test Email',
            message='This is a test email from Django.',
            from_email='isiri1320@gmail.com',
            recipient_list=['isiri132007@gmail.com'],
            fail_silently=False
        )
        return Response({"message": "Email sent successfully."})
    except Exception as e:
        return Response({"error": str(e)})