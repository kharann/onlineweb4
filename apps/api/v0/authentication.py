# -*- coding: utf-8 -*-

from tastypie.resources import ModelResource

from apps.authentication.models import OnlineUser as User


class UserResource(ModelResource):

    class Meta(object):
        queryset = User.objects.all()
        resource_name = 'user'
        fields = ['username', 'first_name', 'last_name', 'email', ]
