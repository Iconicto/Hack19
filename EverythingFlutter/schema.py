import graphene
import Feed.schema


class Query(Feed.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
