from Worker import Worker
import e3

class Session(e3.Session):
    '''a specialization of e3.Session'''
    NAME = 'Jabber session'
    DESCRIPTION = 'Session to connect to the Jabber network'
    AUTHOR = 'Mariano Guerra'
    WEBSITE = 'www.emesene.org'

    SERVICES = {
        "gtalk": {
            "host": "talk.google.com",
            "port": "5223"
        },
        "facebook": {
            "host": "chat.facebook.com",
            "port": "5222"
        }
    }

    def __init__(self, id_=None, account=None):
        '''constructor'''
        e3.Session.__init__(self, id_, account)

    def login(self, account, password, status, proxy, host, port, use_http=False):
        '''start the login process'''
        self.account = e3.Account(account, password, status, host)
        worker = Worker('emesene2', self, proxy, use_http)
        worker.start()

        self.add_action(e3.Action.ACTION_LOGIN, (account, password, status,
            host, port))

    def send_message(self, cid, text, style=None, cedict=None, celist=None):
        '''send a common message'''
        if cedict is None:
            cedict = {}

        if celist is None:
            celist = []

        account = self.account.account
        message = e3.Message(e3.Message.TYPE_MESSAGE, text, account,
            style)
        self.add_action(e3.Action.ACTION_SEND_MESSAGE, (cid, message))

    def request_attention(self, cid):
        '''request the attention of the contact'''
        account = self.account.account
        message = e3.Message(e3.Message.TYPE_MESSAGE,
            '%s requests your attention' % (account, ), account)
        self.add_action(e3.Action.ACTION_SEND_MESSAGE, (cid, message))
