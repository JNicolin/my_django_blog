from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'carl',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_form_name_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'JN',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Name is not valid")

    def test_form_email_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'carl',
            'email': 'test@tes.se',
            'message': 'Hello!'
        })
        self.assertTrue(form.is_valid(), msg="Email is not valid")

    def test_form_message_is_required(self):
        """ Test for all fields"""
        form = CollaborateForm({
            'name': 'carl',
            'email': 'test@test.com',
            'message': 'tst9jg'
        })
        self.assertTrue(form.is_valid(), msg="Message is not valid")