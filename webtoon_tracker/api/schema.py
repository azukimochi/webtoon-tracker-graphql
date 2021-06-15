from graphene import ObjectType, Field, Schema
from graphene_django.filter import DjangoFilterConnectionField
from . types import WebtoonNode, AuthorNode
from . mutations import AddAuthor, AddWebtoon

class Mutation(ObjectType):
    add_author = AddAuthor.Field() # Do I really need this mutation?
    add_webtoon = AddWebtoon.Field()

class Query(ObjectType):
    # webtoon = relay.Node.Field(WebtoonNode)
    all_webtoons = DjangoFilterConnectionField(WebtoonNode)

    # author = relay.Node.Field(AuthorNode)
    all_authors = DjangoFilterConnectionField(AuthorNode)

schema = Schema(query=Query, mutation=Mutation)