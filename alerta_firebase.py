import logging
import os
from firebase_admin import messaging, initialize_app
try:
    from alerta.plugins import app
except ImportError:
    from alerta.app import app

from alerta.plugins import PluginBase

LOG = logging.getLogger('alerta.plugins.firebase')

default_app = initialize_app()

class FirebaseNotify(PluginBase):
    def pre_receive(self, alert):
        LOG.debug('FirebaseNotify pre_receive: %s', alert)
        return alert

    def _prepare_payload(self, alert):
        LOG.debug('FirebaseNotify prepare_payload: %s', alert)
        return "{}: {}".format(alert.resource, alert.text)


    def post_receive(self, alert):
        if alert.repeat:
            LOG.debug("FirebaseNotify alert repeated - ignore")
            return

        body = self._prepare_payload(alert)
        topic = alert.resource
        title = alert.severity
        self.send_notification(body, title, topic)

    def status_change(self, alert, status, text):
        return

    def send_notification(self, body, title, topic):
        LOG.debug('FirebaseNotify: body: {}, title: {}, topic: {}'.format(body, title, topic))
        message = messaging.Message(
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            topic=topic
        )

        try:
            response = messaging.send(message)
            LOG.debug("FirebaseNotify: success {}:{}".format(title, topic))
        except Exception as e:
            LOG.error("Error: {}".format(e))
        #print("Result: {}".format(response))


if __name__ == '__main__':
    pass
    # send_notification('test_body', 'test_title', 'test_topic')
