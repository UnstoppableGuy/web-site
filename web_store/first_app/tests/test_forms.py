from django.test import TestCase

from first_app.forms import UserForm

class UserFormTest(TestCase):

    def test_password1_form_char_field_label(self):
        form = UserForm()
        self.assertTrue(form.fields['password1'].label == None or form.fields['password1'].label == 'Password')

    def test_password2_form_char_field_label(self):
        form = UserForm()
        self.assertTrue(form.fields['password2'].label == None or form.fields['password2'].label == 'Password confirmation')

    def test_password2_form_char_field_help_text(self):
        form = UserForm()
        self.assertEquals(form.fields['password2'].help_text, 'Enter the same password as above, for verification.')

    def test_email_form_email_field_required(self):
        """ Checks if email is required """
        form = UserForm()
        self.assertEquals(form.fields['email'].required, True)

    def test_email_form_email_field_label(self):
        form = UserForm()
        self.assertEquals(form.fields['email'].label, 'Email')

    def test_first_name_form_char_field_max_length(self):
        form = UserForm()
        self.assertEquals(form.fields['first_name'].max_length, 50)

    def test_last_name_form_char_field_max_length(self):
        form = UserForm()
        self.assertEquals(form.fields['last_name'].max_length, 50)