from django.shortcuts import render
import joblib
import numpy as np 
import math


def home(request):
    return render(request, "home.html")
    #prediction = model.predict([lis])
    #model = joblib.load('Final.sav')
from django.utils.datastructures import MultiValueDictKeyError

def result(request):  
        
    #cls1 = joblib.load('Battery_25_28.sav')

    cls1 = joblib.load('Battery_29_32.sav')
    
    cls2 = joblib.load('Battery_33_36.sav')
    
    cls3 = joblib.load('Battery_38_40.sav')
    
    cls4 = joblib.load('Battery_41_44.sav')
    
    cls5 = joblib.load('BatteryAgingARC_25_26_27_28_P1.sav')
    
    cls6 = joblib.load('BatteryAgingARC_45_46_47_48.sav')
    
    #cls8 = joblib.load('BatteryAgingARC_49_50_51_52.sav')
    
    cls7 = joblib.load('BatteryAgingARC_53_54_55_56.sav')
    
    lis = []

    if request.GET['Model']=='2':
        model = cls1
    elif request.GET['Model']=='3':
        model = cls2
    elif request.GET['Model']=='4':
        model = cls3
    elif request.GET['Model']=='5':
        model = cls4
    elif request.GET['Model']=='6':
        model = cls5
    elif request.GET['Model']=='7':
        model = cls6
    elif request.GET['Model']=='8':
        model = cls7
    # elif request.GET['Model']=='8':
    #     model = cls8
    
    lis.append(request.GET['CYC'])
    x = float(request.GET['VOL'])

    #pred
    prediction = model.predict(np.asarray([lis[0]]).reshape(-1,1))[0]
    prediction = f'{prediction : 0.3f} Ah '

    #no of remaining cycles
    n = int(lis[0])
    cap = math.inf

    temp = None
    cap1 = model.predict(np.asarray(n).reshape(-1,1))[0]
    
    isbool = True

    if cap1<x:
        prediction = cap1
        rul = "0"
        isbool = False
   
    if isbool:
        while cap > x:
            if(cap!=temp):
                temp = cap
            cap = model.predict(np.asarray(n).reshape(-1,1))[0]
            if cap == temp:
                prediction = "___!!!___ Invalid value: Value out of Bounds ___!!!___"
                rul = "___!!!___ Invalid value: Value out of Bounds ___!!!___"
                break
            print(cap)
            n+=1

            #RUL
            rul = n-int(lis[0])

    print(rul)
    return render(request,"result.html",{'prediction': prediction,'rul':rul})


def graphs(request):
    return render(request,"graphs.html")
