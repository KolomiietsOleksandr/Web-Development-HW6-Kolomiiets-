from django.http import JsonResponse
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
import os
import uuid

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
def entity(request):
    """
    Handle both GET and POST requests for /entity/ endpoint
    """
    if request.method == 'GET':
        return list_entities(request)
    elif request.method == 'POST':
        return create_entity(request)
    else:
        return HttpResponseBadRequest("Unsupported method")

@csrf_exempt
def entity_id(request, entity_id):
    """
    Handle both GET and POST requests for /entity/id endpoint
    """
    if request.method == 'GET':
        return get_entity_by_id(request, entity_id)
    elif request.method == 'DELETE':
        return delete_entity(entity_id)
    else:
        return HttpResponseBadRequest("Unsupported method")

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
                entity_id = str(uuid.uuid4())
                entity = {
                    'id': entity_id,
                    'username': username,
                    'email': email,
                    'password': password
                }
                save_entity_to_json(entity)
                return JsonResponse({'message': 'Entity created successfully', 'id': entity_id}, status=201)
            else:
                return JsonResponse({'error': 'Missing parameters'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def save_entity_to_json(entity):
    """
    Save entity data to a JSON file
    """
    file_path = '/Users/zakerden1234/Desktop/Web-Development-HW6-Kolomiiets-/myproject/users.json'
    mode = 'a' if os.path.exists(file_path) else 'w'
    with open(file_path, mode) as f:
        json.dump(entity, f)
        f.write('\n')

@csrf_exempt
def get_entity_by_id(request, entity_id):
    """
    Get an entity profile by ID
    """
    try:
        if request.method == 'GET':
            entity = get_entities_from_json(entity_id)
            print(entity_id)
            if entity:
                return JsonResponse(entity, safe=False)
            else:
                return JsonResponse({'error': 'Entity not found'}, status=404)
        else:
            return JsonResponse({'error': 'Only GET method allowed'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def list_entities(request):
    """
    Display a list of entities via GET request
    """
    try:
        if request.method == 'GET':
            entities = get_entities_from_json(None)
            return JsonResponse(entities, safe=False)
        else:
            return JsonResponse({'error': 'Only GET method allowed'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def get_entities_from_json(entity_id):
    """
    Fetch entities from a JSON file
    """
    with open('/Users/zakerden1234/Desktop/Web-Development-HW6-Kolomiiets-/myproject/users.json') as f:
        if entity_id == None:
            entities = [json.loads(line) for line in f]
            return entities
        else:
            entities = [json.loads(line) for line in f]
            for entity in entities:
                if entity.get('id') == str(entity_id):
                    print('2')
                    return entity

@csrf_exempt
def delete_entity(entity_id):
    """
    Delete an entity by ID
    """
    try:
        file_path = '/Users/zakerden1234/Desktop/Web-Development-HW6-Kolomiiets-/myproject/users.json'

        updated_entities = []
        with open(file_path, 'r') as f:
            for line in f:
                entity = json.loads(line)
                if entity.get('id') != str(entity_id):
                    updated_entities.append(entity)

        with open(file_path, 'w') as f:
            for entity in updated_entities:
                json.dump(entity, f)
                f.write('\n')

        return JsonResponse({'message': 'Entity deleted successfully'})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
