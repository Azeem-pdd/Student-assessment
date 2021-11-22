from django.db.models import query
from django.http import request
from django.http import response
from django.http import HttpResponseRedirect, HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import CreateTestForm, ResponseDetailsForm,TestDetailsForm, AddQuestionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import Responses, Test,TestDetails,Question,Choices, Selcted_choices
from accounts.models import User
import clipboard as c
from django.template.loader import get_template

from django.urls import reverse
from urllib.parse import urlencode

from xhtml2pdf import pisa

import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
# Create your views here.
class DashboardView(View):
    def get(self, request, cont=None):
        print(cont)
        if cont is not None:
            context={}
            context['responses']=cont
        context={}
        if request.user.is_authenticated:
            user=request.user
            try:
                tests=Test.objects.filter(user=user)
                tests = tests.extra(order_by = ['test_title'])
            except User.DoesNotExist:
                tests=None
            context['tests']=tests
        return render(request, 'dashboard.html', context)
    
    def post(self, request):
        testId=request.POST.get('test')
        accept=request.POST.get('accept')
        stop=request.POST.get('stop')
        copy=request.POST.get('copy')
        responses=request.POST.get('responses')
        
        context={}
        try:
            test_obj=Test.objects.get(id=testId)
        except Test.DoesNotExist:
            test_obj=None
        if test_obj:
            if accept:
                test_obj.accept=True
            elif stop:
                test_obj.accept=False
            test_obj.save()
            if copy:
                user_obj=request.user
                test_identifier=test_obj.identifier
                user_identifier=user_obj.identifier
                if test_identifier is not None and user_identifier is not None:
                    link=('http://127.0.0.1:8000/tests/attempt/'+user_identifier+'/'+test_identifier)
                    c.copy(link)
            elif responses:
                request.session['testId']=test_obj.id
                return redirect('responses')
            
            
        return redirect('dashboard')
class ResponsesView(View):
    def get(self, request):
        testId=None
        resId=None
        context={}
        testId=request.session.get('testId')
        resId=request.session.get('rID')
        user_obj=request.user
        try:
            test_obj=Test.objects.get(pk=testId)
        except:
            test_obj=None
        try:
            res_obj=Responses.objects.get(pk=resId)
        except:
            res_obj=None
        if test_obj is not None and res_obj is not None and user_obj is not None:
            q_objs=Question.objects.filter(test=test_obj)
            objs=Selcted_choices.objects.filter(res_obj=res_obj)
            ids=[]
            for obj in objs:
                ids.append(obj.c_id)
        
            context['questions']=q_objs
            context['ids']=ids
            del request.session['rID']
            
            #using xhtml2pdf library
            
            # template_path='html2pdf.html'
            # response=HttpResponse(content_type='application/pdf')
            # response['Content-Disposition']='filename={}.pdf'.format(res_obj.id)
            # template=get_template(template_path)
            # html=template.render(context)
            # pisa_status=pisa.CreatePDF(html, dest=response)
            # if pisa_status.error:
            #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
            # return response
            
            
            #using reportlab library
            
            
            # buf=io.BytesIO()
            # c=canvas.Canvas(buf, pagesize=letter, bottomup=0)
            # text_obj=c.beginText()
            # text_obj.setTextOrigin(inch, inch)
            # text_obj.setFont('Helvetica', 12)
            # lines=[
                
            # ]
            # for q in q_objs:
            #     lines.append(q.question)
            # for line in lines:
            #     text_obj.textLine(line)
            
            # c.drawText(text_obj)
            # c.showPage()
            # c.save()
            # buf.seek(0)
            
            # return FileResponse(buf, as_attachment=True, filename='response.pdf')

            return render(request, 'show_responses.html', context)
        elif test_obj is not None and user_obj is not None:
            
            
                
            if request.user.is_authenticated:
                user_obj=request.user
                try:
                    res_objs=Responses.objects.filter(test=test_obj, user=user_obj)
                except Responses.DoesNotExist:
                    res_objs=None
                
                context['responses']=res_objs
                return render(request, 'show_responses.html', context)
            else:
                return redirect('/accounts/login')
            
        return redirect('login')
    def post(self, request):
        
        
        resID=request.POST.get('res')
        if resID:
            request.session['rID']=resID
            return redirect('responses')
            


class IndexView(View):
    
    def get(self, request):
        return render(request, 'index.html')
class CreateView(View):
    def get(self, request):
        form=CreateTestForm()
        context={}
        context['form']=form
        return render(request, 'create.html', context)
    def post(self, request):
        user=request.session.get('user')
        form=CreateTestForm(request.POST or None)
        context={}
        if form.is_valid():
            title=form.cleaned_data['test_title']
            if request.user.is_authenticated:
                user=request.session.get('user')
                user=User.objects.get(id=user)
                identifier=title+'eem'
                identifier=make_password(identifier)
                ident=identifier.split('/')
                id=''
                for i in ident:
                    id=i+id
                test=Test(user=user, test_title=title, identifier=id )
                test.save()
                request.session['test']=test.id
                return redirect('test_detail')
            else:
                return redirect('login')
            
class TestDetailView(View):
    def get(self, request):
        context={}
        form=TestDetailsForm()
        context['form']=form
        return render(request,'create.html', context)
    def post(self, request):
        form=TestDetailsForm(request.POST or None)
        if form.is_valid():
            test_total_time=form.cleaned_data['test_total_time']
            no_of_questions=form.cleaned_data['no_of_questions']
            marks=form.cleaned_data['marks']
            test=request.session.get('test')
            user=request.session.get('user')
            if test is not None and user is not None:
                test=Test.objects.get(id=test)
                user=User.objects.get(id=user)
                test_details=TestDetails(user=user,
                                         test=test,
                                         test_total_time=test_total_time,
                                         no_of_questions=no_of_questions,
                                         marks=marks)
                test_details.save()
                return redirect('question')
            else:
                if user is None:
                    return redirect('login')
                elif test is None:
                    redirect('create')
            
        return redirect('test_detail')
    
class QuestionView(View):
    def get(self, request):
        context={}
        form=AddQuestionForm()
        context['form']=form
        return render(request,'question.html', context)
    def post(self, request):
        form=AddQuestionForm(request.POST or None)
        if form.is_valid():
            
            #get test from session
            test=request.session.get('test')
            test=Test.objects.get(id=test)
            
            obj=TestDetails.objects.get(test=test)
            length=obj.no_of_questions
            no_of_objs=Question.objects.filter(test=test).count()
            question=form.cleaned_data['question']
            choice1=form.cleaned_data['choice1']
            choice2=form.cleaned_data['choice2']
            choice3=form.cleaned_data['choice3']
            choice4=form.cleaned_data['choice4']
            correct=form.cleaned_data['correct']
            
            if no_of_objs<length:
                dict={'1':choice1,'2':choice2,'3':choice3,'4':choice4}
                correct=dict[correct]
                choices=[choice1,choice2,choice3,choice4]
                question=Question(test=test, question=question)
                question.save()
                for choice in choices:
                    
                    choicesss=Choices(choice=choice, question=question)
                    if choice==correct:
                        choicesss.correct=True
                    choicesss.save()
                if no_of_objs+1 == length:
                    return redirect('confirm')
                else:
                    return redirect('question')
            else:
                return redirect('confirm')
        return redirect('question')
class ConfirmView(View):
    def get(self, request):
        test=request.session.get('test')
        user=request.session.get('user')
        
        testobj=None
        user_identifier=None
        test_identifier=None
        data=request.GET.get('data')
        
        
        try:
            userobj=User.objects.get(id=user)
            
        except:
            pass
        
        try:
            testobj=Test.objects.get(id=test)
            
        except:
            pass
        
        try:
            questions=Question.objects.filter(test=test)
        except:
            pass
        
        context={}
        context['questions']=questions
        context['Choices']=Choices
        
        if data:
            if userobj is not None and testobj is not None:
                user_identifier=userobj.identifier
                test_identifier=testobj.identifier
                
                
                if test_identifier is not None and user_identifier is not None:
                    
                    link=('http://127.0.0.1:8000/tests/attempt/'+user_identifier+'/'+test_identifier)
                    
                else:
                    link=None
                context['link']=link
            
        
        return render(request,'confirm.html', context)
    def post(self, request):
        link=request.POST.get('link')
        c.copy(link)
        path=request.get_full_path()
        return redirect(path)
class AttemptView(View):
    def get(self, request,user_identifier=None, test_identifier=None, accept=None, con=None):
        context={}
        
        
        
        if user_identifier is not None and test_identifier is not None:
            try:
                user=User.objects.get(identifier=user_identifier)
                test=Test.objects.get(identifier=test_identifier)
            except:
                user=None
                test=None
            
            if accept is None:
                if user is not None and test is not None:
                    if test.accept==False:
                        return HttpResponse('This test is not accepting responses anymore. Try contacting owner of test.')
                    else:
                        form=ResponseDetailsForm()
                        context['form']=form
                else:
                    return HttpResponse('Test you are looking for not Found or link was invalid.')
            elif accept=='ok' and con is None:
                if user is not None and test is not None:
                    if test.accept==False:
                        return HttpResponse('This test is not accepting responses anymore. Try contacting owner of test.')
                    else:
                        details=TestDetails.objects.get(test=test, user=user)
                else:
                    return HttpResponse('Test you are looking for not Found or link was invalid.')
                link=user_identifier+'/'+test_identifier+'/ok'
                context['details']=details
                context['link']=link
            else:
                if user is not None and test is not None:
                    if test.accept==False:
                        return HttpResponse('This test is not accepting responses anymore. Try contacting owner of test.')
                    else:
                        questions=Question.objects.filter(test=test)
                else:
                    return HttpResponse('Test you are looking for not Found or link was invalid.')
                context['questions']=questions    
            
                
        else:
            return HttpResponse('Test you are looking for not Found or link was invalid.')
            
        
        
            
        return render(request,'attempt.html', context)
    
    def post(self, request, user_identifier=None, test_identifier=None, accept=None, con=None):
        r_id=None
        r_id=request.session.get('response')
        user=None
        test=None
        questions=None
        if user_identifier is not None and test_identifier is not None:
            try:
                user=User.objects.get(identifier=user_identifier)
                test=Test.objects.get(identifier=test_identifier)
                test_obj=TestDetails.objects.get(test=test, user=user)
                tot_q=test_obj.no_of_questions
                marks=test_obj.marks
                if r_id is not None:
                    res_obj=Responses.objects.get(id=r_id)
            except:
                pass
            if user is not None and test is not None:
                if test.accept==False:
                        return HttpResponse('This Test is not currently accepting responses. Try contacting the owner of this test')
                else:
                    if accept is None:
                        form=ResponseDetailsForm(request.POST or None)
                        
                        if form.is_valid():
                            obj=form.save(commit=False)
                            obj.test=test
                            obj.user=user
                            obj.total_no_of_questions=tot_q
                            obj.save()
                            request.session['response']=obj.id
                            url=request.get_full_path()+'/ok'
                            return redirect(url)
                            
                    elif accept is not None and con is not None:
                        questions=Question.objects.filter(test=test)
                        if questions is not None:
                            ids=[]
                            for q in questions:
                                ids.append(request.POST.get(str(q.id)))
                            correct=0
                            objs=[]
                            for id in ids:
                                try:
                                    obj=Choices.objects.get(id=id)
                                    objs.append(obj)
                                except:
                                    obj=None
                                if obj is not None and obj.correct==True:
                                    correct+=1
                            
                            res_obj.total_no_of_questions=tot_q
                            res_obj.correct_questions=correct
                            res_obj.obtained_marks=marks*correct
                            res_obj.save()
                            
                            for obj in objs:
                                a=Selcted_choices(res_obj=res_obj, c_id=obj.id)
                                a.save()
                            
                            return redirect('success')
            return HttpResponse('Test you are looking for not Found or link was invalid.')
        return HttpResponse('Test you are looking for was not Found.')
                    
class SuccessView(View):
    def get(self, request):
        return render(request,'success.html')
    
                        
                        
                            
                            
                            
                        
                        
                
            