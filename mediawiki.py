import json
import requests


class MediaWiki(object):
    def __init__(self, session, headers, proxies, url):
        self.session = session
        self.headers = headers
        self.proxies = proxies
        self.url = url
        
    def get_token(self, action):
        base = self.url
        try:
            print("getting token for %s" % action)
            params = {'action': 'query', 'meta': 'tokens', 'type': action, 'format': 'json'} \
                     if action is not 'query' \
                     else {'action': 'query', 'meta': 'tokens', 'format': 'json'}
            login = self.session.get(
                    url=base,
                    params=params,
                    headers=self.headers,
                    proxies=self.proxies
            )
            return login.text
        except (ConnectionError, ValueError) as e:
            raise e


    def login(self, uname, pw):
        base = self.url
        try:
            token = json.loads(self.get_token('login'))["query"]["tokens"]["logintoken"]
            params = {
                'action': 'clientlogin',
                'username': uname,
                'password': pw,
                'format': 'json',
                'loginreturnurl': base,
            }
            data = {
                'logintoken': token
            }
            print("trying to login...")
            log =self.session.post(
                    url=base,
                    params=params,
                    headers=self.headers,
                    proxies=self.proxies,
                    data=data
            )
            return log.text
        except (ConnectionError, ValueError) as e:
            raise e


    def edit(self, text, params, uname, password):
        base = self.url
        try:
            if not "error" in self.login(uname, password):
                token = json.loads(self.get_token('query'))["query"]["tokens"]["csrftoken"]
                params = {
                    'action': 'edit',
                    'title': params["title"],
                    'format': params["format"]
                }
                data = {
                    'text': text,
                    'token': token,
                }
                req =self.session.post(
                        url=base,
                        params=params,
                        headers=self.headers,
                        proxies=self.proxies,
                        data=data
                )
                print(req.text)
            else:
                raise AuthenticationError()
        except (ConnectionError, ValueError) as e:
            raise e


class AuthenticationError(Exception):
    def __init__(self):
        super().__init__("Invalid Username or Password")
