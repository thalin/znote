from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.dates import ArchiveIndexView
from models import Note

class NoteList(ListView):
    queryset = Note.objects.filter(parent=None)

class NoteDetail(DetailView):
    queryset = Note.objects.all()

class NoteCreate(CreateView):
    queryset = Note.objects.all()
    template_name = 'znote/note_create.html'

    def get_initial(self):
        title = self.request.GET.get('title', '')
        return {'parent': None, 'text': '', 'title': title}

class NoteCreateChild(CreateView, DetailView):
    queryset = Note.objects.all()
    template_name = 'znote/note_create.html'

    def get_context_data(self, *args, **kwargs):
        detail_context = super(DetailView, self).get_context_data(*args, **kwargs)
        detail_context.update({'form': self.get_form(self.get_form_class())})
        return detail_context

    def get_initial(self):
        title = self.request.GET.get('title', '')
        return {'parent': self.object, 'text': '', 'title': title}

class NoteEdit(UpdateView):
    queryset = Note.objects.all()

class NoteDateList(ArchiveIndexView):
    queryset = Note.objects.all()
    date_field = 'created'
