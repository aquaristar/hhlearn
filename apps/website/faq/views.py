from django.shortcuts import render
import datetime

from apps.utility.models import *
from apps.dashboard.models import *


def faq(request):
    faq_categories = UtilFaqCategories.objects.filter(is_active=True).order_by('title')
    faq_datas = []
    for category in faq_categories:
        faqs = UtilFaqs.objects.filter(faq_category=category)
        faq_datas.append(faqs)
    faqs = zip(faq_categories, faq_datas)
    return render(request, 
                  'website/faq/index.html', 
                  {'request': request,
                   'categories': faq_categories,
                   'faqs': faqs,
                   })
