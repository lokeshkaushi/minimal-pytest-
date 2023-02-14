# from django.test import TestCase
# from accounts.models import *
# from rest_framework.test import APIClient
# from rest_framework import status
# import factory
# from django.http import HttpResponse
# import uuid
# import random
# from django.test import TestCase
# from unittest.mock import MagicMock


# class RegisterApiTestCase(TestCase):
#     def setUp(self):
#         self.request = MagicMock()
#         self.User = CustomUser

#     def test_register_api(self):
#         # Generate dynamic values for the test data
        
#         username = 'testuser' + str(uuid.uuid4())[:8]
#         email = 'testemail' + str(uuid.uuid4())[:8] + '@example.com'
#         password = 'testpassword' + str(uuid.uuid4())[:8]
#         first_name = 'testfirst_name'  + str(uuid.uuid4())[:8]
#         last_name = 'testlast_name'  + str(uuid.uuid4())[:8]
#         # Generate a valid mobile number for all countries
#         print(username)
#         number = '+' + str(random.randint(1, 999)) + str(random.randint(100000000, 999999999))
       
#         data = {
#             'username': username,
#             'email': email,
#             'first_name' : first_name,
#             'last_name' : last_name,
#             'password': password,
#             'number': number,
#         }
#         self.request.data = data

#         # Call the registration API
#         response = self.client.post('http://127.0.0.1:8000/register/', data,format="json")
#         print(response.json())
#         # Assert that the API returns a 201 status code
#         self.assertEqual(response.status_code, 201)
        
#         #Assert that a user was created with the correct information

#         self.assertTrue(CustomUser.objects.filter(username=username).exists())
#         self.assertTrue(CustomUser.objects.filter(email=email).exists())
#         self.assertTrue(CustomUser.objects.filter(first_name=first_name).exists())
#         self.assertTrue(CustomUser.objects.filter(last_name=last_name).exists())
#         self.assertTrue(CustomUser.objects.filter(number=number).exists())
#         self.assertFalse(CustomUser.objects.filter(password=password).exists())


'''@pytest.mark.django_db
def test_registration(client, user_data):
    response = client.post(reverse('Register'), user_data, format="json")
    _data = response.json()
    assert response.status_code == 201
    assert _data.get('status') == True
    assert _data.get('message') == "Register successfully"
    #print("Registration successful")'''




'''class LoginApiTestCase(TestCase):
    def setUp(self):
        self.request = MagicMock()
        self.User = CustomUser

    def test_login_api(self):
        # Generate dynamic values for the test data
        
        email = 'testemail' + str(uuid.uuid4())[:8] + '@example.com'
        password = 'testpassword' + str(uuid.uuid4())[:8]
        
        # Generate a valid mobile number for all countries
        data = {
            
            'email': email,
            'password': password,
        }
        self.request.data = data

        # Call the registration API
        response = self.client.post('http://127.0.0.1:8000/login/', data,format="json")
        #print(response.json())
        # Assert that the API returns a 201 status code
        self.assertEqual(response.status_code, 201)
        
        #Assert that a user was created with the correct information
        
        self.assertTrue(CustomUser.objects.filter(email=email).exists())
        # self.assertTrue(CustomUser.objects.filter(first_name=first_name).exists())
        # self.assertTrue(CustomUser.objects.filter(last_name=last_name).exists())
        # self.assertTrue(CustomUser.objects.filter(number=number).exists())
        self.assertTrue(CustomUser.objects.filter(password=password).exists())'''


'''@pytest.mark.django_db
def test_forgot_password(client, user_data):
    # Get the URL for the forget password view
    
    with unittest.mock.patch('django.contrib.auth.authenticate') as mock_authenticate:
        mock_authenticate.return_value = authenticate(
        test_login(client, user_data))
           
    # Call the API to request a password reset
    response = client.post(reverse('forget_password'),{'email': user_data['email']}, content_type='application/json')
    

    # Check that a password reset email has been sent
    send_password_reset_email = MagicMock()
    send_password_reset_email()
    send_password_reset_email.assert_called_once()
    
    # Check that the password reset token has been added to the user's profile
    
    user = CustomUser.objects.get(email= user_data['email'])
    assert user.forget_password_token is not None
    assert user.email is not None
    #assert response.status_code == 202
    if response.status_code != 202:
            print({"message": "Unauthorized User"})
    assert response.status_code == 202'''

   