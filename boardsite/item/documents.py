from django.contrib.auth.models import User
from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from .models import Item, Category


@registry.register_document
class CategoryDocument(Document):
    id = fields.IntegerField()

    class Index:
        name = 'categories'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Category
        fields = [
            'name',
        ]

@registry.register_document
class ItemDocument(Document):
    category = fields.ObjectField(properties={
        'id': fields.IntegerField(),
        'name': fields.TextField(),
    })
    type = fields.TextField(attr='type_to_string')

    class Index:
        name = 'items'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }

    class Django:
        model = Item
        fields = [
            'name',
            'description',
        ]


