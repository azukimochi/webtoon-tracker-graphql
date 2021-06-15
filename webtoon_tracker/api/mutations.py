from graphene import InputObjectType, Mutation, String, Boolean, List, Field
from . models import Webtoon, Author
from . types import WebtoonNode, AuthorNode
from . mutations_utils import get_valid_authors, get_valid_days_of_release

class AddAuthor(Mutation):
    class Arguments:
        username = String(required=True)
    
    author = Field(AuthorNode)

    @staticmethod
    def mutate(root, info, **arguments):
        print("Karen", arguments)
        new_author = Author(username = arguments['username'])
        new_author.save()

        return AddAuthor(author = new_author)

class NewWebtoonInput(InputObjectType):
    title = String(required=True)
    dropped = Boolean(required=True)
    completed_reading = Boolean(required=True)
    authors = List(String, required=True)
    days_of_release = List(String, required=True)

class AddWebtoon(Mutation):
    class Arguments:
        webtoon_data = NewWebtoonInput(required=True)
    
    webtoon = Field(WebtoonNode)

    @staticmethod
    def mutate(root, info, webtoon_data):
        print("Karen", webtoon_data)
        valid_authors = get_valid_authors(webtoon_data.authors)
        valid_days_of_release = get_valid_days_of_release(webtoon_data.days_of_release)

        new_webtoon = Webtoon(
            title=webtoon_data.title,
            dropped=webtoon_data.dropped,
            completed_reading=webtoon_data.completed_reading,
        )
        new_webtoon.save()
        new_webtoon.authors.add(*valid_authors)
        new_webtoon.days_of_release.add(*valid_days_of_release)
        
        return AddWebtoon(webtoon=new_webtoon)