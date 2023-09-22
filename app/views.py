from rest_framework import viewsets
from rest_framework.response import Response
import django_eventstream
import django_rq

class TestMainViewSet(viewsets.ViewSet):
    def list(self, request):
        print('Sending an event with value: main')
        data = {'message': 'Sending a event with value: main'}
        django_eventstream.send_event('test', 'message', 'main')
        return Response(data)

def test_job():
    print('Sending an event with value: worker')
    django_eventstream.send_event('test', 'message', 'worker')

class TestWorkerViewSet(viewsets.ViewSet):
    def list(self, request):
        print('Will send an event with value: worker')
        queue = django_rq.get_queue('default')
        queue.enqueue(test_job)
        data = {'message': 'Sending a event with value: worker'}
        return Response(data)