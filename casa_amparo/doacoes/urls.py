from django.urls import path, include
from casa_amparo.doacoes.views import DoacoesUpdatelView, DoacaoOutrosCreateView, DoacaoDashboardView
from django.views.decorators.cache import never_cache

app_name = 'doacoes'

urlpatterns = [

    path('<int:pk>', DoacoesUpdatelView.as_view(), name='doacao_update'),
    path('create_other_donation/', DoacaoOutrosCreateView.as_view(), name='doacao_outros_create'),
    path('donation_dashboard/', DoacaoDashboardView.as_view(), name='doacao_dashboard'),

]
