from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from music.models import Album , Song
from django.template import loader

### views with templates on

def index(request):
	all_albums = Album.objects.all()
	template = loader.get_template('music/index.html')
	## information that your template needs
	context  = {'all_albums' : all_albums}
	#return HttpResponse(template.render(context, request))
	return render(request, 'music/index.html', context)

## old details view
# def detail(request,album_id):
# 	text = "<h1> Details for Album id is :" + str(album_id) + "</h1>"
# 	return HttpResponse(text)


### use get_object_or_404 to remove try and except syntax
def detail(request, album_id):
	try:
		album = Album.objects.get(pk=album_id)
		template = loader.get_template('music/details.html')
		context = {
		'album': album,
		}
	except Album.DoesNotExist:
		raise Http404(" Album DoesNotExist ")
	return render(request, 'music/details.html', {'album' : album})
	#return HttpResponse(template.render(context, request))

def favorite(request, album_id):
	album  = get_object_or_404(Album, pk=album_id)
	try: 
		## get the value of the song selected
		selected_song = album.song_set.get(pk = request.POST['song'])
	except (KeyError, Song.DoesNotExist):
		return render(request, 'music/details.html', 
			{
			"album": album,
			"error_message": "You did not select anything"})
	else:
		selected_song.is_favorite = True
		selected_song.save()
		return render(request, 'music/details.html', {'album' : album })



def more_depth(request, album_id, sec_al):
	return HttpResponse("<h2> Details further:" + str(album_id) +"sec_al" + str(sec_al) + "</h2>")

### views




# from django.views import generic
# from music.models import Album
# ## list of all albums
# class IndexView(generic.ListView):
# 	template_name = 'music/index.html'
# 	context_object_name = 'all_albums'

# 	def get_queryset(self):
# 		return Album.objects.all()

# class DetailView(generic.DetailView):
# 	model = Album
# 	template_name = 'music/details.html'
