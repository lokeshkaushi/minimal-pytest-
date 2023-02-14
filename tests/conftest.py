import pytest
import uuid
from accounts.models import *
from django.test import Client, TestCase
from django.urls import reverse
import string
import random
from django.core.mail import send_mail
from PIL import Image
import io

def random_string(string_length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters)for i in range(string_length))

@pytest.fixture
def user_data():
    return {
        'username': random_string(),
        'email': random_string()+'@gmail.com',
        'password': random_string(),
        'first_name' : random_string(),
        'last_name':  random_string(),
        'number' : '+' + str(random.randint(1, 999)) + str(random.randint(100000000, 999999999))
    }

@pytest.fixture
def forget_password_mail():
    return {
        
        'username': random_string(),
        'email': random_string()+'@gmail.com',
        'password': random_string(),
    }

@pytest.fixture
def change_password_data():
    return {
        'new_password': random_string(),
        'confirm_password': random_string()
       }

@pytest.fixture
def create_user(user_data):
    username = user_data['username']
    password = user_data['password']
    user = CustomUser.objects.create_user(username=username, password=password)
    return user     

@pytest.fixture
def create_user_data(user_data):
    return {
       'user': user_data['username'],
      # 'username': random_string(),
       'email': random_string()+'@gmail.com',
       'password': random_string(),
       'first_name' : random_string(),
       'last_name':  random_string(),
       'number' : '+' + str(random.randint(1, 999)) + str(random.randint(100000000, 999999999))
    }   



def imagee():        
    img = Image.new("RGB", (128, 128), (255, 0, 0))
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="JPEG")
    img_bytes = img_bytes.getvalue()
    return img_bytes



@pytest.fixture
def post_data():
    return{
        
        'post_name': random_string(), 
        'tag_name': random_string(),
        'post_header': random_string(),
        'post_content': random_string(),
        'images': imagee(),
        'blog': 5,
        'user': random_string()
        }       

@pytest.fixture
def blog_data(user_data):
    return {
       "tag_name":random_string(),
       'blog_name': random_string(),
       'images': imagee(),
       'user': user_data['username']
    }
         
@pytest.fixture        
def blog_post_data():
    return {
       "tag_name":random_string(),
       'blog_name': random_string(),
       'images': imagee()
}

@pytest.fixture
def user_Social_data():
    return {
        'linkedin':random_string(),
        'twitter': random_string(),
        'instagram': random_string(),
        'facebook' : random_string(),
        'user':random_string()
    }

'''@pytest.fixture
def create_user(django_db_setup, django_db_blocker, user_data):
    with django_db_blocker.unblock():
        User = Post
        Post.objects.create_user(**user_data)'''

