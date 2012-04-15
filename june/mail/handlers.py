#!/usr/bin/python
# -*- coding: utf-8 -*-

#import logging
#import urllib
#import tornado.web
#from datetime import datetime
#from tornado.auth import httpclient
#from tornado.options import options
#from tornado.auth import GoogleMixin

from .lib import MailHandler


class WelcomeMailHdr(MailHandler):
    # use options to replace
    SEND_INFO = {
        'hostport': 'smtp.gmail.com:587',
        'username': 'reorx.xiao@gmail.com',
        'password': 'mx320lf2',
        'from_addr': 'reorx.xiao@gmail.com'
    }

    def post(self):
        to_addr = self.get_argument('to_addr')
        self.send(to_addr, 'Hello', 'how are you', self.render_mail('mail_example.html'))


handlers = [
    ('/mail/welcome', WelcomeMailHdr)
]
