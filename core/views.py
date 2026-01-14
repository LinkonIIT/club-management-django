from django.shortcuts import render, redirect, get_object_or_404
from .models import Member, MembershipPayment, Event, Expenditure
from .forms import MemberForm, MembershipPaymentForm, EventForm, ExpenditureForm
from .utils import get_final_income

# Dashboard
def dashboard(request):
    members = Member.objects.all()
    payments = MembershipPayment.objects.all()
    events = Event.objects.all()
    expenses = Expenditure.objects.all()
    final_income = get_final_income()

    context = {
        'members': members,
        'payments': payments,
        'events': events,
        'expenses': expenses,
        'final_income': final_income,
    }
    return render(request, 'core/dashboard.html', context)

# Member CRUD
def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MemberForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Member'})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    return render(request, 'core/form.html', {'form': form, 'title': 'Edit Member'})

def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('dashboard')

# Membership Payment CRUD
def add_payment(request):
    if request.method == "POST":
        form = MembershipPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = MembershipPaymentForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Membership Payment'})

# Event CRUD
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = EventForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Event'})

# Expenditure CRUD
def add_expenditure(request):
    if request.method == "POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ExpenditureForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Expenditure'})
