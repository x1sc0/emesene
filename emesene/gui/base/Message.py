'''a module that contains a class that represents a message
'''
# -*- coding: utf-8 -*-

#    This file is part of emesene.
#
#    emesene is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 3 of the License, or
#    (at your option) any later version.
#
#    emesene is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with emesene; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

import os
import e3
import gui

class Message(object):
    '''a class that represents a message to be used by the adium themes
    '''

    def __init__(self, incoming, first, sender, display_name, alias, image_path,
            status_path, message, status, service='MSN', classes='',
            direction='ltr', timestamp=None):
        '''constructor, see
        http://trac.adium.im/wiki/CreatingMessageStyles for more information
        of the values
        '''
        self.incoming       = incoming
        self.first          = first
        self.sender         = sender
        self.display_name   = display_name
        self.alias          = alias
        self.image_path     = image_path
        self.status_path    = status_path
        self.message        = message
        self.status         = status
        self.service        = service
        self.classes        = classes
        self.direction      = direction
        self.timestamp      = timestamp

    @classmethod
    def from_contact(cls, contact, message, first, incomming, tstamp=None):
        picture = contact.picture

        if not picture:
            picture = os.path.abspath(gui.theme.user)

        return cls(incomming, first, contact.account,
                contact.display_name, contact.alias, picture,
                gui.theme.status_icons[contact.status], message,
                e3.status.STATUS[contact.status], timestamp=tstamp)

    @classmethod
    def from_data(cls, nick, message, first, incomming):
        picture = contact.picture

        if not picture:
            picture = os.path.abspath(gui.theme.user)

        return cls(incomming, first, contact.account,
                contact.display_name, contact.alias, picture,
                gui.theme.status_icons[contact.status], message,
                e3.status.STATUS[contact.status])

