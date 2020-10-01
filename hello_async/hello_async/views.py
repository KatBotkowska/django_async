from django.http import HttpResponse
import asyncio
from time import sleep
import httpx




#helpers
async def http_call_async():
    for num in range(1,6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)

def http_call_sync():
    for num in range(1,6):
        sleep(1)
        print(num)
    r = httpx.get("https://httpbin.org/")
    print(r)
async def smoke(smokables: List[str] = None, flavor: str='Sweet Baby ray\'s')->List[str]:
    for smokable in smokables:
        print(f'Smoking some {smokable}...')
        print(f'Appying the {flavor}...')
        print(f'{smokable.capitalize()} smoked')

return len(smokables)
#views

async def index(request):
    return HttpResponse('Hello, I\'ve just checked how it works')

async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('non-blocking http response')

def sync_view(request):
    http_call_sync()
    return HttpResponse('blocking http request')