from django.shortcuts import render, HttpResponse, redirect, reverse
from django.views import View
from ifind.search import EngineFactory
from ifind.search import Query

import logging
import logging.handlers
from django.conf import settings
logger = logging.getLogger('sample')


# Create your views here.

class SearchView(View):
    template_name = 'serp/search.html'
    engine = EngineFactory('dummy')

    def get(self, request, *args, **kwargs):
        getdict = request.GET
        user_query = ''
        results = []
        if 'query' in getdict:
            user_query = getdict['query']
            results = self.do_search(user_query,1,10)
            print(results)

        return render(request, self.template_name,{'query':user_query, 'results':results})

    def post(self, request, *args, **kwargs):
        print("hello")
        user_query = ''
        results = []
        user_query = request.POST['query'].strip()
        results = self.do_search(user_query,1,10)

        return render(request, self.template_name, {'query':user_query, 'results':results})

    def do_search(self, query_str, page, num_results):
        logger.info("Query Issued {0}".format(query_str))
        query = Query(query_str, top=num_results)
        response = self.engine.search(query)
        return response

class ResultsView(View):
    template_name = 'serp/results.html'
    engine = EngineFactory('dummy')

    def get(self, request, *args, **kwargs):
        getdict = request.GET
        user_query = ''
        results = []
        if 'query' in getdict:
            user_query = getdict['query']
            results = self.do_search(user_query,1,10)

        return render(request, self.template_name, {'results':results})

    def do_search(self, query_str, page, num_results):
        logger.info("Query Issued {0}".format(query_str))
        query = Query(query_str, top=num_results)
        response = self.engine.search(query)
        return response




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




