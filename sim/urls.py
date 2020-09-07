from django.urls import path

from .views import MotherboardView, CreateMtbView, MtbDetailView, CpuView, CpuDetailView, VgaView, VgaDetailView, RamView, RamDetailView, StorageView, StorageDetailView, CreateSimView, SimRes, DssPostView,DssRestView

app_name = 'sim'

urlpatterns = [
    path('motherboard/', MotherboardView, name='mtb_home'),
    path('motherboard/post', CreateMtbView.as_view(), name='add_mtb_post'),
    path('motherboard/post/<int:pk>/', MtbDetailView.as_view(), name='mtb_detail'),
    path('cpu/', CpuView, name='cpu_home'),
    path('cpu/post/<int:pk>/', CpuDetailView.as_view(), name='cpu_detail'),
    path('vga/', VgaView, name='vga_home'),
    path('vga/post/<int:pk>/', VgaDetailView.as_view(), name='vga_detail'),
    path('ram/', RamView, name='ram_home'),
    path('ram/post/<int:pk>/', RamDetailView.as_view(), name='ram_detail'),
    path('storage/', StorageView, name='storage_home'),
    path('Storage/post/<int:pk>/', StorageDetailView.as_view(), name='storage_detail'),
    path('simulation/post', CreateSimView, name='sim_post'),
    path('simulation/result', SimRes, name='sim_res'),
    path('simulation/dssform', DssPostView, name='dss_form'),
    path('simulation/dssrest', DssRestView.as_view(), name='dss_rest'),
]
