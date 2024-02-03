from django.http import JsonResponse

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
