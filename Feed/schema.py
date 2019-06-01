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
        model = Widget


class SourceType(DjangoObjectType):
    class Meta:
        model = Source
        exclude_fields = ('NewsSource', 'TutorialSource',)


class Query(graphene.ObjectType):
    event = graphene.Field(EventType, id=graphene.ID(required=True))

    news = graphene.List(NewsType)
    events = graphene.List(EventType)
    tutorials = graphene.List(TutorialType)
    communities = graphene.List(CommunityType)
    widgets = graphene.List(WidgetType)

    def resolve_event(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Event.objects.get(pk=id)
        return None
