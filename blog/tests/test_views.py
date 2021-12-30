
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from blog.models import Post
from django.utils import timezone

class TestBlogViews(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='user', password='password')
        user.save()
        self.user = user

        self.created_data = timezone.now()
        post = Post.objects.create(
            id=1,
            author = self.user,
            title = 'titulo do post',
            text = 'conteudo do post',
            created_data = self.created_data,
            )
        post.save()
        self.post = post

    def test_access_index(self):
        response = self.client.get(reverse('blog:index'))
        self.assertAlmostEquals(response.status_code, 200)
        
        self.assertEqual(str(response.context['user']), 'AnonymousUser')


    def test_access_post_new_no_login(self):
        response = self.client.get(reverse('blog:post-new'))
        self.assertAlmostEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/post/new/')


    def test_access_post_new_with_login(self):
        login = self.client.login(username='user', password='password')
        response = self.client.get(reverse('blog:index'))
        self.assertEqual(str(response.context['user']), 'user')

        response = self.client.get(reverse('blog:post-new'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')


    def test_access_post_detail_and_template_used(self):
        response = self.client.get(reverse('blog:post-detail', args=[self.post.id]))
        self.assertEquals(response.status_code, 200)

        self.assertTemplateUsed(response, 'blog/post_detail.html')


    def test_access_post_edit_no_login(self):
        response = self.client.get(reverse('blog:post-edit', args=[self.post.id]))
        self.assertEquals(response.status_code, 302)


    def test_access_post_edit_with_login_and_template_used(self):
        login = self.client.login(username='user', password='password')
        response = self.client.get(reverse('blog:index'))
        self.assertEquals(str(response.context['user']), 'user')

        response = self.client.get(reverse('blog:post-edit', args=[self.post.id]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')


    def test_access_post_delete_no_login(self):
        response = self.client.get(reverse('blog:post-delete', args=[self.post.id]))
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/post/1/delete/')


    def test_access_post_delete_with_login(self):
        login = self.client.login(username='user', password='password')
        response = self.client.get(reverse('blog:index'))
        self.assertEquals(str(response.context['user']), 'user')

        response = self.client.get(reverse('blog:post-delete', args=[self.post.id]))
        self.assertEquals(response.status_code, 302)#depois do delete ele faz um redirect
        self.assertRedirects(response, reverse('blog:index'))
    

    def test_access_sobre(self):
        response = self.client.get(reverse('blog:sobre'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/sobre.html')
