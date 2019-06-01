from django.db.models import Count
import graphene
from graphene_django.types import DjangoObjectType
from django.db.models import Q

from .models import *


class NewsType(DjangoObjectType):
    class Meta:
        model = News


class EventType(DjangoObjectType):
    class Meta:
        model = Event


class TutorialType(DjangoObjectType):
    class Meta:
        model = Tutorial


class CommunityType(DjangoObjectType):
    class Meta:
        model = Community


class WidgetType(DjangoObjectType):
    class Meta:
        model = Community


class Query(graphene.ObjectType):
    news = graphene.List(NewsType)
    events = graphene.List(EventType)
    tutorials = graphene.List(TutorialType)
    communities = graphene.List(CommunityType)
    widget = graphene.List(WidgetType)