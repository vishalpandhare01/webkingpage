from django.shortcuts import redirect, render
from .models import Survey

# Create your views here.
def survey(request):
   if request.method=='POST':
      full_name=request.POST.get('full_name')
      age=request.POST.get('age')
      responsive_web=request.POST.get('responsive_web')
      web_desing=request.POST.get('web_desing')
      web_speed=request.POST.get('web_speed')
      service=request.POST.get('service')
      message=request.POST.get('message')
      feedback=request.POST.get('feedback')
      rating=request.POST.get('rating')

      form=Survey.objects.create(
         full_name=full_name,
         age=age,
         responsive_web=responsive_web,
         web_desing=web_desing,
         web_speed=web_speed,
         service=service,
         message=message,
         feedback=feedback,
         rating=rating
         )
      form.save()
      print('data submited')
      return render(request,'thx.html')

    
   return render(request,'form.html')

