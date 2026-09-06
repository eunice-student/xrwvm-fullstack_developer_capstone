from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Already Registered"}, status=400)
        
        # Create new user
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        
        # Log user in
        login(request, user)
        
        return JsonResponse({"userName": username, "status": "Authenticated"})
    
    return JsonResponse({"error": "Invalid request method"}, status=405)
