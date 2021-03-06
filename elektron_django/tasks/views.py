# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import datetime
from .models import Task, DateTimeTask, DataTask, TaskState, TaskFunction
from devices.models import Device
from django.views import generic
from django.contrib.auth.models import User

def check_device_mac(**kwargs):
    if not 'device_mac' in kwargs:
        return False
    else:
        if type(kwargs['device_mac']) is list:
            kwargs['device_mac'] = kwargs['device_mac'][0]

    return kwargs

def check_task(**kwargs):

    if not 'taskfunction' in kwargs:
        return False
    else:
        if type(kwargs['taskfunction']) is list:
            kwargs['taskfunction'] = kwargs['taskfunction'][0]

    if not 'label' in kwargs:
        return False
    else:
        if type(kwargs['label']) is list:
            kwargs['label'] = kwargs['label'][0]

    if not 'data_value' in kwargs and not 'date_from' in kwargs and not 'date_to' in kwargs:
        return False
    else:
        if 'data_value' in kwargs and type(kwargs['data_value']) is list:
            kwargs['data_value'] = kwargs['data_value'][0]
        elif 'date_from' in kwargs and type(kwargs['date_from']) is list:
            kwargs['date_from'] = kwargs['date_from'][0]
        elif 'date_to' in kwargs and type(kwargs['date_to']) is list:
            kwargs['date_to'] = kwargs['date_to'][0]

    if not 'description' in kwargs:
        return False
    else:
        if type(kwargs['description']) is list:
            kwargs['description'] = kwargs['description'][0]

    if not 'taskstate' in kwargs:
        return False
    else:
        if type(kwargs['taskstate']) is list:
            kwargs['taskstate'] = kwargs['taskstate'][0]

    if not 'taskfunction' in kwargs:
        return False
    else:
        if type(kwargs['taskfunction']) is list:
            kwargs['taskfunction'] = kwargs['taskfunction'][0]

    if not 'owner' in kwargs:
        return False
    else:
        if type(kwargs['owner']) is list:
            kwargs['owner'] = kwargs['owner'][0]

    try:
        kwargs['taskstate'] = TaskState.objects.get(id=kwargs['taskstate'])
    except Exception as e:
        #TODO: create default taskstates in settings.py
        kwargs['taskstate'] = TaskState.objects.get(name="ready")

    try:
        kwargs['taskfunction'] = TaskFunction.objects.get(id=kwargs['taskfunction'])
    except Exception as e:
        #TODO: create default taskfunctions in settings.py
        kwargs['taskfunction'] = TaskFunction.objects.get(name="shutdown")

    try:
        kwargs['owner'] = User.objects.get(username=kwargs['owner'])
    except Exception as e:
        #TODO: create default user in settings.py
        kwargs['owner'] = User.objects.get(username="root")

    return kwargs

class IndexView(generic.ListView):
    model = Task

    def get(self, request, *args, **kwargs):
        """Return all tasks."""
        return JsonResponse({'tasks': list(map(lambda x: x.serialize(), Task.objects.all()))})

class DateTimeTaskIndexView(IndexView):
    model = DateTimeTask

    def get(self, request, *args, **kwargs):
        """Return all date time tasks."""
        return JsonResponse({'datetimetasks': list(map(lambda x: x.serialize(), DateTimeTask.objects.all()))})

class DataTaskIndexView(IndexView):
    model = DataTask

    def get(self, request, *args, **kwargs):
        """Return all data tasks."""
        return JsonResponse({'datatasks': list(map(lambda x: x.serialize(), DataTask.objects.all()))})

class DataTaskDetailView(generic.DetailView):
    model = DataTask

    def get(self, request, *args, **kwargs):
        """Return the selected by id DataTask."""
        try:
            return JsonResponse({'datatasks': DataTask.objects.get(id=kwargs["pk"]).serialize()})
        except Exception as e:
            print "Some error ocurred getting Single DataTask with id: " + str(kwargs["pk"])
            print "Exception: " + str(e)
            return HttpResponse(status=500)

class DateTimeTaskDetailView(generic.DetailView):
    model = DateTimeTask

    def get(self, request, *args, **kwargs):
        """Return the selected by id DateTimeTask."""
        try:
            return JsonResponse({'datetimetasks': DateTimeTask.objects.get(id=kwargs["pk"]).serialize()})
        except Exception as e:
            print "Some error ocurred getting Single DateTimeTask with id: " + str(kwargs["pk"])
            print "Exception: " + str(e)
            return HttpResponse(status=500)

class DatetimeTaskDeviceView(generic.ListView):

    def get(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DateTimeTask.objects.all().filter(device=device_id)

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)

    def post(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DateTimeTask.objects.all()

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)

class DataTaskDeviceView(generic.ListView):

    def get(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DateTimeTask.objects.all().filter(device=device_id)

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)

    def post(self, request, *args, **kwargs):

        result = Device.objects.get(id=kwargs["pk"])
        device_id = result.serialize()["id"]

        if device_id:
            try:
                tasks = DataTask.objects.all()

            except Exception as e:
                print  "Device you ask does not exist"
                print "Exception: " + str(e)
                raise
                return HttpResponse(status=500)

            if tasks:
                try:

                    task_list = list(tasks)
                    task_list = ({'task': list(map(lambda x: x.serialize(), tasks))})

                    return JsonResponse({'device_tasks': task_list})

                except Exception as e:
                    print "Some error ocurred getting Task Device"
                    print "Exception: " + str(e)
                    return HttpResponse(status=500)

class DataTaskCreateView(generic.View):

    def post(self, request, *args, **kwargs):

        result = check_device_mac(**request.POST)

        if result:
            device = Device.objects.get(device_mac=result["device_mac"])

            task = check_task(**request.POST)

            if task:
                try:
                    datatask = DataTask()
                    datatask.description = task["description"]
                    datatask.label = task["label"]
                    datatask.data_value = task["data_value"]
                    datatask.taskstate = task["taskstate"]
                    datatask.taskfunction = task["taskfunction"]
                    datatask.owner = task["owner"]
                    datatask.device = device

                except DataTask.DoesNotExist:
                    datatask = DataTask(**task)

                datatask.save()

            return JsonResponse({'status':True})

class DataTaskUpdateView(generic.View):

    def post(self, request, *args, **kwargs):

        result = check_device_mac(**request.POST)

        if result:
            device = Device.objects.get(device_mac=result["device_mac"])

            task = check_task(**request.POST)

            if task:
                try:
                    datatask = DataTask(pk=kwargs['pk'])
                    datatask.description = task["description"]
                    datatask.label = task["label"]
                    datatask.data_value = task["data_value"]
                    datatask.taskstate = task["taskstate"]
                    datatask.taskfunction = task["taskfunction"]
                    datatask.owner = task["owner"]
                    datatask.device = device
                    datatask.created = datetime.datetime.now()

                except Task.DoesNotExist:
                    datatask = DataTask(**task)

                datatask.save()

            return JsonResponse({'status':True})

class DateTimeTaskCreateView(generic.View):

    def post(self, request, *args, **kwargs):

        result = check_device_mac(**request.POST)

        if result:
            device = Device.objects.get(device_mac=result["device_mac"])

            task = check_task(**request.POST)
            print task

            if task:
                try:
                    datetimetask = DateTimeTask()
                    datetimetask.description = task["description"]
                    datetimetask.label = task["label"]
                    datetimetask.taskstate = task["taskstate"]
                    datetimetask.taskfunction = task["taskfunction"]
                    datetimetask.date_to = task["date_to"]
                    datetimetask.date_from = task["date_from"]
                    datetimetask.owner = task["owner"]
                    datetimetask.device = device

                except DateTimeTask.DoesNotExist:
                    datetimetask = DateTimeTask(**task)

                datetimetask.save()

            return JsonResponse({'status':True})

class DateTimeTaskUpdateView(generic.View):

    def post(self, request, *args, **kwargs):

        result = check_device_mac(**request.POST)

        if result:
            device = Device.objects.get(device_mac=result["device_mac"])

            task = check_task(**request.POST)

            if task:
                try:
                    datetimetask = DateTimeTask()
                    datetimetask.description = task["description"]
                    datetimetask.label = task["label"]
                    datetimetask.taskstate = task["taskstate"]
                    datetimetask.taskfunction = task["taskfunction"]
                    datetimetask.date_to = task["date_to"]
                    datetimetask.date_from = task["date_from"]
                    datetimetask.owner = task["owner"]
                    datetimetask.device = device

                except DateTimeTask.DoesNotExist:
                    datetimetask = DateTimeTask(**task)

                datetimetask.save()

            return JsonResponse({'status':True})
