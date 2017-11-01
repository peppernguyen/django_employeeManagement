# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views import generic
# Create your views here.
from em.models import Employee


class EmployeeListView(generic.ListView):
    model = Employee
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        num_employees = Employee.objects.all().count()
        context['num_employees'] = num_employees
        return context

    def get_queryset(self):
        return Employee.objects.all()

def SubTree(request, pk):
    emps = Employee.objects.filter(parents=pk)
    root = Employee.objects.get(id = pk)
    #
    context = {'instances':emps, 'root': root}


    return render(request, 'subtree.html', context )

class EmployeeCreate(generic.CreateView):
    model = Employee
    template_name = 'emp_form.html'
    fields = '__all__'
    # initial={'date_of_death':'12/10/2016',}