
from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post
from django.utils import timezone

class TestModelsBlog(TestCase):

    def setUp(self):
        user = User.objects.create_user(username='user', password='password')
        user.save()
        self.user = user
        self.created_data = timezone.now()

    def test_create_post(self):
        post = Post.objects.create(
            author = self.user,
            title = 'titulo do post',
            text = 'conteudo do post',
            created_data = self.created_data,
            )
        
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.title, 'titulo do post')
        self.assertEqual(post.text, 'conteudo do post')
        self.assertEqual(post.created_data, self.created_data)

    


