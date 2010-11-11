# this module will include a parser for all the markups that will
# convert it into a restricted subset of xhtml
import os
import xml.sax.saxutils
import re
import base64

import gui

dic = {
    '\"'    :    '&quot;',
    '\''    :    '&apos;',
}

dic_inv = {
    '&quot;'    :'\"',
    '&apos;'    :'\''
}

URL_REGEX_STR = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
URL_REGEX = re.compile(URL_REGEX_STR)

def escape(string_):
    '''replace the values on dic keys with the values'''
    return xml.sax.saxutils.escape(string_, dic)

def unescape(string_):
    '''replace the values on dic_inv keys with the values'''
    return xml.sax.saxutils.unescape(string_, dic_inv)

def parse_emotes(message, cedict={}):
    '''parser the emotes in a message, return a string with img tags
    for the emotes acording to the theme'''

    # Get the message body to parse emotes
    p = re.compile('<span.*?>(.*)</span>', re.DOTALL)
    plain_find = p.search(message)
    if plain_find:
        plain_text = plain_find.group(1)
    else:
        plain_text = ''

    chunks = [plain_text]
    shortcuts = gui.Theme.EMOTES.keys()
    if cedict is not None:
        shortcuts.extend(cedict.keys())
    temp = []

    while len(shortcuts) > 0:
        shortcut = shortcuts.pop()
        temp = []

        for chunk in chunks:
            parts = chunk.split(shortcut)

            if len(parts) > 1:
                if shortcut in gui.Theme.EMOTES.keys():
                    path = gui.theme.emote_to_path(shortcut)
                else:
                    path = cedict[shortcut]
                tag = '<img src="%s" alt="%s"/>' % (path, shortcut)

                for part in parts:
                    temp.append(part)
                    temp.append(tag)

                temp.pop()
            else:
                temp.append(chunk)

        chunks = temp

    # return the markup with plan text
    return message.replace(plain_text, ''.join(chunks))

def replace_shortcut_with_tag(string, short, tag):
    def repltags(m):
        tags.append(m.group(0))
        return '#THEREISATAGHERE#'
    def backtags(m):
        return tags.pop()
    tags = []
    result = re.sub(r'(<img[^>]+\>)', repltags, string)
    result = result.replace(short, tag)
    tags.reverse()
    result = re.sub(r'#THEREISATAGHERE#', backtags, result)
    return result

def replace_emotes(msgtext, cedict={}, cedir=None, sender=''):
    '''replace emotes with img tags to the images'''
    shortcuts = gui.Theme.EMOTES.keys()
    if cedict is not None:
        l_cedict = cedict.keys()
        l_cedict.sort(key=lambda x: len(x), reverse=True)
        shortcuts.extend(l_cedict)
    for shortcut in shortcuts:
        eshort = escape(shortcut)
        if eshort in msgtext:
            if shortcut in gui.Theme.EMOTES.keys():
                path = gui.theme.emote_to_path(shortcut)
            else:
                path = os.path.join(cedir, cedict[shortcut])

            if path is not None:
                # creating sort of uid for image name since different users
                # may have different images with the same shortcut
                _id = base64.b64encode(sender+shortcut)
                imgtag = '<img src="%s" alt="%s" name="%s"/>' % (path, eshort, _id)
                #msgtext = msgtext.replace(eshort, imgtag)
                msgtext = replace_shortcut_with_tag(msgtext, eshort, imgtag)

    return msgtext

def get_custom_emotes(message, cedict={}):
    ''' returns a list with the shortcuts of the
        custom emoticons present in the message
        celist comes from cache '''
    chunks = [message]
    l = []
    if cedict is None:
        return l
    shortcuts = cedict.keys()
    while len(shortcuts) > 0:
        shortcut = shortcuts.pop()

        for chunk in chunks:
            parts = chunk.split(shortcut)

            if len(parts) > 1:
                l.append(shortcut)
    return l

def replace_urls(match):
    '''function to be called on each url match'''
    url = match.group()
    return '<a href="%s">%s</a>' % (url, url)

def urlify(strng):
    '''replace urls by an html link'''
    return re.sub(URL_REGEX, replace_urls, strng)

