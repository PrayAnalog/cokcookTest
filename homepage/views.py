# -*- coding: utf-8 -*- 


from django.shortcuts import render

from .models import * 

def index(request):
	food_list_for_sale = Food.objects.filter(state="주문가능")
	food_list_reserve = Food.objects.filter(state="예약가능")
	food_list_not_for_sale = Food.objects.filter(state="주문불가능")
	return render(request, 'homepage/index.html', {'food_list_for_sale':food_list_for_sale, 'food_list_reserve':food_list_reserve, 'food_list_not_for_sale':food_list_not_for_sale})

def detail(request, foodid):
	food = Food.objects.get(id=foodid)
	return render(request, 'homepage/detail.html', {'food':food})
