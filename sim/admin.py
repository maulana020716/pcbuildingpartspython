from django.contrib import admin
from sim.models import Motherboard,Cpu,Storage,Vga,Ram,Simulation
# Register your models here.

admin.site.register(Motherboard)
admin.site.register(Cpu)
admin.site.register(Storage)
admin.site.register(Vga)
admin.site.register(Ram)
admin.site.register(Simulation)
