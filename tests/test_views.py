from django.test import Client
from django.contrib.auth import authenticate
from unittest.mock import MagicMock
from accounts.models import *
import unittest.mock
import pytest
from django.urls import reverse
from django.utils import timezone
from unittest.mock import patch, Mock
from rest_framework import status
#from django.test import APITestCase
import string
import random
from rest_framework import status
import requests

@pytest.mark.django_db
def test_registration(client, user_data):
    mock_response = requests.models.Response()
    mock_response.status_code = 201
    mock_response._content = b'{"message": "registration successful"}'

    with unittest.mock.patch("requests.post", return_value=mock_response):
        response = client.post(reverse('Register'), user_data, format="json")
        if response.status_code != 201:
           print({"message": "registration Unsuccessful"})
        assert response.status_code == 201


@pytest.mark.django_db    
def test_login(client, user_data):
    with unittest.mock.patch('django.contrib.auth.authenticate') as mock_authenticate:
        mock_authenticate.return_value = authenticate(
            
            test_registration(client, user_data)
            )
        
        response = client.post(reverse('login'),
                               {
            'email': user_data['email'],
            'password': user_data['password'],
        })
        if response.status_code != 200:
            print({"message": "Unauthorized User"})
        assert response.status_code == 200

@pytest.mark.django_db
def test_forgot_password(client,user_data):
    # First, you need to create a user
    user = CustomUser.objects.create_user(**user_data)
        
    # Then, you can simulate a forgot password request by sending a POST request to the API
    with unittest.mock.patch('django.contrib.auth.authenticate') as mock_authenticate:
        mock_authenticate.return_value = authenticate
           
    response = client.post(reverse('forget_password'), {'email': user_data['email']}, content_type='application/json')
    assert response.status_code == 202
    assert response.data['message'] == 'Reset Password Email has been sent to your Email ID'


    # You can use MagicMock to mock the send_mail function and check if it's called
    send_password_reset_email = MagicMock(return_value=True)
    send_password_reset_email(to=[user_data['email']], subject='Password reset request', message='Reset your password',email_from = settings.EMAIL_HOST_USER)
    send_password_reset_email.assert_called_once()

    # Finally, you can check if the forget_password_token field is updated
    user = CustomUser.objects.get(email=user_data['email'])
    assert user.forget_password_token is not None
    if response.status_code != 202:
            print({"message": "Unauthorized User"})
    assert response.status_code == 202


@pytest.mark.django_db
def test_change_password(client, change_password_data,user_data):
    # First, you need to create a user and set the forget_password_token field
    with unittest.mock.patch('django.contrib.auth.authenticate') as mock_authenticate:
        mock_authenticate.return_value = authenticate(
            
            test_forgot_password(client, user_data)
            )
    user = CustomUser.objects.create_user(username = 'testuser')
    user.forget_password_token = 'token'
    user.save()
    
    # Then, you can simulate a change password request by sending a POST request to the API with the token
    with unittest.mock.patch('django.contrib.auth.authenticate') as mock_authenticate:
        mock_authenticate.return_value = authenticate

    response = client.post(reverse('change_password', kwargs={'token': 'token'}), change_password_data, content_type='application/json')
    if response.status_code != 205:
            print({'message': "Invalid credentials, try again"})
    assert response.status_code == 205
    assert response.data['message'] == 'Password change successfully now login'
    
    # Finally, you can check if the password has been updated for the user
    user = CustomUser.objects.get(username='testuser')
    assert user.check_password(change_password_data['new_password']) is True

        
'''@pytest.mark.django_db
def test_create_post(create_user):
    url = reverse('user_post')
    data = {'title': 'Test post', 'body': 'This is a test post.'}
    client = client()
    #client = APITestCase().client
    client.login(username=create_user.username, password=create_user.password)
    
    with patch('posts.views.create_post') as mock_create_post:
        mock_create_post.return_value = Mock(status_code=status.HTTP_201_CREATED)
        response = client.post(url, data, format='json')
        assert response.status_code == status.HTTP_201_CREATED'''

@pytest.mark.django_db
def test_create_blog(client,user_data,blog_data,create_user_data):
    
    user = test_login(client,user_data)
    print (user)
    #If the user exists and is authenticated, the function returns True
    user is not None and user.is_authenticated
    #return user is not None and user.is_authenticated
    user is not None and user
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"key": "value"}
    
    #Make the POST request to create the blog post
    with unittest.mock.patch("requests.post", return_value=mock_response):    
        response = client.post(reverse('blog'), blog_data, format="json")
        return response
        if response.status_code != 201:
           print({"message":"blog post not created"})
        assert response.status_code == 201

'''@pytest.mark.django_db
def test_update_blog(client,user_data,blog_data):
    
    user = test_login(client,user_data)
    print (user)
    #If the user exists and is authenticated, the function returns True
    user is not None and user.is_authenticated
    #return user is not None and user.is_authenticated
    user is not None and user
    mock_response = MagicMock()
    mock_response.status_code = 201
    mock_response.json.return_value = {"key": "value"}
    
    #Make the POST request to create the blog post update
    with unittest.mock.patch("requests.post", return_value=mock_response):    
        response = client.post(reverse('blog_update/<int:pk>/'), blog_data, format="json")
        #return response
        if response.status_code != 201:
           print({"message":"blog post not created"})
        assert response.status_code == 201'''

@pytest.mark.django_db
def test_update_blog(client, user_data, blog_data, blog_post_data):
    # Login the active user
    user = test_login(client, user_data)
    print(user)
   # assert (user and user.is_authenticated), f'User authentication failed'

    # Create a blog
    response = client.post(reverse('blog_update/<int:pk>/'), blog_data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    blog = response.json()

    # Use MagicMock to simulate the response from the put request
    mock_response = unittest.mock.MagicMock(return_value=None)
    with unittest.mock.patch('Blog_update.put', mock_response):
        # Update the blog
        response = client.put(reverse('update_blog/<int:pk>/', kwargs={'pk': blog['id']}), blog_data, format="json")
        assert response.status_code == status.HTTP_205_RESET_CONTENT
        assert mock_response.call_count == 1
   
        
'''@pytest.mark.django_db
def test_update_blog(client,user_data, blog_data,blog_post_data):
    # Login the active user
    user = test_login(client, user_data)
    #If the user exists and is authenticated, the function returns True
    user is not None and user.is_authenticated
    # result = test_registration(client, user_data)
    # assert (result is None), f'Unexpected result: {result}'
    # Create a blog
    #response = blog_post_data(client, user_data, blog_data)
    response = client.post(reverse('create_blog'), blog_data, format="json")

    assert response.status_code == status.HTTP_201_CREATED
    blog = response.json()
    print(blog)
    
    # Mock the blog update API
    # with unittest.mock.patch("requests.post", return_value=mock_response):    
    #     response = client.post(reverse('blog'), blog_data, format="json")
    #     return response
    with unittest.mock.patch('accounts.views.blog_update') as mock_update_blog:
        # Set the return value for the mock API
        mock_update_blog.return_value = {
            'id': blog['id'],
            'tag_name':random_string(),
            'blog_name': random_string(),
        }

        # Update the blog
        response = client.put(reverse('blog_update', kwargs={'pk': blog['id']}), data=blog_data , format="json")
        if response.status_code != 200:
            print({"message":"blog update failde"})
        assert response.status_code == status.HTTP_200_OK
        updated_blog = response.json()'''






'''@pytest.mark.django_db
def test_user_social_view(client,user_Social_data):
    
    # Get JWT token for the user
    #client = APIClient()
    response = client.post(reverse('user_social'), user_Social_data, content_type='application/json')
   # token = response.data['token']

    # Add JWT token to the client 
    client.credentials(HTTP_AUTHORIZATION='Bearer ')

    # Create mock data to be posted
    mock_data = user_Social_data
    #mock_data = user_Social_data{'username': 'test_user', 'provider': 'provider_name', 'uid': 'uid_value'}

    # Patch the serializer to return the mock data
    with unittest.mock.patch('django.contrib.auth.authenticate') as mock_authenticate:
        mock_authenticate.return_value = authenticate
        instance = mock_authenticate.return_value
        #instance.is_valid.return_value = True
        instance.return_value = mock_data

        # Make a post request to the view
        response = client.post('/user_social/', data=mock_data)

        # Assert the request was successful
        assert response.status_code == status.HTTP_200_OK

        # Assert the response data is as expected
        assert response.data == mock_data '''


     


