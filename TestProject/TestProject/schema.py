import graphene
import TestApp.schema
class Query(TestApp.schema.Query, graphene.ObjectType):
    pass
class Mutation(TestApp.schema.Mutation, graphene.ObjectType):
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)