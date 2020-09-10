from django.urls import path

from .views import MotherboardView, CreateMtbView, MtbDetailView, CpuView, CpuDetailView,DssPostViewCpu,DssPostViewCpu4,DssPostViewCpu3,DssPostViewCpu2, VgaView, VgaDetailView, RamView,DssPostViewCpu1, RamDetailView, StorageView, StorageDetailView, CreateSimView, CreateSimView1, SimRes, SimRes1, DssPostView,DssRestView

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
    path('simulation/post1', CreateSimView1, name='sim_post1'),
    path('simulation/result', SimRes, name='sim_res'),
    path('simulation/dssform', DssPostView, name='dss_form'),
    path('simulation/dssformcpu', DssPostViewCpu, name='dss_form_cpu'),
    path('simulation/dssformcpu1', DssPostViewCpu1, name='dss_form_cpu1'),
    path('simulation/dssformcpu2', DssPostViewCpu2, name='dss_form_cpu2'),
    path('simulation/dssformcpu3', DssPostViewCpu3, name='dss_form_cpu3'),
    path('simulation/dssformcpu4', DssPostViewCpu4, name='dss_form_cpu4'),
    path('simulation/dssrest', DssRestView.as_view(), name='dss_rest'),
]
