from django.contrib.auth.tokens import PasswordResetTokenGenerator

# pip install six
from six import text_type



class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (text_type(user.is_active) + text_type(user.pk) # pragma: no cover
                + text_type(timestamp))
        
my_token_generator = TokenGenerator()