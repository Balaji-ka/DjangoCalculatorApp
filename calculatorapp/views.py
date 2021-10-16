import math

from django.shortcuts import render
from django.http import HttpResponse

# Create your viewgs here.
def index(request):
    return render(request,'index.html')

def submitquery(request):
    q=request.GET['query']
    try:
        #ans=eval(q)
        if q[:4]=="sinr" or q[:4]=="Sinr":
           ans=math.sin(int(q[5:-1]))
        elif q[:4]=="cosr" or q[:4]=="Cosr":
            ans=math.cos(int(q[5:-1]))
        elif q[:4]=="tanr" or q[:4]=="Tanr" :
            ans=math.tan(int(q[5:-1]))
        elif q[:6]=="cosecr" or q[:6]=="Cosecr":
            ans=1/(math.sin((int(q[7:-1]))))
        elif q[:4]=="secr" or q[:4]=="Secr":
            ans=1/(math.cos(int(q[5:-1])))
        elif q[:4]=="cotr" or q[:4]=="Cotr":
            ans=1/(math.tan(int(q[5:-1])))

        elif q[:3]=="sin" or q[:3]=="Sin":
           ans=math.sin(math.radians(float(q[4:-1])))
        elif q[:3]=="cos" or q[:3]=="Cos":
           ans=math.cos(math.radians(float(q[4:-1])))
        elif q[:3]=="tan" or q[:3]=="Tan":
           ans=math.tan(math.radians(float(q[4:-1])))
        elif q[:3]=="sec" or q[:3]=="Sec":
           ans=1/math.cos(math.radians(float(q[4:-1])))
        elif q[:3]=="cot" or q[:3]=="Cot":
           ans=1/math.tan(math.radians(float(q[4:-1])))
        elif q[:3]=="log" or q[:3]=="Log":
           ans=math.log10(int(q[4:-1]))
        else:
            ans=eval(q)
                    

        dic={
            "q":q,
            "ans":ans,
            "error":False,
            "result":True
        }
        return render(request,'index.html',context=dic)
    except:
        dic={
            "error":True,
            "result":False
        }
        return render(request,'index.html',context=dic)
