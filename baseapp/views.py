from django.shortcuts import render, redirect
from .forms import QueryForm, CareerForm
from .models import Query
# Create your views here.

def home_view(request):

    template_name = 'baseapp/home.html'
    context = {}
    return render(request, template_name, context)

# TEAM

def team_firm_view(request):

    template_name = 'baseapp/team/team_firm.html'
    context = {}
    return render(request, template_name, context)

def team_partners_view(request):

    template_name = 'baseapp/team/team_partners.html'
    context = {}
    return render(request, template_name, context)

def team_global_view(request):

    template_name = 'baseapp/team/global.html'
    context = {}
    return render(request, template_name, context)

# SERVICES

def services_accounting_services_view(request):

    template_name = 'baseapp/services/Accounting_Services.html'
    context = {}
    return render(request, template_name, context)

def services_audit_assurance_view(request):

    template_name = 'baseapp/services/Audit_Assurance.html'
    context = {}
    return render(request, template_name, context)

def services_corporate_advisory_view(request):

    template_name = 'baseapp/services/Corporate_Advisory.html'
    context = {}
    return render(request, template_name, context)

def services_corporate_finance_view(request):

    template_name = 'baseapp/services/Corporate_Finance.html'
    context = {}
    return render(request, template_name, context)

def services_outsourcing_view(request):

    template_name = 'baseapp/services/Outsourcing.html'
    context = {}
    return render(request, template_name, context)

def services_payroll_view(request):

    template_name = 'baseapp/services/Payroll.html'
    context = {}
    return render(request, template_name, context)

def services_risk_advisory_view(request):

    template_name = 'baseapp/services/Risk_Advisory.html'
    context = {}
    return render(request, template_name, context)

def services_tax_advisory_view(request):

    template_name = 'baseapp/services/Tax_Advisory.html'
    context = {}
    return render(request, template_name, context)


def services_secretarial_services_view(request):

    template_name = 'baseapp/services/Secretarial_Services.html'
    context = {}
    return render(request, template_name, context)

# REST OF nav

def contact_us_view(request):

    template_name = 'baseapp/Contact_Us.html'
    context = {}
    return render(request, template_name, context)

def industries_view(request):

    template_name = 'baseapp/Industries.html'
    context = {}
    return render(request, template_name, context)

def news_view(request):

    template_name = 'baseapp/News.html'
    context = {}
    return render(request, template_name, context)

def query_view(request):
    template_name = 'baseapp/Query.html'
    form = QueryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = { 'form' : form }
    return render(request, template_name, context)

def careers_view(request):
    template_name = 'baseapp/Careers.html'
    if request.method == 'GET':
        return render(request, template_name, {'form':CareerForm()})
    else:
        form = CareerForm(request.POST, request.FILES)
        error = None
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Please input a valid file.'
            form = CareerForm(request.POST)
            context = { 'form' : form , 'error' : error}
            return render(request, template_name, context)

def about_us_view(request):

    template_name = 'baseapp/About_Us.html'
    context = {}
    return render(request, template_name, context)

def error404_view(request):

    template_name = '404.html'
    context = {}
    return render(request, template_name, context)
