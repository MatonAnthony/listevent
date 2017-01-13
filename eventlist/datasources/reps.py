import requests
import json

from datetime import date
from eventlist.event import Event
from eventlist.exceptions import HTTPError, FormatError


class Reps():
    """ Get events from reps.mozilla.org API v1 """

    BASE_URL = 'https://reps.mozilla.org/api/v1/event/'

    def __init__(self, query, start=date.today().isoformat(), offset=0,
                 limit=0):
        self.offset = offset
        self.limit = limit
        self.start = start
        self.query = query

    def __get_data__(self):
        url = '{}?offset={}&limit={}&start__gte={}&query={}'.format(
            self.BASE_URL, self.offset, self.limit, self.start, self.query)
        response = requests.get(url)
        if response.status_code != 200:
            raise HTTPError(response.status_code, '{} status : {}'.format(
                url, response.reason))
        if response.headers['Content-Type'] != 'application/json':
            raise FormatError(response.headers['Content-Type'],
                              '{} doesn\'t return json'.format(url))

        raw_data = json.loads(response.content)

        return raw_data['objects']

    def __parse__(self, data):
        events = []

        for event in data:
            events.append(Event(city=event['city'],
                                country=event['country'],
                                description=event['description'],
                                contact=event['owner_name'],
                                begin=event['local_start'],
                                end=event['local_end'],
                                url=event['event_url'],
                                name=event['name'],
                                venue=event['venue'],
                                latitude=event['lat'],
                                longitude=event['lon']))
        return events

    def get_events(self):
        return self.__parse__(self.__get_data__())
