from graphene import relay
from graphene_django import DjangoObjectType
from . models import Webtoon, Author, DayOfRelease

class WebtoonNode(DjangoObjectType):
    class Meta:
        model = Webtoon
        filter_fields = {
            'title': ['exact', 'icontains', 'istartswith'],
            'dropped': ['exact'],
            'completed_reading': ['exact'],
            'authors': ['exact'],
            'days_of_release': ['exact'],
            }
        interfaces = (relay.Node, )

class AuthorNode(DjangoObjectType):
    class Meta:
        model = Author
        filter_fields = {
            'username': ['exact', 'icontains', 'istartswith']
        }
        interfaces = (relay.Node, )

class DayOfReleaseNode(DjangoObjectType):
    class Meta:
        model = DayOfRelease
        filter_fields = {
            'day_of_week': ['exact']
        }
        interfaces = (relay.Node, )