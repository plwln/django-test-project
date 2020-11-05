import graphene
from graphene_django.types import DjangoObjectType
from .models import Occupation
# Occupation.
class OccupationType(DjangoObjectType):
    class Meta:
        model = Occupation
        fields = ("name","company_name","position_name","hire_date","fire_date","salary","fraction","base","advance","by_hours")


class Query(graphene.ObjectType):
    get_occupation = graphene.Field(OccupationType, id=graphene.Int())
    get_occupations = graphene.List(OccupationType)
    hello = graphene.String(description='A typical hello world')  # 3

    def resolve_hello(self, info, **kwargs):  # 4
        return 'World'

    def resolve_get_occupation(self, info, **kwargs):
        id = kwargs.get('id')
        print(id)
        if id is not None:
            return Occupation.objects.get(id=id)
    
    def resolve_get_occupations(self, info, **kwargs):
        return Occupation.objects.all()

class OccupationInput(graphene.InputObjectType):
    name = graphene.String()
    company_name = graphene.String()
    position_name = graphene.String()
    hire_date = graphene.Date()
    fire_date = graphene.Date()
    salary = graphene.Int()
    fraction = graphene.Int()
    base = graphene.Int()
    advance = graphene.Int()
    by_hours = graphene.Boolean()


class AddOccupation(graphene.Mutation):
    ok = graphene.Boolean()
    occupation = graphene.Field(OccupationType)
    class Arguments:
        input = OccupationInput(required=True)

    Output = OccupationType
    
    @staticmethod
    def mutate(root, info, input=None):
        occupation_instance = Occupation(
            name=input.name,
            company_name=input.company_name,
            position_name=input.position_name,
            hire_date=input.hire_date,
            fire_date=input.fire_date,
            salary=input.salary,
            fraction=input.fraction,
            base=input.base,
            advance=input.advance,
            by_hours=input.by_hours)
        occupation_instance.save()
        return occupation_instance

class Mutation(graphene.ObjectType):
    add_occupation = AddOccupation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
