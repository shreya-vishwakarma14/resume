from django.shortcuts import render
from .models import Consigner,Consignee
# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from .process import html_to_pdf 

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
         
        # getting the template
        pdf = html_to_pdf('html_files/invoice.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')



def display_data(request):
    consignerData = Consigner.objects.all() 
    consigneeData = Consignee.objects.all()
    context ={
        'consignerData': consignerData,
        'consigneeData' : consigneeData,
    }# Fetch all instances of YourModel
    return render(request, 'html_files/invoice.html',context)



# def home_invoice(request):
#     return render(request, 'html_files/invoice.html')
# def demo_page(request):
#     return render(request, 'html_files/pdf_template.html')
