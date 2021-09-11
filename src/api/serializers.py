# -*- coding: utf-8 -*-

from rest_framework import serializers

from src.todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            "name",
            "complete",
        )
