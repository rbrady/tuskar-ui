# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

# FIXME: configuration for dummy data
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Capacity(models.Model):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    name = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    unit = models.CharField(max_length=10)


class Alert(models.Model):
    class Meta:
        db_table = 'infrastructure_alerts'

    object_id = models.CharField(max_length=50)
    object_type = models.CharField(max_length=20)
    message = models.CharField(max_length=250)
    time = models.DateTimeField()


class FlavorTemplate(models.Model):
    class Meta:
        db_table = 'infrastructure_flavortemplate'

    name = models.CharField(max_length=50, unique=True)
    capacities = generic.GenericRelation(Capacity)


class Node(models.Model):
    class Meta:
        db_table = 'infrastructure_node'

    name = models.CharField(max_length=50, unique=True)
    rack_id = models.PositiveIntegerField(null=True)
    mac_address = models.CharField(max_length=50, unique=True)
    ip_address = models.CharField(max_length=50, unique=True, null=True)
    status = models.CharField(max_length=50, null=True)
    usage = models.IntegerField(max_length=50, null=True)
    capacities = generic.GenericRelation(Capacity)
