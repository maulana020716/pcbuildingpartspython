from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView # new
from django.urls import reverse_lazy # new
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MtbPostForm, SimPostForm # new
from .models import Motherboard,Cpu,Vga,Ram,Storage,Simulation
from django.db.models import Q, Count
def is_valid_queryparam(param):
    return param != '' and param is not None

def MotherboardView(request):
    mtb = filtermtb(request)
    context = {
        'queryset': mtb,
    }
    return render(request, "mtb.html", context)

def filtermtb(request):
    mtb = Motherboard.objects.all()
    name_contains_query = request.GET.get('name_contains')


    if is_valid_queryparam(name_contains_query):
        mtb = mtb.filter(name__icontains=name_contains_query)


    return mtb

class MtbDetailView(DetailView):
    model = Motherboard
    template_name = 'mtb_detail.html'

def CpuView(request):
    cpu = filtercpu(request)
    context = {
        'queryset': cpu,
    }
    return render(request, "cpu.html", context)

def filtercpu(request):
    cpu = Cpu.objects.all()
    name_contains_query = request.GET.get('name_contains')

    if is_valid_queryparam(name_contains_query):
        cpu = cpu.filter(name__icontains=name_contains_query)

    return cpu

class CpuDetailView(DetailView):
    model = Cpu
    template_name = 'cpu_detail.html'

def VgaView(request):
    vga = filtervga(request)
    context = {
        'queryset': vga,
    }
    return render(request, "vga.html", context)

def filtervga(request):
    vga = Vga.objects.all()
    name_contains_query = request.GET.get('name_contains')

    if is_valid_queryparam(name_contains_query):
        vga = vga.filter(name__icontains=name_contains_query)

    return vga

class VgaDetailView(DetailView):
    model = Vga
    template_name = 'vga_detail.html'

def RamView(request):
    ram = filterram(request)
    context = {
        'queryset': ram,
    }
    return render(request, "ram.html", context)

def filterram(request):
    ram = Ram.objects.all()
    name_contains_query = request.GET.get('name_contains')

    if is_valid_queryparam(name_contains_query):
        ram = ram.filter(name__icontains=name_contains_query)

    return ram

class RamDetailView(DetailView):
    model = Ram
    template_name = 'ram_detail.html'

def StorageView(request):
    storage = filterstr(request)
    context = {
        'queryset': storage,
    }
    return render(request, "storage.html", context)

def filterstr(request):
    storage = Storage.objects.all()
    name_contains_query = request.GET.get('name_contains')

    if is_valid_queryparam(name_contains_query):
        storage = storage.filter(name__icontains=name_contains_query)

    return storage

class StorageDetailView(DetailView):
    model = Storage
    template_name = 'storage_detail.html'

class CreateMtbView(LoginRequiredMixin, CreateView): # new
    login_url = '/login/'
    model = Motherboard
    form_class = MtbPostForm
    template_name = 'mtb_post.html'
    redirect_field_name = 'sim/mtb.html'

class CreateSimView(LoginRequiredMixin, CreateView): # new
    login_url = '/login/'
    model = Simulation
    form_class = SimPostForm
    template_name = 'sim_post.html'
    redirect_field_name = 'sim/sim.html'

    # def SimReq(request):
    #     sim = simpost(request)
    #     context = {
    #         'queryset': sim,
    #     }
    #     return render(request, 'sim_post.html', context)
    #
    #
    # def simpost(request):
    #     mtb = Motherboard.objects.all()
    #     cpu = Cpu.objects.all()
    #     vga = Vga.objects.all()
    #     ram = Ram.objects.all()
    #     storage = Storage.objects.all()
    #     mtbform = request.GET.get('mtb_name')
    #     cpuform = request.GET.get('cpu_name')
    #     vgaform = request.GET.get('vga_name')
    #     ramform = request.GET.get('ram_name')
    #     strform = request.GET.get('str_name')
    #
    #     if is_valid_queryparam(mtbform):
    #         sim = Cpu.objects.raw(select socket from cpu where name = cpu_name )
