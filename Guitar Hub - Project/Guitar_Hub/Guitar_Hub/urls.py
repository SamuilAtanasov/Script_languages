"""
URL configuration for Guitar_Hub project.

"""
from django.contrib import admin
from django.urls import path, include

from main.views import (
    home_page,
    types_page,
    chords_page,
    tips_page,
    facts_page,
    forum_page,
    edit_message,
    delete_message

)

urlpatterns = [
    path('guitar_hub_superpanel/', admin.site.urls), #hide admin url
    path('', home_page, name='home'),
    path('types/', types_page, name='types'),
    path('chords/', chords_page, name='chords'),
    path('tips/', tips_page, name='tips'),
    path('facts/', facts_page, name='facts'),
    path('forum/', forum_page, name='forum'),
    path('forum/delete/<int:message_id>/', delete_message, name='delete_message'),
    path('forum/edit/<int:message_id>/', edit_message, name='edit_message'),
    path('accounts/', include('accounts.urls')),

]
