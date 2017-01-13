class Event:
    def __init__(self, name, description, city, country, venue, begin, end,
                 contact, url, longitude=None, latitude=None):
        self.name = name
        self.description = description
        self.city = city
        self.country = country
        self.venue = venue
        self.begin = begin
        self.end = end
        self.contact = contact
        self.url = url
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return 'Name : {} \n' \
               'Description : {} \n' \
               'City : {} \n' \
               'Country : {} \n' \
               'Venue : {} \n' \
               'Begin : {} \n' \
               'End : {} \n' \
               'Contact : {} \n' \
               'URL : {} \n' \
               'Longitude : {} \n' \
               'Latitude : {} \n'.format(self.name, self.description,
                                         self.city,
                                         self.country, self.venue, self.begin,
                                         self.end, self.contact, self.url,
                                         self.longitude, self.latitude
                                         )
