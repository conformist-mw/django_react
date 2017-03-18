import re
from django.test import TestCase, Client
# from .models import Key


class KeyTestCase(TestCase):
    def test_create_key(self):
        c = Client()
        response = c.get('/sms/create/')
        self.assertTrue(re.match(r'[a-zA-Z0-9]{4}', response.data['id']) != None)

    def test_last_keys(self):
        c = Client()
        response = c.get('/sms/last/')
        self.assertTrue(isinstance(response.data['last'], int))

    def test_submit(self):
        c = Client()
        response = c.get('/sms/create/')
        key = response.data['id']
        submitted_response = c.get('/sms/submit/{}/'.format(key))
        self.assertFalse(submitted_response.data['active'])

    def test_check(self):
        c = Client()
        response = c.get('/sms/create/')
        key = response.data['id']
        check_response = c.get('/sms/check/{}/'.format(key))
        self.assertTrue(check_response.data['active'])

    def test_check_not_exist(self):
        c = Client()
        response = c.get('/sms/check/xxxx/')
        self.assertEqual(response.data['detail'], 'Not found.')
