from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.


def month_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    text = None
    if month.lower() == "january":
        text = "january challenge"
    elif month.lower() == "february":
        text = "february challenge"
    elif month.lower() == "march":
        text = "march challenge"
    elif month.lower() == "april":
        text = "april challenge"
    elif month.lower() == "may":
        text = "may challenge"
    elif month.lower() == "june":
        text = "june challenge"
    elif month.lower() == "july":
        text = "july challenge"
    elif month.lower() == "august":
        text = "august challenge"
    elif month.lower() == "september":
        text = "september challenge"
    elif month.lower() == "october":
        text = "october challenge"
    elif month.lower() == "november":
        text = "november challenge"
    elif month.lower() == "december":
        text = "december challenge"
    else:
        text = "invalid month"
        return HttpResponseNotFound(f"{text} nano ka")
    return HttpResponse(f"{text} time mga paps!")
