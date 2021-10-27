
from typing import Generator
from .models import LotInv, ProjectList
from django.core import paginator
from django.db.models.expressions import RawSQL
from django.http.response import Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required
from django.db import connection
from .filters import LotInvFilters
from .form import LotInvForm


# Create your views here.



@login_required(login_url='user-login')
def index(request):
        lot_list = LotInv.objects.all().order_by('c_lid')
        available = LotInv.objects.filter(c_status='Available')
        available_count = available.count()
        sold = LotInv.objects.filter(c_status='Sold')
        sold_count = sold.count()
        hold = LotInv.objects.filter(c_status='On Hold')
        hold_count = hold.count()
       
        context = {
        'lot_list': lot_list,
        'available': available,
        'sold' : sold,
        'hold': hold,
        'sold_count': sold_count,
        'available_count': available_count,
        'hold_count': hold_count,
         }

        return render(request, 'lot_inv/index.html', context)


@login_required(login_url='user-login')
def lots(request):
    
        result = LotInv.objects.filter().order_by('c_lid')
        #acronym = ProjectList.objects.values_list('c_code','c_acronym')
        acronym = ProjectList.objects.filter().order_by('c_acronym')
        
        #proj_list = ProjectList.objects.all().order_by('c_acronym')

        myfilter = LotInvFilters(request.GET, queryset=result)
        results = myfilter.qs
        
        paginator = Paginator(results, 5)
        page_number = request.GET.get('page',1)
        results = paginator.get_page(page_number)
        #results =  paginator.page(page_number)

        context = {
        'page_obj' : results,
        'acronym' : acronym,
        #'project_list': proj_list,
        'myfilter' : myfilter
         }
     
     
        return render(request, 'lot_inv/lots.html', context)

   

@login_required(login_url='user-login') 
def add_lot(request):
        form = LotInvForm()
        if request.method == 'POST':
            form = LotInvForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect('/lot_inv')
        else:
            form = LotInvForm()
            

        context = {'form': form}
        return render(request, 'lot_inv/add_lot.html',context)



@login_required(login_url='user-login') 
def update_lot(request, pk):
	lot_details = LotInv.objects.get(id=pk)
	form = LotInvForm(instance=lot_details)

	if request.method == 'POST':
		form = LotInvForm(request.POST, instance=lot_details)
		if form.is_valid():
			form.save()
			return redirect('/lot_inv')

	context = {'form':form}
	return render(request, 'lot_inv/add_lot.html', context)


@login_required(login_url='user-login') 
def delete_lot(request, pk):
        lot_details = LotInv.objects.get(id=pk)
        #print(lot_details)
        if request.method == 'POST':
	        lot_details.delete()
	        return redirect('/lot_inv')

        context = {'lot_details': lot_details}
        return render(request, 'lot_inv/delete_lot.html', context)


def generate_lid(request):
        l_site =request.POST.get('c_site') 
        l_block =request.POST.get('c_block')
        l_lot =request.POST.get('c_lot')

        l_site_no = int(l_site)
        l_block_no = int(l_block)
        l_lot_no = int(l_lot)
        l_lid = "%03d%03d%02d" % (l_site_no,l_block_no, l_lot_no)
        print(l_lid)
        try:
                n = LotInv.objects.get(c_lid=l_lid)
                # lid already exists
                return render(request, 'lot_inv/add_lot.html', {'error_message' : "Duplicate lid: " + l_lid})
        except ObjectDoesNotExist:

                context = {'l_lid' : l_lid}
                return render(request, 'lot_inv/add_lot.html', context)

