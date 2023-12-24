import datetime
from django.test import TestCase
from django.utils import timezone
from django.conf import settings
from .models import Article
from decouple import config
from django.contrib.auth.password_validation import validate_password

# Create your tests here.

class ArticleModelTests(TestCase):
    def test_was_published_recently_with_future_article(self):
        """
        was_published_recently() returns False for articles whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_article = Article(pub_date=time)
        self.assertIs(future_article.was_published_recently(), False)

    def test_was_published_recently_with_old_article(self):
        """
        was_published_recently() returns False for articles whose pub_date is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_article = Article(pub_date=time)
        self.assertIs(old_article.was_published_recently(), False)


    def test_was_published_recently_with_recent_article(self):
        """
        was_published_recently() returns True for articles whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_article = Article(pub_date=time)
        self.assertIs(recent_article.was_published_recently(), True)

    def test_str_method(self):
        """
        __str__() should return a string representation of the article.
        """
        article = Article(title="Test Article")
        self.assertEqual(str(article), "Test Article")

    def test_secret_key_strength(self):
        """
        checks if we have a strong secret key
        """
        SECRET_KEY = config("SECRET_KEY")
        try:
            is_strong = validate_password(SECRET_KEY)
        except Exception as e:
            self.fail(e)    


            