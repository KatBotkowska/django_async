from asgiref.sync import sync_to_async
from django.http import HttpResponse
import asyncio
from time import sleep
from typing import List
import httpx
import random




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

async def get_smokables():
    print('Getting smokables...')

    await asyncio.sleep(2)
    async with httpx.AsyncClient() as client:
        await client.get('https://httpbin.org')

        print('returning smokeable')
        return [
            'ribs',
            'brisket',
            'lemon chicken',
            'salmon',
            'bison sirloin',
            'sausage'
        ]

async def get_flavor():
    print('getting flavor...')

    await asyncio.sleep(1)
    async with httpx.AsyncClient() as client:
        await client.get('https://httpbin.org')

        print('returning flavor')
        return random.choice(
            [
                'sweet baby ray\'s'
                'stubbs original',
                'famous dave',
            ]
        )
def oversmoke() ->None:
    sleep(5)
    print('who doesn\'t like burnt meals?')

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

async def smoke_some_meats(request):
    results = await asyncio.gather(*[get_smokables(), get_flavor()])
    total = await asyncio.gather(*[smoke(results[0], results[1])])
    return HttpResponse(f'smoked {total[0]} meats with {results[1]}!')

async def burn_some_meats(request):
    oversmoke()
    return HttpResponse('I have burned some meats')


async def async_with_sync_view(request):
    loop =asyncio.get_event_loop()
    async_function = sync_to_async(http_call_sync)
    loop.create_task(async_function())
    return HttpResponse('non blocking HTTP request via sync to async')

