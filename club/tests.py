from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
# Create your tests here.

class MeetingTest(TestCase):
    def setup(self):
        meeting = Meeting( meetingtitle='Discussion', meetingdate='2020-03-31', meetingtime='12:00:00', meetinglocation='Rec Center', meetingagenda='Discussing stuff')
        return meeting
    def test_string(self):
        meet = self.setup()
        self.assertEqual(str(meet), meet.meetingtitle)

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class EventTest(TestCase):
    def setup(self):
        event = Event( eventtitle='Convention', eventlocation='Convention Center', eventdate='2020-03-29', eventtime='09:00:00', eventdescription='Convention for conventions')
        return event
    def test_string(self):
        even = self.setup()
        self.assertEqual(str(even), even.eventtitle)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class ResourceTest(TestCase):
    def setup(self):
        resource = Resource( resourcename='Wiki', resourcetype='website', resourceurl='wikipedia.org', resourceentrydate='2020-03-22', resourcedescription='wikipedia website')
        return resource
    def test_string(self):
        res = self.setup()
        self.assertEqual(str(res), res.resourcename)

    def test_table(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')


# class New_Meeting_authentication_test(TestCase):
#     def setUp(self):
#         self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
#         self.prod = Meeting.objects.create(meetingtitle='Discussions', meetingdate='2019-04-02', user=self.test_user, meetingtime='09:00:00', meetinglocation='Rec Center',meetingagenda= 'Discussing stuff')

#     def test_redirect_if_not_logged_in(self):
#         response=self.client.get(reverse('newmeeting'))
#         self.assertRedirects(response, '/accounts/login/?next=/club/newMeeting/')

#     def test_Logged_in_uses_correct_template(self):
#         login=self.client.login(username='testuser1', password='P@ssw0rd1')
#         response=self.client.get(reverse('newmeeting'))
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'club/newmeeting.html')

