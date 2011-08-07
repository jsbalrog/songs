# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from songster.models import Song

def list(request):
	songs = Song.objects.all()
	returnVals = RequestContext(request, {'songs' : songs})
	return render_to_response('list_results.html', returnVals)

def search(request):
	if 'q' in request.GET:
		errors = []
		query = request.GET['q'].strip()
		if not query:
			errors.append('Enter a search term.')
		else:
			show_results = True
			results = Song.objects.filter(title__icontains=query)
			variables = RequestContext(request,
				{
					'results' : results,
					'show_results' : show_results,
					'query' : query,
					'errors' : errors
				}
			)
			return render_to_response('search.html', variables)
	return render_to_response('search.html');
