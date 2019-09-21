from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.shortcuts import render_to_response	
from django.template.loader import get_template	
from django.views.decorators.csrf import csrf_exempt
from audio.models import db_design, speech , store_syn
from django.utils.decorators import method_decorator
from audio.python_codes import algo, clean_up
from audio.python_codes.algo import rec_speech
from audio.python_codes.clean_up import text_clean


# Create your views here.

def homepage(request):
	return HttpResponse("<h1>This is New</h1>")


def temp_l(request):
	context= {}
	return render_to_response('audio/intro.html', context)


def disp_results(request):
	if len(request.GET['fname']) < 1:
		m_return = "you entered nothing"
	else:
		fname = request.GET['fname']
		lname = request.GET['lname']
	context={'first_name': fname, 'last_name': lname}
	return render_to_response('audio/search.html', context)


@csrf_exempt
def store_results(request):
	if request.method =='POST':
		if request.POST.get('fname') and request.POST.get('lname'):
			post= db_design()
			post.first_name = request.POST.get('fname')
			post.last_name = request.POST.get('lname')
			fname = request.POST.get('fname')
			lname = request.POST.get('lname')
			context = {'first_name' : fname , 'last_name' : lname}
			post.save()
			return render(request, 'audio/store.html', context)
		else:
			return render(request, 'audio/store.html')




################### Store Syndrome code
def form_res(request):
	context ={}
	return render_to_response('audio/form_db.html', context)


@csrf_exempt
def get_form_res(request):
	context= {}
	if len(request.GET['Syndrome']) < 1:
		m_return = "you didnt enter anything"
	else:
		m_return = request.GET['Syndrome']
	context = {'syndrome': m_return}
	return render_to_response('audio/get_form_res.html',context)

@csrf_exempt
def store_data(request):
	if request.method == 'POST':
		if request.POST.get('SYN'):
			post= store_syn()
			post.syndrome_store = request.POST.get('SYN')
			post.save()

			return render_to_response('audio/store_syn.html')
		else:
			return render_to_response('audio/store_syn.html')

#############################################

### Get  Speech CODE

### record speech
def sample_voice(request):
	context= {}
	return	render_to_response('audio/voice_text_temp.html', context)


def display_speech(request):
	if len(request.GET['rec_speech'])< 1:
		m_return = "No recs"
	else:
		m_return = request.GET['rec_speech']
	context ={'rec_words': m_return}
	return render_to_response('audio/disp_speech.html', context)

@csrf_exempt
def save_speech(request):
	if request.method == 'POST':
		if request.POST.get("lang"):
			post = speech()
			post.voice_to_text= request.POST.get('lang')
			post.save()
			m_return = request.POST.get("lang")
			####### 			
			### symptoms
			my_sentence = request.POST.get("lang")
			eci = '100011'
			s1,s2,s3,s4,s5=text_clean(my_sentence).clean_words()
			aa= rec_speech(eci, s1, s2, s3, s4, s5).SVM_make()
			

			context = {'vtt' : m_return,
						's1':  s1,
						's2':  s2,
						's3' : s3,
						's4' : s4,
						's5' : s5,
						'disease': aa }
			return render_to_response('audio/speech_save.html',  context)
		else:
			return render_to_response('audio/speech_save.html')

