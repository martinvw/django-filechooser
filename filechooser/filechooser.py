import datetime
import json
import humanize
import os
import urllib

from operator import itemgetter

from django.http import HttpResponse, HttpResponseNotFound
from django.conf.urls import url

class FileChooser(object):
    def __init__(self, id, basedir, callback = None):
        self.pattern = r'^filechooser/'+id+'/(?P<type>((ajax)|(http)))/(?P<method>((list)|(process)))/(?P<file>.*)$'
        self.id = id

        # check that id only contains a-z0-9

        self.callback = callback
        self.basedir = os.path.abspath(basedir)

    def url_pattern(self):
        return url(self.pattern, self.process, name='filechooser_'+self.id)

    def process(self, request, file=None, type=None, method=None):
        # make sure we can't get higher than the given basedir
        path = os.path.join(self.basedir, file)
        absolute = os.path.abspath(path)

        # path should still contain at least the BASE directory
        if not absolute.startswith(self.basedir):
            raise  EnvironmentError("Do not try to escape from the designated folder")

        if method == 'list' and type == 'ajax':
            return self.__ajax_list(file)
        elif method == 'process' and type == 'http':
            if self.callback: return self.callback(file)
        else:
            return HttpResponseNotFound("<h1>Requested operation not supported in FileChooser</h1>")


    def __ajax_list(self, folder):
        path = os.path.join(self.basedir, folder)
        records = []

        for filename in os.listdir(path):
            records.append(self.__process_file(folder, filename))

        result = {
            "data": sorted(records, key=itemgetter('order'))
        }

        return HttpResponse(json.dumps(result))

    def __process_file(self, folder, filename):
        fullpath = os.path.join(self.basedir, folder, filename)

        mtime = os.path.getmtime(fullpath)
        mtime_date = datetime.datetime.fromtimestamp(mtime)

        size = os.path.getsize(fullpath)
        natural_size = humanize.naturalsize(size,gnu=True)
        sortkey = 'z'
        icon = filetype = 'file'

        if os.path.isdir(fullpath):
            sortkey = 'a' # force the folder in front of the files
            filetype = 'folder'
            icon = 'folder-open'
            natural_size = '-'
            size = -1

        return {
            'order'   : sortkey + os.path.join(folder, filename).lower(),
            'filename': {
                'icon':    icon,
                'value':   os.path.join(folder, filename),
                'display': filename,
                'type':    filetype,
            },
            'size': {
                'value':   size,
                'display': natural_size
            },
            'mtime': {
                'value':   mtime,
                'display': humanize.naturaltime(datetime.datetime.now() - mtime_date),
                'title':   mtime_date.strftime("%x %X")
            }
        }
