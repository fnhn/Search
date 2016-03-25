#coding:utf-8

from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

def index(request):
	if request.POST:
		search_content = request.POST['search_content']
		print search_content

		blocks = [{
			"title": "我是标题1",
			"content": "我是内容1",
		}, {
			"title": "我是标题2", 
			"content": "我是内容2",
		}]

		return TemplateResponse(request, "App/index.html", {
				"blocks": blocks
			});
	else:
		return TemplateResponse(request, "App/index.html", {});


