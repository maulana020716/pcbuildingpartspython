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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["mtb_name"].label = "Motherboard"
        self.fields["cpu_name"].label = "Cpu"
        self.fields["vga_name"].label = "Vga"
        self.fields["ram_name"].label = "Ram"
        self.fields["str_name"].label = "Storage"
