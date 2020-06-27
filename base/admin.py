from django.contrib import admin
from . models import Reducer, Weldolet, WeldingNeckFlangDIN, WeldingBend
from . models import WeldingNeckFlangASAASTM, TPiece, TReducer, Valve, InsertFlang
from . models import Flange2with35, Flange11, Flange13, Angle90, Angle180, TPieceDIN, TReducerPieceDIN, ReducerDIN, Caps
admin.site.register(TReducer)
admin.site.register(TPiece)
admin.site.register(Valve)
admin.site.register(InsertFlang)
admin.site.register(WeldingBend)
admin.site.register(WeldingNeckFlangASAASTM)
admin.site.register(Weldolet)
admin.site.register(WeldingNeckFlangDIN)
admin.site.register(Reducer)
admin.site.register(Flange2with35)
admin.site.register(Flange11)
admin.site.register(Flange13)
admin.site.register(Angle90)
admin.site.register(Angle180)
admin.site.register(TPieceDIN)
admin.site.register(TReducerPieceDIN)
admin.site.register(ReducerDIN)
admin.site.register(Caps)
# Register your models here.
