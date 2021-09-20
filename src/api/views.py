# -*- coding: utf-8 -*-

import json

from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404

# from rest_framework import permissions, serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from src.api.serializers import TaskSerializer
from src.todo.models import Task


class LoginAPI(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "status": "success",
                    "token": token.key,
                    "user_id": user.pk,
                    "email": user.email,
                }
            )
        else:
            return Response(
                {"status": "error", "message": "Username or password is incorrect"}
            )


class TaskListAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        datas = [
            {"id": task.id, "name": task.name, "complete": task.complete}
            for task in Task.objects.filter(user=request.user)
        ]
        return Response({"status": "success", "datas": datas})


class TaskCreateAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            print("Serializer is valid")
            task = serializer.save(user=request.user)
            return Response(
                {
                    "status": "success",
                    "data": {
                        "id": task.id,
                        "name": task.name,
                        "date": task.date,
                        "complete": task.complete,
                    },
                }
            )
        return Response({"status": "error", "message": "Can't create task"})


class TaskDeleteAPI(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = request.data
        task = get_object_or_404(Task, id=data["id"])
        task.delete()
        return Response({"status": "success"})
