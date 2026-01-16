from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Member, MembershipPayment, Event, Expenditure
from .forms import MemberForm, MembershipPaymentForm, EventForm, ExpenditureForm

# =========================
# Main Dashboard
# =========================
def dashboard(request):
    total_members = Member.objects.count()
    membership_income = MembershipPayment.objects.aggregate(total=Sum('amount'))['total'] or 0
    event_income = Event.objects.aggregate(total=Sum('income'))['total'] or 0
    expense = Expenditure.objects.aggregate(total=Sum('amount'))['total'] or 0

    final_income = membership_income + event_income - expense

    context = {
        'total_members': total_members,
        'membership_income': membership_income,
        'event_income': event_income,
        'expense': expense,
        'final_income': final_income
    }

    return render(request, 'core/dashboard_main.html', context)

# =========================
# Member CRUD
# =========================
def add_member(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_dashboard')
    else:
        form = MemberForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Member'})

def edit_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    form = MemberForm(request.POST or None, instance=member)
    if form.is_valid():
        form.save()
        return redirect('member_dashboard')
    return render(request, 'core/form.html', {'form': form, 'title': 'Edit Member'})

def delete_member(request, pk):
    member = get_object_or_404(Member, pk=pk)
    member.delete()
    return redirect('member_dashboard')

# =========================
# Membership Payment CRUD
# =========================
def add_payment(request):
    if request.method == "POST":
        form = MembershipPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment_dashboard')
    else:
        form = MembershipPaymentForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Membership Payment'})

# =========================
# Event CRUD
# =========================
def add_event(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_dashboard')
    else:
        form = EventForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Event'})

# =========================
# Expenditure CRUD
# =========================
def add_expenditure(request):
    if request.method == "POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_dashboard')
    else:
        form = ExpenditureForm()
    return render(request, 'core/form.html', {'form': form, 'title': 'Add Expenditure'})

# =========================
# Separate Segment Dashboards
# =========================
def member_dashboard(request):
    members = Member.objects.all()
    return render(request, 'core/dashboard_members.html', {'members': members})

def payment_dashboard(request):
    payments = MembershipPayment.objects.all()
    return render(request, 'core/dashboard_payments.html', {'payments': payments})

def event_dashboard(request):
    events = Event.objects.all()
    return render(request, 'core/dashboard_events.html', {'events': events})

def expense_dashboard(request):
    expenses = Expenditure.objects.all()
    return render(request, 'core/dashboard_expenses.html', {'expenses': expenses})
