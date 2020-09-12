from django import forms
from sim.models import Motherboard,Cpu,Vga,Storage,Ram,Simulation

class MtbPostForm(forms.ModelForm):

    class Meta:
        model = Motherboard
        fields = ['name', 'socket','mem_type','vga_interface','str_interface','price','thumb_pic']

class SimPostForm(forms.ModelForm):

    class Meta:
        model = Simulation
        fields = ['mtb_name','cpu_name','vga_name','ram_name','str_name']

class DssPostForm(forms.ModelForm):

    class Meta:
        model = Simulation
        fields = ['cpu_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["cpu_name"].label = "Pilih Cpu"

class DssPostFormRam(forms.ModelForm):

    class Meta:
        model = Simulation
        fields = ['ram_name']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["ram_name"].label = "Pilih Ram"
