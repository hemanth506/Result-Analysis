from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .forms import *
from .models import Credential

# Create your views here.

def details(req):
    submitted = False
    if req.method == 'POST':
        # urldata = Credential.objects.get()
        form = CredentialForm(req.POST)
        if form.is_valid():
            form.save() 
            # print(req.POST)
            return HttpResponseRedirect('/api/student')
        else:
            form = CredentialForm()
            if 'submitted' in req.GET:
                submitted = True
        list = Credential.objects.all()
    elif req.method == 'GET':
        form = CredentialForm()
        list = Credential.objects.all()
        # print(list)

    print(list)
    context = {'form' : form, 'submitted' : submitted, 'list': list}
    return render(req,'details.html', context)

def addMark(req):
    submitted = False
    if(req.method == 'POST'):
        form = MarkForm(req.POST)
        #print(req.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/api/student/add-mark')
        else:
            form = MarkForm()
            if 'submitted' in req.GET:
                submitted = True
        list = Report.objects.all().distinct()
    elif req.method == 'GET':
        form = MarkForm()
        # list = Report.objects.all().distinct()
        list = Report.objects.order_by('credential')

    print(list)
    context = {'form' : form, 'submitted' : submitted, 'list': list}
    return render(req,'addMark.html', context)

def result(req):
    if req.method == 'GET' :
        count_of_std = Report.objects.all().count()
        #print(count_of_std)


        grade = Report.objects.values('mark')
        AGrade = []
        BGrade = []
        CGrade = []
        DGrade = []
        EGrade = []
        FGrade = []
        len_A = len_B = len_C = len_D = len_E = len_F = 0
        for grd in grade:
            if grd['mark'] <= 100 and grd['mark'] >= 91:
                AGrade.append(grd['mark'])
                len_A = len(AGrade)
            elif grd['mark'] <= 90 and grd['mark'] >= 81:
                BGrade.append(grd['mark'])
                len_B = len(BGrade)
            elif grd['mark'] <= 80 and grd['mark'] >= 71:
                CGrade.append(grd['mark'])
                len_C = len(CGrade)
            elif grd['mark'] <= 70 and grd['mark'] >= 61:
                DGrade.append(grd['mark'])
                len_D = len(DGrade)
            elif grd['mark'] <= 60 and grd['mark'] >= 55:
                EGrade.append(grd['mark'])
                len_E = len(EGrade)
            else:
                FGrade.append(grd['mark'])
                len_F = len(FGrade)

        """
        print(AGrade)
        print(BGrade)
        print(CGrade)
        print(DGrade)
        print(EGrade)
        print(FGrade)
        """

        distinction = (round((len(AGrade) / count_of_std), 2) *100)

        firstclass = (round(((len(BGrade) + len(CGrade)) / count_of_std), 2) *100)

        passpercent = (round(((count_of_std - len(FGrade)) / count_of_std),2) *100)

        count_each_grp = {
            'A': len_A,
            'B': len_B,
            'C': len_C,
            'D': len_D,
            'E': len_E,
            'F': len_F
        }
        content = {'count_of_std' : count_of_std, 'count_each_grp' : count_each_grp, 'distinction' :distinction, 'firstclass' :firstclass, 'pass':passpercent}
    return render(req,'result.html',content)



def update(req,id):
    print("Hemanth")
    obj = get_object_or_404(Credential, id=id)
    if req.method == 'POST':
        # urldata = Credential.objects.get(id=id)
        form = CredentialForm(req.POST, instance=obj)
        if form.is_valid():
            form.save() 
            # print(req.POST)
            return HttpResponseRedirect('/api/student')
        list = Credential.objects.all()
    else:
        form = CredentialForm()
    content = {'form': form}
    return render(req,'update.html',content)

def delete(req,id):
    obj = get_object_or_404(Credential, id=id)
    obj.delete()
    return HttpResponseRedirect('/api/student')
    
