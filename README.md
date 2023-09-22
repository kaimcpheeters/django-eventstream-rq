When I call  `django_eventstream.send_event` directly from a view the event gets sent (main).

However, when I call  `django_eventstream.send_event` from a django RQ enqueued function the event never gets sent (worker).

```
from rest_framework import viewsets
from rest_framework.response import Response
import django_eventstream
import django_rq

class TestMainViewSet(viewsets.ViewSet):
    def list(self, request):
        data = {'message': 'Sending a event with value: main'}
        django_eventstream.send_event('test', 'message', 'main')
        return Response(data)

def test_job():
    django_eventstream.send_event('test', 'message', 'worker')

class TestWorkerViewSet(viewsets.ViewSet):
    def list(self, request):
        queue = django_rq.get_queue('default')
        queue.enqueue(test_job)
        data = {'message': 'Sending a event with value: worker'}
        return Response(data)
```

This might be a related issue https://github.com/django/channels/issues/1302

requirements.txt
```
Django==4.2.1
djangorestframework==3.14.0
channels==3.0.5
django-eventstream==4.5.1
django-rq==2.8.1
```

Are there any known reasons for why django_eventstream doesn't work with django-rq? Is there a work around?


## Replicate with Docker

```bash
docker-compose up
```

Your Django application is now available at `http://localhost:8000`.

Streaming endpoint is now available at `http://localhost:8000/streaming/`.


