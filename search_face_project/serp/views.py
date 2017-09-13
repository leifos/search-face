from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View

import logging
import logging.handlers
from django.conf import settings
#from webhose_search import run_query
#from bing_search import run_query
from chatnoir_search import run_query

logger = logging.getLogger('sample')


# Create your views here.

class SearchView(View):
    template_name = 'serp/search.html'

    def get(self, request, *args, **kwargs):
        getdict = request.GET
        user_query = ''
        results = []
        if 'query' in getdict:
            user_query = getdict['query']
            results = run_query(user_query)
            print(results)

        return render(request, self.template_name,{'query':user_query, 'results':results})

    def post(self, request, *args, **kwargs):
        print("hello")
        user_query = ''
        results = []
        user_query = request.POST['query'].strip()
        results = run_query(user_query)

        return render(request, self.template_name, {'query':user_query, 'results':results})


class ResultsView(View):
    template_name = 'serp/results.html'

    def get(self, request, *args, **kwargs):
        getdict = request.GET
        user_query = ''
        results = []
        if 'query' in getdict:
            user_query = getdict['query']
            results = run_query(user_query)

        return render(request, self.template_name, {'results':results})






class GotoView(View):

    def get(self, request, *args, **kwargs):
        page_url = None
        if 'page_url' in request.GET:
            page_url = request.GET['page_url']
        if page_url:
            print("Redirecting to: {0}".format(page_url))
            logger.info("Redirecting to: {0}".format(page_url))
            return redirect(page_url)

        return redirect(reverse('serp-search'))


class LogView(View):

    def get(self, request, *args, **kwargs):
        msg = None
        details = ''
        if 'msg' in request.GET:
            msg = request.GET['msg']
        if 'details' in request.GET:
            details = request.GET['details']

        if msg:
            logger.info("{0} {1}".format(msg,details))
            return HttpResponse('1')
        else:
            return HttpResponse('0')




