from tastypie.resources import ModelResource
from tastypie import fields
from models import Note

class NoteResource(ModelResource):
    children = fields.ToManyField('self', 'children', null=True)
    parent = fields.ToOneField('self', 'parent', null=True)
    class Meta:
        queryset = Note.objects.all()
