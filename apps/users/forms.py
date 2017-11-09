# _*_ coding: utf-8 _*_
__author__ = 'taylor'
__date__ = '02/11/2017 5:02 PM'


from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class ResetPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)