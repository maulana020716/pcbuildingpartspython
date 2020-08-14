from django import forms
from sim.models import Motherboard,Cpu,Vga,Storage,Ram,Simulation

class MtbPostForm(forms.ModelForm):

    class Meta:
        model = Motherboard
        fields = ['name', 'socket','mem_type','vga_interface','str_interface','price','thumb_pic']

class SimPostForm(forms.ModelForm):

    class Meta:
        model = Simulation
        fields = ['build_name','mtb_name','cpu_name','vga_name','ram_name','str_name']
