import os

from eventlist.datasources.reps import Reps
from werkzeug.contrib.cache import SimpleCache
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
    SECRET_KEY='CHANGE ME',
    REFRESH_RATE=15 * 60
))

app.config.from_envvar('EVENTLIST_SETTINGS', silent=True)

""" We use an in memory cache to avoid constantly pulling various sources """
cache = SimpleCache()


@app.route('/')
def render_all_events():
    events = cache.get('all-events')
    if events is None:
        cache.set('all-events', __get_all_events(), timeout=app.config.get(
            'REFRESH_RATE', 15 * 60
        ))
        events = cache.get('all-events')

    return render_template('body.html', events=events)


def __get_all_events():
    events = []
    events.extend(Reps(query='belgium').get_events())
    events.extend(Reps(query='france').get_events())
    return events
