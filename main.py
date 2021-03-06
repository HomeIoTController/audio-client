import os
import json

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.config import Config

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

from connected import Connected
import settings

Config.set('kivy','window_icon','images/favicon.ico')

class Login(Screen):
    error_message = ""

    def __init__(self, **kwargs):
        self.name='login'
        super(Login,self).__init__(**kwargs)

        self.transport = RequestsHTTPTransport(
            url=settings.apiURL,
            use_json=True,
        )

        self.client = Client(
            retries=3,
            transport=self.transport,
            fetch_schema_from_transport=True,
        )

    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        query = gql("mutation { login(email: \"" +
            app.username + "\", password: \"" + app.password +
        "\") }")

        try:
            self.ids['error_message'].text = ""
            app.jwt_token = self.client.execute(query)['login']

            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'connected'

            app.config.read(app.get_application_config())
            app.config.write()

        except Exception as err:
            self.ids['error_message'].text = json.loads(err.args[0].replace("\'", "\""))['message']


    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""
        self.ids['error_message'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        self.icon = 'images/favicon.ico'
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))

        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
