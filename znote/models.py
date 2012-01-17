from django.db import models
#from django.core.urlresolvers import reverse
#from django.db.models import Q
from django_extensions.db import models as emodels
from mptt import models as tmodels
import os
from tempfile import mkstemp
#import markdown

class Notebook(tmodels.MPTTModel, emodels.TitleSlugDescriptionModel):
    parent = tmodels.TreeForeignKey('self', null=True, blank=True, related_name='children')

    def __str__(self):
        return self.title

class NoteBase(tmodels.MPTTModel, emodels.TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    slug = emodels.AutoSlugField(populate_from='title', blank=True)
    notebook = models.ForeignKey(Notebook, null=True, blank=True, related_name='%(class)s_items')
    parent = tmodels.TreeForeignKey('self', null=True, blank=True, related_name='%(class)s_children')

    class Meta:
        abstract = True

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        if self.parent:
            return "%s/%s" % (self.parent, self.title)
        else:
            return self.title

    def note_children(self):
        if self.children.count() <= 0:
            return None
        return self.children.filter()

class Note(NoteBase):
    text = models.TextField()

    def edit(self):
        fid, tmpfile = mkstemp(suffix='.note')
        orig_text = self.text
        with open(tmpfile, 'w') as f:
            f.write(self.text)
        print "Editing note %s..." % self.title
        os.system('vim %s' % tmpfile)
        with open(tmpfile) as f:
            new_text = f.read()
        if new_text != orig_text:
            print "New text!  Saving text to model..."
            self.text = new_text
            self.save()

    @models.permalink
    def get_absolute_url(self):
        return('note_detail', [self.id])

    def render_text(self):
        pass
        #md_ext = ['codehilite', 'wikilinks', 'toc', 'nl2br']
        #md_conf = {'wikilinks': [('build_url', self.wikilinks_build_url)]}
        #md = markdown.Markdown(extensions=md_ext, extension_configs=md_conf)
        #return md.convert(self.text)

STATUSES = ['New', 'In Progress', 'Finished', 'Expired']

STATUS_CHOICES = [(n, choice) for n, choice in enumerate(STATUSES)]

class Task(NoteBase):
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    due = models.DateField(null=True, blank=True)
