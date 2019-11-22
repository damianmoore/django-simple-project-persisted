import os

from django.shortcuts import render_to_response
import redis


def home(request):
    r = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=os.environ.get('REDIS_PORT', 6379), db=os.environ.get('REDIS_DB_NUM', 0))

    visitor_count = int(r.get('visitor_count') or 0)
    if visitor_count:
        r.incr('visitor_count', 1)
        visitor_count += 1
    else:
        r.set('visitor_count', 1)
        visitor_count = 1

    context = {
        'visitor_count': visitor_count,
    }
    return render_to_response('home.html', context)
