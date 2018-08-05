import graphene
from model import EnglishBot


class Query(graphene.ObjectType):
    chat = graphene.String(msg=graphene.String(), description='A typical hello world')

    def resolve_chat(self, info, msg):
        return str(EnglishBot.get_response(msg))


class Mutation(graphene.ObjectType):
    learn = graphene.String(body=graphene.List(graphene.String))

    def resolve_learn(self, info, body):
        return str(EnglishBot.train(body))


schema = graphene.Schema(query=Query, mutation=Mutation)
