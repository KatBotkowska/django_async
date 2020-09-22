from django.http import HttpResponse

async def index(request):
    return HttpResponse('Hello, I\'ve just checked how it works')
