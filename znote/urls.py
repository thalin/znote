from django.conf.urls.defaults import url, patterns
from views import NoteList, NoteDetail, NoteEdit, NoteCreate, NoteCreateChild, NoteDateList


urlpatterns = patterns('',
    url(r'^$', NoteList.as_view(), name='note_home'),
    url(r'^list/$', NoteList.as_view(), name='note_list'),
    url(r'^create/$', NoteCreate.as_view(), name='note_create'),
    url(r'^by_date/$', NoteDateList.as_view(), name='note_date_list'),
    url(r'^(?P<pk>\d+)/$', NoteDetail.as_view(), name='note_detail'),
    url(r'^(?P<pk>\d+)/create/$', NoteCreateChild.as_view(), name='note_create_child'),
    url(r'^(?P<pk>\d+)/edit/$', NoteEdit.as_view(), name='note_edit'),
)
