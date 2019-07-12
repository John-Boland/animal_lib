import graphene
from graphene_django.types import DjangoObjectType


class NewsType(DjangoObjectType):
    """DjangoObjectType to access the User model."""
    """picture = graphene.String()
    name = graphene.String()

    class Meta:
        model = User

    def resolve_picture(self, *args, **kwargs):
        if self.picture:
            return self.picture.url

        return self.username

    def resolve_name(self, *args, **kwargs):
        if self.name:
            return self.name

        return self.username"""
    count_thread = graphene.Int()

class NewsPaginatedType(graphene.ObjectType):
    objects = graphene.List(NewsType)

class NewsQuery(object):
    """all_users = graphene.List(UserType)
    user = graphene.Field(UserType, id=graphene.Int())

    class Meta:
        model = User

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return User.objects.get(id=id)

        return None
    """
    all_news = graphene.List(NewsType)
