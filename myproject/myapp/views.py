from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
import os

@csrf_exempt
def index(request):
    """
    Main page view
    """
    endpoints = {
        "endpoints": {
            "/": "Main page with info ",
            "(GET) entity":"Display list of them",
            "(GET) entity/:id":"One entity profile",
            "entity/":"Post method to create new one via postman and push in data.",
            "entity/:id":"Delete method to remove one from data."
        }
    }
    return JsonResponse(endpoints)

@csrf_exempt
def create_entity(request):
    """
    Create a new entity via POST request and save data in JSON file
    """
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('username', None)
            email = data.get('email', None)
            password = data.get('password', None)

            if username and email and password:
                entity = {
                    'username': username,
                    'email': email,
                    'password': password
                }
                save_entity_to_json(entity)
                return JsonResponse({'message': 'Entity created successfully'}, status=201)
            else:
                return JsonResponse({'error': 'Missing parameters'}, status=400)
        else:
            return JsonResponse({'error': 'Only POST method allowed'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def save_entity_to_json(entity):
    """
    Save entity data to a JSON file
    """
    file_path = '/Users/zakerden1234/Desktop/Web-Development-HW6-Kolomiiets-/myproject/users.json'
    mode = 'a' if os.path.exists(file_path) else 'w'
    with open(file_path, mode) as f:
        json.dump(entity, f)
        f.write('\n')
