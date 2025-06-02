from django.contrib import admin
from .models import Net, Fabric, Rolet, Worker, WorkerImage, WindowType, WindowColour

# Register your models here.

admin.site.register(Net)

admin.site.register(Fabric)

admin.site.register(Rolet)

admin.site.register(Worker)

admin.site.register(WorkerImage)

admin.site.register(WindowType)

admin.site.register(WindowColour)
