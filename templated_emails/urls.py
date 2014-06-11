#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import patterns, url
from templated_emails.views import *

urlpatterns = patterns('',
                       url(r'^$', index, name="templated_emails_index"),
                       url(r'^view(?P<path>[\w.+-_/]+)$', view, name="templated_email_view"),
                       )
