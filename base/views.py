from .models import Reducer, Weldolet, WeldingBend, WeldingNeckFlangDIN, \
    WeldingNeckFlangASAASTM, \
    TPiece, TReducer, Valve, InsertFlang, AllSpieces
from .models import Flange2with35, Flange11, Flange13, Angle90, Angle180, TPieceDIN, TReducerPieceDIN, ReducerDIN, Caps
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.db.models import F
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q
import json
from django.apps import apps
from django import template
from .parse import ParseWeldolet, ParseWeldingBend, ParseValve, ParseFlange212


def renderBaseHTML(request):
    return render(request, 'base.html')


register = template.Library()


@register.filter
def get_obj_attr(obj, attr):
    return getattr(obj, attr)


def index(request):
    # здесь обращаемся к бд и получаем нужные списки данных
    # чтобы потом их использовать в разметке
    all_spieces = AllSpieces.objects.all()
    t_pieces = TPiece.objects.all()
    t_reducers = TReducer.objects.all()
    insert_flangs = InsertFlang.objects.all()
    valves = Valve.objects.all()
    return render(request, 'field/autorisation.html', {'t_pieces': t_pieces, 't_reducers': t_reducers,
                                                       'insert_flangs': insert_flangs, 'valves': valves,
                                                       'all_spieces': all_spieces})


def baseHTML(request):
    # здесь обращаемся к бд и получаем нужные списки данных
    # чтобы потом их использовать в разметке
    print(request)
    all_spieces = AllSpieces.objects.all()
    t_pieces = TPiece.objects.all()
    t_reducers = TReducer.objects.all()
    insert_flangs = InsertFlang.objects.all()
    valves = Valve.objects.all()
    return render(request, 'field/base.html', {
        't_pieces': t_pieces, 't_reducers': t_reducers,
        'insert_flangs': insert_flangs, 'valves': valves,
        'all_spieces': all_spieces})

    # return HttpResponse('field/base.html')


def secureBase(request):
    print("here")
    password = request.GET.get("password", None)
    login = request.GET.get("login", None)
    if login == "123" and password == "123":
        return JsonResponse({'valid': True}, content_type="application/json")
        # baseHTML(request)
    else:
        return JsonResponse({'valid': False}, content_type="application/json")


def finder(name):
    if name == "WeldingBend" or name == "WeldingNeckFlangASAASTM" or name == "WeldingNeckFlangDIN" or name == "Valve" or name == "InsertFlang" or name == 'Flange13' or name == 'Flange11' or name == 'Flange2with35':
        return "group1"
    elif name == "TPiece" or name == "TReducer" or name == "Reducer" or name == 'TPieceDIN' or name == 'TReducerPieceDIN' or name == 'ReducerDIN' or name == 'Caps':
        return "group2"
    elif name == "Weldolet":
        return "group3"
    elif name == 'SPECIAL':
        return "group4"
    else:
        return "404"

        return string


def group1(name, var, diameter):
    var = ParseWeldingBend(var)
    var = ParseValve(var)
    var = ParseFlange212(var)
    print(var)
    Model = apps.get_model('field', name)
    model = Model.objects.get(pipe_diam=diameter)
    return getattr(model, var)


def group2(name, var, var2, diameter):
    if name == 'Caps' and diameter >= 700:
        parsed = var.split(' ')
        print(parsed)
        if parsed[1] == '>':
            return Caps.objects.get(pipe_diam=diameter).install_length
        elif parsed[1] == '<=':
            return Caps.objects.get(pipe_diam=diameter).install_length_T
    if name == "TPiece" or name == 'TPieceDIN' or (name == 'Caps' and diameter < 700):
        print('got here ')
        Model = apps.get_model('field', name)
        return Model.objects.get(pipe_diam=diameter).install_length
    if name == "TReducer" or name == 'TReducerPieceDIN':
        Model = apps.get_model('field', name)
        if var2 == "Big":
            print('sup')
            return Model.objects.get(Q(pipe_diam_big=diameter) & Q(pipe_diam_small=var)).install_length_big
        elif var2 == "Small":
            return Model.objects.get(Q(pipe_diam_big=var) & Q(pipe_diam_small=diameter)).install_length_small
        else:
            return ''
    if name == "Reducer":
        if var2 == 'Big':
            return Reducer.objects.get(Q(pipe_diam_big=diameter) & (Q(small_pipe_diam1=var) | Q(small_pipe_diam2=var) |
                                                                    Q(small_pipe_diam3=var) | Q(
                        small_pipe_diam4=var) | Q(small_pipe_diam5=var) | Q(small_pipe_diam6=var))) \
                .install_length_mm
        elif var2 == 'Small':
            return Reducer.objects.get(Q(pipe_diam_big=var) & (
                    Q(small_pipe_diam1=diameter) | Q(small_pipe_diam2=diameter) | Q(small_pipe_diam3=diameter) | Q(
                            small_pipe_diam4=diameter) | Q(small_pipe_diam5=diameter) | Q(
                            small_pipe_diam6=diameter))).install_length_mm
        else:
            return ''
    if name == 'ReducerDIN':
        if var2 == 'Big':
            return ReducerDIN.objects.get(Q(pipe_diam_big=diameter) & Q(pipe_diam_small=var)).install_length
        elif var2 == 'Small':
            return ReducerDIN.objects.get(Q(pipe_diam_big=var) & Q(pipe_diam_small=diameter)).install_length
        else:
            return ''


def group3(name, var, var2, diameter):
    var2 = ParseWeldolet(var2)
    return getattr(Weldolet.objects.get(Q(pipe_diam=diameter) & (Q(size=var))), var2)


def calculation(request):
    compAname = request.GET.get("compAname", None)
    compAvar1 = request.GET.get('compAprops', None)
    weld = request.GET.get("weld", None)
    compAvar2 = request.GET.get("compAvar", None)
    compBname = request.GET.get("compBname", None)
    compBvar1 = request.GET.get("compBprops", None)
    compBvar2 = request.GET.get("compBvar", None)
    print(compAname, compAvar1, compAvar2, compBname, compBvar1, compBvar2)
    if compAname == '' and compBname == '' or weld == '':
        return JsonResponse({'reason': 'no components have been chosen', "valid": False},
                            content_type="application/json")
    if weld == '':
        return JsonResponse({'reason': 'no weld values are given', "valid": False}, content_type="application/json")
    if weld != '':
        try:
            weld = float(weld)
        except ValueError:
            return JsonResponse({'reason': 'cannot read weld of component A as a number', "valid": False},
                                content_type="application/json")
    else:
        weld = 0
    try:
        dia = float(request.GET.get("diameter", None))
    except ValueError:
        return JsonResponse({'reson': 'cannot read diameter as a number', "valid": False},
                            content_type="application/json")
    try:
        length = float(request.GET.get("length", None))
    except ValueError:
        return JsonResponse({'reason': 'cannot read length as a number', "valid": False},
                            content_type="application/json")
    if compAname == 'SPECIAL':
        try:
            specialsizeA = float(request.GET.get('compAinput', None))
            print(specialsizeA)
        except ValueError:
            return JsonResponse({'reason': 'cannot convert component A\' s inbuilt size to float', "valid": False},
                                content_type="application/json")
    if compBname == 'SPECIAL':
        try:
            specialsizeB = float(request.GET.get('compBinput', None))
        except ValueError:
            return JsonResponse({'reason': 'cannot convert component B\' s inbuilt size to float', "valid": False},
                                content_type="application/json")
    inbs = 0
    inbs2 = 0
    decider = finder(compAname)
    if decider == 'group1':
        inbs = group1(compAname, compAvar1, dia)
    elif decider == 'group2':
        inbs = group2(compAname, compAvar1, compAvar2, dia)
    elif decider == 'group3':
        inbs = group3(compAname, compAvar1, compAvar2, dia)
    elif decider == 'group4':
        inbs = specialsizeA
    else:
        inbs = 0
    decider2 = finder(compBname)
    if decider2 == 'group1':
        inbs2 = group1(compBname, compBvar1, dia)
        print(inbs2, 'wtf1')
    elif decider2 == 'group2':
        inbs2 = group2(compBname, compBvar1, compBvar2, dia)
        print(inbs2, 'wtf2')
    elif decider2 == 'group3':
        inbs2 = group3(compBname, compBvar1, compBvar2, dia)
        print(inbs2, 'wtf3')
    elif decider2 == 'group4':
        inbs2 = specialsizeB
    else:
        inbs2 = 0
    resp = length - (inbs + weld) - (inbs2 + weld)
    if resp <= 0:
        return JsonResponse({'reason': 'expected length is less than 0, please check again', "valid": False},
                            content_type="application/json")
    return JsonResponse({"instance": resp, 'valid': True}, content_type="application/json")


# Search for additional variable given diameter and first parameter
def getadditionaldata(request):
    dia = float(request.GET.get("diameter", None))
    component_type = request.GET.get("type", None)
    parameter = request.GET.get("parameter", None)
    if component_type == 'Reducer':
        if str(parameter) == 'Big':
            data = Reducer.objects.all().filter(pipe_diam_big=dia).values('small_pipe_diam1'
                                                                          , 'small_pipe_diam2'
                                                                          , 'small_pipe_diam3'
                                                                          , 'small_pipe_diam4'
                                                                          , 'small_pipe_diam5'
                                                                          , 'small_pipe_diam6')
        else:
            data = Reducer.objects.all().filter(
                Q(small_pipe_diam1=dia) | Q(small_pipe_diam2=dia) | Q(small_pipe_diam3=dia) | Q(
                    small_pipe_diam4=dia) | Q(small_pipe_diam5=dia) | Q(small_pipe_diam6=dia)).values('pipe_diam_big')
    elif component_type == 'TReducer':
        if str(parameter) == 'Big':
            data = TReducer.objects.all().filter(pipe_diam_big=dia).values('pipe_diam_small')
        else:
            data = TReducer.objects.all().filter(pipe_diam_small=dia).values('pipe_diam_big')
    elif component_type == 'Weldolet':
        data = Weldolet.objects.all().filter(Q(pipe_diam=dia) & Q(size=str(parameter))).values('weldolet_diam1',
                                                                                               'weldolet_diam2'
                                                                                               , 'weldolet_diam3',
                                                                                               'weldolet_diam4',
                                                                                               'weldolet_diam5',
                                                                                               'weldolet_diam6',
                                                                                               'weldolet_diam7',
                                                                                               'weldolet_diam8',
                                                                                               'weldolet_diam9',
                                                                                               'weldolet_diam10',
                                                                                               'weldolet_diam11'
                                                                                               , 'weldolet_diam12',
                                                                                               'weldolet_diam13',
                                                                                               'weldolet_diam14',
                                                                                               'weldolet_diam15',
                                                                                               'weldolet_diam16',
                                                                                               'weldolet_diam17')
    elif component_type == 'ReducerDIN':
        if str(parameter) == 'Big':
            data = ReducerDIN.objects.all().filter(pipe_diam_big=dia).values('pipe_diam_small')
        else:
            data = ReducerDIN.objects.all().filter(pipe_diam_small=dia).values('pipe_diam_big')
    elif component_type == 'TReducerPieceDIN':
        if str(parameter) == 'Big':
            data = TReducerPieceDIN.objects.all().filter(pipe_diam_big=dia).values('pipe_diam_small')
        else:
            data = TReducerPieceDIN.objects.all().filter(pipe_diam_small=dia).values('pipe_diam_big')
    else:
        data = False
    if data:
        jsondata = json.dumps(list(data), cls=DjangoJSONEncoder)
        return JsonResponse(
            {"valid": True, "data": jsondata},
            content_type="application/json")
    else:
        return JsonResponse({"valid": False}, content_type="application/json")


# Search for components' objects with suitable diamater
def checkdia(request):
    print("here")
    dia = float(request.GET.get("diameter", None))
    flag = request.GET.get("flag", None)
    if flag == "true":
        # Noemwijdte
        temp1 = WeldingNeckFlangDIN.objects.all().filter(pipe_diam=dia).values('DIN2632ND10h',
                                                                               'DIN2633ND16h', 'DIN2634ND25h',
                                                                               'DIN2635ND40h', 'DIN2636ND64h',
                                                                               'DIN2637ND100h')
        temp2 = Flange2with35.objects.all().filter(pipe_diam=dia).values('PN212',
                                                                         'PN6', 'PN10',
                                                                         'PN16', 'PN25',
                                                                         'PN40')
        temp3 = Flange11.objects.all().filter(pipe_diam=dia).values('PN212',
                                                                    'PN6', 'PN10',
                                                                    'PN16', 'PN25',
                                                                    'PN40', 'PN63',
                                                                    'PN100', 'PN160',
                                                                    'PN250', 'PN320',
                                                                    'PN400')
        temp4 = Flange13.objects.all().filter(pipe_diam=dia).values('PN212',
                                                                    'PN6', 'PN10',
                                                                    'PN16', 'PN25',
                                                                    'PN40', 'PN63',
                                                                    'PN100')
        temp5 = Angle90.objects.all().filter(pipe_diam=dia)
        temp6 = Angle180.objects.all().filter(pipe_diam=dia)
        temp7 = TPieceDIN.objects.all().filter(pipe_diam=dia)
        if temp5:
            temp5 = True
        else:
            temp5 = False
        if temp6:
            temp6 = True
        else:
            temp6 = False
        if temp7:
            temp7 = True
        else:
            temp7 = False
        temp8 = TReducerPieceDIN.objects.all().filter(Q(pipe_diam_big=dia) | Q(pipe_diam_small=dia))
        temp9 = ReducerDIN.objects.all().filter(Q(pipe_diam_big=dia) | Q(pipe_diam_small=dia))
        if temp8:
            temp8 = True
        else:
            temp8 = False
        if temp9:
            temp9 = True
        else:
            temp9 = False
        temp10 = Caps.objects.all().filter(pipe_diam=dia).values('pipe_diam', 'TValueinterval')
        all_spieces = {'name1': 'Angle90', 'name2': 'Angle180', 'name3': 'TPieceDIN', 'name4': 'ReducerDIN',
                       'name5': 'TReducerPieceDIN',
                       'name6': 'WeldingNeckFlangDIN', 'name7': 'Flange13', 'name8': 'Flange11',
                       'name9': 'Flange2with35', 'name10': 'Caps'}
        if temp1 or temp2 or temp3 or temp4 or temp5 or temp6 or temp7 or temp8 or temp9 or temp10:
            jsonlist1 = json.dumps(temp5)
            jsonlist2 = json.dumps(temp6)
            jsonlist3 = json.dumps(temp7)
            jsonlist4 = json.dumps(temp9)
            jsonlist5 = json.dumps(temp8)
            jsonlist6 = json.dumps(list(temp1))
            jsonlist7 = json.dumps(list(temp4), cls=DjangoJSONEncoder)
            jsonlist8 = json.dumps(list(temp3), cls=DjangoJSONEncoder)
            jsonlist9 = json.dumps(list(temp2), cls=DjangoJSONEncoder)
            jsonlist10 = json.dumps(list(temp10), cls=DjangoJSONEncoder)
            all_spieces = json.dumps(all_spieces)
            return JsonResponse(
                {"valid": True, "data1": jsonlist1, "data2": jsonlist2, "data3": jsonlist3, "data4": jsonlist4,
                 "data5": jsonlist5, "data6": jsonlist6,
                 "data7": jsonlist7, "data8": jsonlist8, "data9": jsonlist9, "data10": jsonlist10,
                 'names': all_spieces},
                content_type="application/json")
        else:
            return JsonResponse({"valid": False}, content_type="application/json")
    else:
        temp1 = WeldingBend.objects.all().filter(pipe_diam=dia).annotate(LR90R=F('L_R_90_R'), LR45B=F('L_R_45_B'),
                                                                         LR180=F('L_R_180'), SR180=F('S_R_180'),
                                                                         SR90A=F('S_R_90_A')).values('LR90R', 'LR45B',
                                                                                                     'LR180', 'SR180',
                                                                                                     'SR90A')
        temp2 = WeldingNeckFlangASAASTM.objects.all().filter(pipe_diam=dia).values('lbs150RF1_16_H', 'lbs300RF1_16_H',
                                                                                   'lbs400RF1_4_H',
                                                                                   'lbs600RF1_4_H', 'lbs900RF1_4_H',
                                                                                   'lbs1500RF1_4_H', 'lbs2500RF1_4_H')
        temp3 = TPiece.objects.all().filter(pipe_diam=dia).annotate(InstallationLength=F('install_length')).values(
            'InstallationLength')
        temp4 = TReducer.objects.filter(Q(pipe_diam_big=dia) | Q(pipe_diam_small=dia))
        if temp4:
            temp4 = True
        else:
            temp4 = False
        temp5 = Reducer.objects.all().filter(
            Q(pipe_diam_big=dia) | Q(small_pipe_diam1=dia) | Q(small_pipe_diam2=dia) | Q(small_pipe_diam3=dia) | Q(
                small_pipe_diam4=dia) | Q(small_pipe_diam5=dia) | Q(small_pipe_diam6=dia))
        if temp5:
            temp5 = True
        else:
            temp5 = False
        temp6 = Weldolet.objects.all().filter(pipe_diam=dia).values('size')
        temp7 = Valve.objects.all().filter(pipe_diam=dia).annotate(GateValve150ibs=F('valve_150ibs'),
                                                                   GateValve300ibs=F('valve_300ibs'),
                                                                   BallValve150ibs=F('ball_150ibs'),
                                                                   BallValve300ibs=F('ball_300ibs'),
                                                                   CheckValve150ibs=F('check_150ibs'),
                                                                   CheckValve300ibs=F('check_300ibs')).values(
            'GateValve150ibs', 'GateValve300ibs',
            'BallValve150ibs', 'BallValve300ibs', 'CheckValve150ibs', 'CheckValve300ibs')
        temp8 = InsertFlang.objects.all().filter(pipe_diam=dia).values('ibs150', 'ibs300', 'ibs600', 'ibs900',
                                                                       'ibs1500')
        if temp1 or temp2 or temp3 or temp4 or temp5 or temp6 or temp7 or temp8:
            jsonlist1 = json.dumps(list(temp3), cls=DjangoJSONEncoder)
            jsonlist2 = json.dumps(list(temp6), cls=DjangoJSONEncoder)
            jsonlist3 = json.dumps(list(temp2), cls=DjangoJSONEncoder)
            jsonlist4 = json.dumps(list(temp1), cls=DjangoJSONEncoder)
            jsonlist5 = json.dumps(list(temp7), cls=DjangoJSONEncoder)
            jsonlist6 = json.dumps(list(temp8), cls=DjangoJSONEncoder)
            jsonlist7 = json.dumps(temp4)
            jsonlist8 = json.dumps(temp5)
            all_spieces = {'name3': 'TPiece', 'name4': 'Weldolet',
                           'name5': 'WeldingNeckFlangASAASTM', 'name6': 'WeldingBend', 'name7': 'Valve',
                           'name8': 'InsertFlang', 'name9': 'TReducer', 'name10': 'Reducer', 'name11': 'SPECIAL'}
            all_spieces = json.dumps(all_spieces)
            return JsonResponse(
                {"valid": True, "data3": jsonlist1, "data4": jsonlist2, "data5": jsonlist3,
                 "data8": jsonlist4, "data9": jsonlist5, "data10": jsonlist6, "data11": jsonlist7, "data12": jsonlist8,
                 "names": all_spieces},
                content_type="application/json")
        else:
            return JsonResponse({"valid": False}, content_type="application/json")
