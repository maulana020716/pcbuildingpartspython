from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Motherboard(models.Model):
    name            = models.CharField(blank=False, max_length=150)
    manufacturer    = models.CharField(blank=False, max_length=150,default=None)
    part            = models.CharField(blank=False, max_length=150,default=None)
    socket          = models.CharField(blank=False, max_length=150,default=None)
    form_factor     = models.CharField(blank=False, max_length=150,default=None)
    chipset         = models.CharField(blank=False, max_length=150,default=None)
    mem_max         = models.IntegerField(blank=False,default=0)
    mem_type        = models.CharField(blank=False, max_length=150,default=None)
    mem_slot        = models.IntegerField(blank=False,default=0)
    color           = models.CharField(blank=False, max_length=150,default=None)
    sli             = models.CharField(blank=False, max_length=150,default=None)
    pcie_16_slot    = models.IntegerField(blank=False,default=0)
    pcie_8_slot     = models.IntegerField(blank=False,default=0)
    pcie_4_slot     = models.IntegerField(blank=False,default=0)
    pcie_1_slot     = models.IntegerField(blank=False,default=0)
    m2_slot         = models.CharField(blank=False, max_length=150,default=None)
    msata_slot      = models.IntegerField(blank=False,default=0)
    on_ethernet     = models.CharField(blank=False, max_length=150,default=None)
    sata_6          = models.IntegerField(blank=False,default=0)
    on_video        = models.CharField(blank=False, max_length=150,default=None)
    usb_2_0_head    = models.IntegerField(blank=False,default=0)
    usb_3_2_head_gen1= models.IntegerField(blank=False,default=0)
    usb_3_2_head_gen2= models.IntegerField(blank=False,default=0)
    usb_3_2_head_gen2x2 = models.IntegerField(blank=False,default=0)
    support_ecc     = models.CharField(blank=False, max_length=150,default=None)
    wireless_net    = models.CharField(blank=False, max_length=150,default=None)
    raid_supp       = models.CharField(blank=False, max_length=150,default=None)
    vga_interface   = models.CharField(blank=False, max_length=150)
    thumb_pic       = models.ImageField(upload_to='mtb/',blank=True)
    str_interface   = models.CharField(blank=False, max_length=150)
    price           = models.IntegerField(blank=False,editable=True)

    def __str__(self):
        return (self.name)

    def get_absolute_url(self):
        return reverse("sim:mtb_detail",kwargs={'pk':self.pk})


class Cpu(models.Model):
    name            = models.CharField(blank=False, max_length=150)
    manufacturer    = models.CharField(blank=False, max_length=150,default=None)
    part            = models.CharField(blank=False, max_length=150,default=None)
    core_count      = models.IntegerField(blank=False)
    core_clock      = models.DecimalField(blank=False, decimal_places=1,max_digits=3)
    boost_clock     = models.DecimalField(blank=False, decimal_places=1,max_digits=3,default=None)
    tdp             = models.IntegerField(blank=False)
    series          = models.CharField(blank=False, max_length=150,default=None)
    mic_arc         = models.CharField(blank=False, max_length=150,default=None)
    core_fam        = models.CharField(blank=False, max_length=150,default=None)
    integ_graph     = models.CharField(blank=False, max_length=150,default=None)
    max_sup_mem     = models.IntegerField(blank=False,default=0)
    ecc_sup         = models.CharField(blank=False, max_length=150,default=None)
    package         = models.CharField(blank=False, max_length=150,default=None)
    inc_cool        = models.CharField(blank=False, max_length=150,default=None)
    l1_cache        = models.CharField(blank=False, max_length=150,default=None)
    l2_cache        = models.CharField(blank=False, max_length=150,default=None)
    l3_cache        = models.CharField(blank=False, max_length=150,default=None)
    litho           = models.CharField(blank=False, max_length=150,default=None)
    sim_multhread   = models.CharField(blank=False, max_length=150,default=None)
    price           = models.IntegerField(blank=False,default=0)
    socket          = models.CharField(blank=False, max_length=150,default=None)
    thumb_pic       = models.ImageField(upload_to='cpu/',blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sim:cpu_detail",kwargs={'pk':self.pk})

class Vga(models.Model):
    name            = models.CharField(blank=False, max_length=150)
    manufacturer    = models.CharField(blank=False, max_length=150,default=None)
    part            = models.CharField(blank=False, max_length=150,default=None)
    chipset         = models.CharField(blank=False, max_length=150)
    mem_cap         = models.IntegerField(blank=False)
    mem_type        = models.CharField(blank=False, max_length=150,default=None)
    core_clock      = models.IntegerField(blank=False,default=0)
    boost_clock     = models.IntegerField(blank=False,default=0)
    eff_mem_clock   = models.IntegerField(blank=False,default=0)
    vga_interface   = models.CharField(blank=False, max_length=150,default=None)
    color           = models.CharField(blank=False, max_length=150,default=None)
    sli             = models.CharField(blank=False, max_length=150,default=None)
    frame_sync      = models.CharField(blank=False, max_length=150,default=None)
    length          = models.DecimalField(blank=False, decimal_places=2,max_digits=6,default=None)
    tdp             = models.IntegerField(blank=False,default=0)
    dvi             = models.IntegerField(blank=False,default=0)
    hdmi_port       = models.IntegerField(blank=False,default=0)
    mini_hdmi       = models.IntegerField(blank=False,default=0)
    display_port    = models.IntegerField(blank=False,default=0)
    mini_disp_port  = models.IntegerField(blank=False,default=0)
    expan_slot      = models.IntegerField(blank=False,default=0)
    cool            = models.IntegerField(blank=False,default=0)
    ex_power        = models.CharField(blank=False, max_length=150,default=None)
    display         = models.IntegerField(blank=False,default=0)
    hdmi            = models.IntegerField(blank=False,default=0)
    price           = models.IntegerField(blank=False,editable=True)
    thumb_pic       = models.ImageField(upload_to='vga/',blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sim:vga_detail",kwargs={'pk':self.pk})

class Ram(models.Model):
    name = models.CharField(blank=False, max_length=150)
    manufacturer    = models.CharField(blank=False, max_length=150,default=None)
    part            = models.CharField(blank=False, max_length=150,default=None)
    form_factor     = models.CharField(blank=False, max_length=150,default=None)
    color           = models.CharField(blank=False, max_length=150,default=None)
    fw_latency      = models.IntegerField(blank=False,default=0)
    cas_latency     = models.IntegerField(blank=False,default=0)
    voltage         = models.DecimalField(blank=False, decimal_places=2,max_digits=6,default=None)
    timing          = models.CharField(blank=False, max_length=150,default=None)
    ecc_reg         = models.CharField(blank=False, max_length=150,default=None)
    heat_spread     = models.CharField(blank=False, max_length=150,default=None)
    mem_type        = models.CharField(blank=False, max_length=150,default=None)
    speed           = models.IntegerField(blank=False)
    module          = models.IntegerField(blank=False)
    price           = models.IntegerField(blank=False,editable=True)
    thumb_pic       = models.ImageField(upload_to='ram/',blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sim:ram_detail",kwargs={'pk':self.pk})

class Storage(models.Model):
    name            = models.CharField(blank=False, max_length=150)
    manufacturer    = models.CharField(blank=False, max_length=150,default=None)
    part            = models.CharField(blank=False, max_length=150,default=None)
    mem_cap         = models.IntegerField(blank=False)
    type            = models.IntegerField(blank=False)
    cache           = models.IntegerField(blank=False)
    form_factor     = models.CharField(blank=False, max_length=150,default=None)
    str_interface   = models.CharField(blank=False, max_length=150,default=None)
    nvme            = models.CharField(blank=False, max_length=150,default=None)
    price           = models.IntegerField(blank=False,editable=True)
    thumb_pic       = models.ImageField(upload_to='storage/',blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("sim:storage_detail",kwargs={'pk':self.pk})

class Simulation(models.Model):
    build_name = models.CharField(blank=False, max_length=150)
    mtb_name = models.ForeignKey(Motherboard, on_delete=models.CASCADE)
    cpu_name = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    vga_name = models.ForeignKey(Vga, on_delete=models.CASCADE)
    ram_name = models.ForeignKey(Ram, on_delete=models.CASCADE)
    str_name = models.ForeignKey(Storage, on_delete=models.CASCADE)

    def __str__(self):
        return self.build_name

    def get_absolute_url(self):
        return reverse('sim:sim_res')
