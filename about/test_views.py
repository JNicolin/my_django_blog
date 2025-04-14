from django.urls import reverse
from django.test import TestCase
from .forms import CollaborateForm
from .models import About

class TestAboutViews(TestCase):

    def setUp(self):
        self.about = About(
            title="About title",
            content="testing an about content")
        
        self.about.save()

    def test_render_about_page_with_collaborate_form(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIsInstance(response.context['collaborate_form'], CollaborateForm)

    def test_successful_post_of_collaboration_submission(self):
        """Test for posting a collaboration request on a post"""
        post_data = {
            'name': 'Johan', 
            'email': 'johan@test.se', 
            'message': 'This is a test request.'
            }
        response = self.client.post(reverse('about'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Collaboration request received! I endeavour to respond within 2 working days.',response.content)