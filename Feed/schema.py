from django.db.models import Count
import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Q

from .models import *


class Query(graphene.ObjectType):
    pass
