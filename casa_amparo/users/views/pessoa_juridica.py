from allauth.account import app_settings
from allauth.account.utils import passthrough_next_redirect_url
from allauth.account.views import SignupView
from allauth.utils import get_request_param
from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView

from ..forms import PessoaJuridicaSignUpForm


class PessoaJuridicaSignUpView(SignupView):
    # The referenced HTML content can be copied from the signup.html
    # in the django-allauth template folder
    template_name = 'account/signup.html'
    # the previously created form class
    form_class = PessoaJuridicaSignUpForm

    # the view is created just a few lines below
    # N.B: use the same name or it will blow up
    view_name = 'pessoa_juridica_signup'

    # I don't use them, but you could override them
    # (N.B: the following values are the default)
    # success_url = None
    # redirect_field_name = 'next'


# Create the view (we will reference to it in the url patterns)
pessoa_juridica_signup = PessoaJuridicaSignUpView.as_view()
