from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home_view, name= 'home'),

    # path('team/firm/', team_firm_view, name= 'team_firm'),
    path('team/partners/', team_partners_view, name= 'team_partners'),
    # path('team/global/', team_global_view, name= 'team_global'),

    path('services/accounting_services/', services_accounting_services_view, name= 'accounting_services'),
    path('services/audit_assurance/', services_audit_assurance_view, name= 'audit_assurance'),
    path('services/corporate_advisory/', services_corporate_advisory_view, name= 'corporate_advisory'),
    path('services/corporate_finance/', services_corporate_finance_view, name= 'corporate_finance'),
    path('services/outsourcing/', services_outsourcing_view, name= 'outsourcing'),
    path('services/payroll/', services_payroll_view, name= 'payroll'),
    path('services/risk_advisory/', services_risk_advisory_view, name= 'risk_advisory'),
    path('services/tax_advisory/', services_tax_advisory_view, name= 'tax_advisory'),
    path('services/services_secretarial_services/', services_secretarial_services_view, name= 'secretarial_services'),

    path('careers/', careers_view, name= 'careers'),
    path('contact_us/', contact_us_view, name= 'contact_us'),
    path('industries/', industries_view, name= 'industries'),
    # path('news/', news_view, name= 'news'),
    path('query/', query_view, name= 'query'),

    path('about_us/', about_us_view, name= 'about_us'),
    path('404/', error404_view, name= '404'),

]
