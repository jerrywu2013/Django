# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template.loader import get_template
from django import template
from django.shortcuts import render_to_response

def here(request):
	return HttpResponse('哈囉，世界!')

def add(request, a, b):
	s = int(a) + int(b)
	return HttpResponse(str(s))

def math(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	html = '<html>sum={s}<br>dif={d}<br>pro={p}<br>quo={q}</html>'.format(s=s, d=d, p=p, q=q)
	return HttpResponse(html)

def mathnew(request, a, b):
	a = int(a)
	b = int(b)
	s = a + b
	d = a - b
	p = a * b
	q = a / b
	return render_to_response('math.html',{'s':s, 'd':d, 'p':p, 'q':q})