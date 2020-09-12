from django.urls import path

from .views import (MotherboardView, CreateMtbView, MtbDetailView, CpuView,
CpuDetailView,DssPostViewCpu,DssPostViewRam, DssPostViewRam1, DssPostViewRam2,
DssPostViewRam3, DssPostResRam, DssPostViewCpu4,DssPostViewCpu3,DssPostViewVga,
DssPostViewVga1,DssPostViewVga2,DssPostViewVga3,DssPostViewVga4,DssPostViewVga5,
DssRestViewVga,DssPostViewCpu2, VgaView, VgaDetailView, RamView,DssPostViewCpu1,
DssPostViewStr,DssPostViewStr1,DssPostViewStr2,DssRestViewStr,
RamDetailView,StorageView, StorageDetailView, CreateSimView, CreateSimView1,
SimRes, SimRes1, DssPostView,DssRestView)

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
    path('simulation/dssformram', DssPostViewRam, name='dss_form_ram'),
    path('simulation/dssformram1', DssPostViewRam1, name='dss_form_ram1'),
    path('simulation/dssformram2', DssPostViewRam2, name='dss_form_ram2'),
    path('simulation/dssformram3', DssPostViewRam3, name='dss_form_ram3'),
    path('simulation/dssresram', DssPostResRam, name='dss_res_ram'),
    path('simulation/dssformvga', DssPostViewVga, name='dss_form_vga'),
    path('simulation/dssformvga1', DssPostViewVga1, name='dss_form_vga1'),
    path('simulation/dssformvga2', DssPostViewVga2, name='dss_form_vga2'),
    path('simulation/dssformvga3', DssPostViewVga3, name='dss_form_vga3'),
    path('simulation/dssformvga4', DssPostViewVga4, name='dss_form_vga4'),
    path('simulation/dssformvga5', DssPostViewVga5, name='dss_form_vga5'),
    path('simulation/dssresvga', DssRestViewVga, name='dss_res_vga'),
    path('simulation/dssformstr', DssPostViewStr, name='dss_form_str'),
    path('simulation/dssformstr1', DssPostViewStr1, name='dss_form_str1'),
    path('simulation/dssformstr2', DssPostViewStr2, name='dss_form_str2'),
    path('simulation/dssresstr', DssRestViewStr, name='dss_res_str'),
]
