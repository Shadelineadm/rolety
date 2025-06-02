from django.shortcuts import render, redirect
from .models import Rolet, Fabric, Net, Worker, WindowType, WindowColour
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from itertools import chain
# Create your views here.


def home_view(request):
    context = {
        'request': request,
    }
    return render(request, "main/home.html", context=context)


def catalog_view(request):
    context = {'request': request,
               }
    if request.GET == {}:
        nets = Net.objects.all()
        rolets = Rolet.objects.all()
        context['nets'] = 'nets'
        context['rolets'] = 'rolets'
        context['search_text'] = ''
        all_objects = rolets.union(nets)
    else:
        if request.GET.get('search_text'):
            context['search_text'] = request.GET.get('search_text')
        else:
            context['search_text'] = ''
        if request.GET.get('nets') == 'nets':
            context['nets'] = 'nets'
            nets = Net.objects.all()
            if request.GET.get('search_text'):
                nets = nets.filter(name__icontains=request.GET.get('search_text'))
            if request.GET.get('rolets') == 'rolets':
                context['rolets'] = 'rolets'
                rolets = Rolet.objects.all()
                if request.GET.get('search_text'):
                    rolets = rolets.filter(name__icontains=request.GET.get('search_text'))
                all_objects = rolets.union(nets)
            else:
                context['rolets'] = ''
                all_objects = nets
        else:
            context['nets'] = ''
            if request.GET.get('rolets') == 'rolets':
                context['rolets'] = 'rolets'
                rolets = Rolet.objects.all()
                if request.GET.get('search_text'):
                    rolets = rolets.filter(name__icontains=request.GET.get('search_text'))
                all_objects = rolets
            else:
                context['rolets'] = ''

    all_objects = all_objects.order_by('id')
    paginator = Paginator(all_objects, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj

    return render(request, "main/catalog.html", context=context)


def calculator_view(request):
    context = {'request': request,
               }
    if request.GET == {}:
        nets = Net.objects.all()
        rolets = Rolet.objects.all()
        context['nets'] = 'nets'
        context['rolets'] = 'rolets'
        context['search_text'] = ''
        all_objects = rolets.union(nets)
    else:
        if request.GET.get('search_text'):
            context['search_text'] = request.GET.get('search_text')
        else:
            context['search_text'] = ''
        if request.GET.get('nets') == 'nets':
            context['nets'] = 'nets'
            nets = Net.objects.all()
            if request.GET.get('search_text'):
                nets = nets.filter(name__icontains=request.GET.get('search_text'))
            if request.GET.get('rolets') == 'rolets':
                context['rolets'] = 'rolets'
                rolets = Rolet.objects.all()
                if request.GET.get('search_text'):
                    rolets = rolets.filter(name__icontains=request.GET.get('search_text'))
                all_objects = rolets.union(nets)
            else:
                context['rolets'] = ''
                all_objects = nets
        else:
            context['nets'] = ''
            if request.GET.get('rolets') == 'rolets':
                context['rolets'] = 'rolets'
                rolets = Rolet.objects.all()
                if request.GET.get('search_text'):
                    rolets = rolets.filter(name__icontains=request.GET.get('search_text'))
                all_objects = rolets
            else:
                context['rolets'] = ''

    all_objects = all_objects.order_by('id')
    paginator = Paginator(all_objects, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj

    return render(request, "main/calculator.html", context=context)


def price_view(request, type, pk, fab):
    context = {
        'request': request,
        'colours': WindowColour.objects.all(),
        'types': WindowType.objects.all(),
    }
    price = 0
    if request.method == 'POST':
        w_type = int(request.POST.get('w_type'))
        w_colour = int(request.POST.get('w_colour'))
        h = int(request.POST.get('height'))
        w = int(request.POST.get('width'))
        w_type = WindowType.objects.get(id=w_type)
        w_colour = WindowColour.objects.get(id=w_colour)
        area = h*w/100
        price += w_type.price
        price += w_colour.price
        if type == 'rolet':
            rol = Rolet.objects.get(id=pk)
            fabric = Fabric.objects.get(id=fab)
            price += rol.price
            price += fabric.price_m*area
        elif type == 'net':
            net = Net.objects.get(id=pk)
            price += net.price
            price += net.price_m * area
    context['price']=price
    return render(request, "main/price.html", context=context)


def workers_view(request):
    context = {
        'request': request,
        'workers': Worker.objects.all(),
    }
    return render(request, "main/workers.html", context=context)


def net_view(request, pk):
    context = {
        'request': request,
        'net': Net.objects.get(id=pk),
    }
    return render(request, "main/net.html", context=context)


def rolet_view(request, pk):
    context = {
        'request': request,
        'rolet': Rolet.objects.get(id=pk),
    }
    return render(request, "main/rolet.html", context=context)


def net_price(request, pk):
    return redirect('price', type='net', pk=pk, fab='0')


def rolet_price(request, pk):
    context = {
        'request': request,
        'rolet': Rolet.objects.get(id=pk),
    }
    return render(request, "main/rolet_price.html", context=context)


def fabric_view(request, pk):
    context = {
        'request': request,
        'fabric': Fabric.objects.get(id=pk),
    }
    return render(request, "main/fabric.html", context=context)
