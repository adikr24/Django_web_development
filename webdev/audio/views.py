from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.shortcuts import render_to_response	
from django.template.loader import get_template	
from django.views.decorators.csrf import csrf_exempt
from audio.models import db_design, speech , store_syn, speech_to_symptoms, speech_symptoms
from django.utils.decorators import method_decorator
from audio.python_codes import algo, clean_up
from audio.python_codes.algo import rec_speech
from audio.python_codes.clean_up import text_clean
from datetime import date
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
import pandas as pd



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
			post = speech_symptoms()
			
			m_return = request.POST.get("lang")
			####### 			
			### symptoms
			today = date.today()
			

			my_sentence = request.POST.get("lang")
			eci = '100011'
			s1,s2,s3,s4,s5=text_clean(my_sentence).clean_words()
			aa= rec_speech(eci, s1, s2, s3, s4, s5).SVM_make()
			
			severe_list = ['Bronchial Asthma','Paralysis (brain hemorrhage)','Typhoid','Heart attack','Peptic ulcer disease','Gastroenteritis']
			if aa in severe_list:
				severe = "Your symptoms are severe!! your nurse is informed."
				ss = "SEVERE"
			else:
				severe = "Your symptoms are mild but we have noted it down for your doc's next visit."
				ss = "NON SEVERE"

			context = {'vtt' : m_return,
						's1':  s1,
						's2':  s2,
						's3' : s3,
						's4' : s4,
						's5' : s5,
						'disease': aa,
						'severity':  severe }
			post.severity= ss
			post.date_logged = today
			post.eci_id = request.POST.get('eci_id')
			post.voice_to_text= request.POST.get('lang')
			post.symptom1 = s1
			post.symptom2 = s2
			post.symptom3 = s3
			post.symptom4 = s4
			post.symptom5 = s5
			post.ailment = 	aa
			
			post.save()
			return render_to_response('audio/speech_save.html',  context)
		else:
			return render_to_response('audio/speech_save.html')


def doctors_view(request):
	return render_to_response('audio/patient_info.html')


def pat_data(request):
	eci = request.GET['eci_id']
	#eci= 1
	fname = request.GET['fname']
	
	ss= speech_symptoms.objects.all()
	
	syms= []	
	for i in ss:
		syms.append(str(i))

	
	severity=[]
	ECI_ID=[]
	Ailment=[]
	Symptom1=[]
	Symptom2=[]
	Symptom3=[]
	Symptom4=[]
	Symptom5=[]
	Date_logged=[]
	all_syms= []
	for ii in syms:
	    severity.append(ii.split(',')[0])
	    ECI_ID.append(ii.split(',')[1])
	    Ailment.append(ii.split(',')[2])
	    Symptom1.append(ii.split(',')[3])
	    Symptom2.append(ii.split(',')[4])
	    Symptom3.append(ii.split(',')[5])
	    Symptom4.append(ii.split(',')[6])
	    Symptom5.append(ii.split(',')[7])
	    Date_logged.append(ii.split(',')[8])


	
	d= {'Severity':severity, 'ECI_ID': ECI_ID, 'Ailment':Ailment, 'Symptom1':Symptom1,'Symptom2':Symptom2, 'Symptom3':Symptom3,'Symptom4':Symptom4,'Symptom5':Symptom5, 'Date_logged':Date_logged}
	df_info= pd.DataFrame(d)
	df_info= df_info[df_info['ECI_ID']==eci]

	time_stamp=[]
	for i in range(0,df_info.shape[0]):
	 	tt = datetime.strptime(df_info['Date_logged'][i], '%Y-%m-%d')
	 	time_stamp.append(tt)

	df_info['Date_logged'] = time_stamp
	
# # #	ll= df_info['Date_logged'][0]
	times_logged=df_info.groupby('Date_logged').count()['Severity'][0]

    
	
	all_syms.extend(Symptom1)
	all_syms.extend(Symptom2)
	all_syms.extend(Symptom3)
	all_syms.extend(Symptom4)
	all_syms.extend(Symptom5)

	def most_frequent(List):
		return max(set(List), key = List.count)



	mf_val= most_frequent(all_syms)
	mf_val= mf_val.replace("_"," ")

	df_ail=df_info[df_info['ECI_ID']==eci]['Ailment']
	
	non_sev=0
	sev_=0
	for i in range(len(df_info)):
	    if df_info['Severity'][i]== 'NON SEVERE':
	        non_sev +=1
	    elif df_info['Severity'][i]== 'SEVERE':
	        sev +=1

# 	#last_val = ll
	print(times_logged, mf_val )
	context = {'eci_id': eci, 'fname': fname, 
				'time_logged': times_logged,
				'most_frequent_symptom': mf_val,
				'ailment': df_ail ,
				'non_sev_times': non_sev,
				'sev_times': sev_ 
				}
	return render_to_response('audio/patient_data.html', context)