import csv,sys,os
import os

import django

from base.models import Reducer, Weldolet,TPiece, TReducer, Valve, InsertFlang, AllSpieces, WeldingBend
from base.models import Flange2with35, Flange11, Flange13, Angle90, Angle180, TPieceDIN, TReducerPieceDIN, ReducerDIN
from base.models import WeldingNeckFlangASAASTM, WeldingNeckFlangDIN, Caps
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path += '/studentPro'
project_dir = dir_path
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
django.setup()
Flange2with35.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/Flange2with35.csv"), delimiter=";")
for row in data:
	if row[0] != 'п»їDN':
		flange = Flange2with35()
		flange.pipe_diam = row[0]
		if row[1] !='':
			flange.PN212 = row[1]
		else:
			flange.PN212 = None
		if row[2] !='':
			flange.PN6 = row[2]
		else:
			flange.PN6 = None
		if row[3] !='':
			flange.PN10 = row[3]
		else:
			flange.PN10 = None
		if row[4] !='':
			flange.PN16 = row[4]
		else:
			flange.PN16 = None
		if row[5] !='':
			flange.PN25 = row[5]
		else:
			flange.PN25 = None
		if row[6] !='':
			flange.PN40 = row[6]
		else:
			flange.PN40 = None
		flange.save()

Flange11.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/Flange11.csv"), delimiter=";")
for row in data:
	if row[0] != 'DN' and row[0] != 'п»їDN':
		flange = Flange11()
		flange.pipe_diam = row[0]
		if row[1] !='':
			flange.PN212 =  row[1]
		else:
			flange.PN212 = None
		if row[2] !='':
			flange.PN6 = row[2]
		else:
			flange.PN6 = None
		if row[3] !='':
			flange.PN10 = row[3]
		else:
			flange.PN10 = None
		if row[4] !='':
			flange.PN16 = row[4]
		else:
			flange.PN16 = None
		if row[5] !='':
			flange.PN25 = row[5]
		else:
			flange.PN25 = None
		if row[6] !='':
			flange.PN40 = row[6]
		else:
			flange.PN40 = None
		if row[7] !='':
			flange.PN63 = row[7]
		else:
			flange.PN63 = None
		if row[7] !='':
			flange.PN100 = row[7]
		else:
			flange.PN100 = None
		if row[8] !='':
			flange.PN160 = row[8]
		else:
			flange.PN160 = None
		if row[9] !='':
			flange.PN250 = row[9]
		else:
			flange.PN250 = None
		if row[10] !='':
			flange.PN320 = row[10]
		else:
			flange.PN320 = None
		if row[11] !='':
			flange.PN400 = row[11]
		else:
			flange.PN400 = None
		flange.save()

Flange13.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/Flange13.csv"), delimiter=";")
for row in data:
	if row[0] != 'п»їDN':
		flange = Flange13()
		flange.pipe_diam = row[0]
		if row[1] !='':
			flange.PN212 =  row[1]
		else:
			flange.PN212 = None
		if row[2] !='':
			flange.PN6 = row[2]
		else:
			flange.PN6 = None
		if row[3] !='':
			flange.PN10 = row[3]
		else:
			flange.PN10 = None
		if row[4] !='':
			flange.PN16 = row[4]
		else:
			flange.PN16 = None
		if row[5] !='':
			flange.PN25 = row[5]
		else:
			flange.PN25 = None
		if row[6] !='':
			flange.PN40 = row[6]
		else:
			flange.PN40 = None
		if row[7] !='':
			flange.PN63 = row[7]
		else:
			flange.PN63 = None
		if row[7] !='':
			flange.PN100 = row[7]
		else:
			flange.PN100 = None
		flange.save()

Angle90.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/Angle90.csv"), delimiter=";")
for row in data:
	if row[0]!='п»їxuy':
		angle = Angle90()
		angle.pipe_diam = row[0]
		angle.install_length = row[1]
		angle.save()

Angle180.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/Angle180.csv"), delimiter=";")
for row in data:
	if row[0]!='п»їDN':
		angle = Angle180()
		angle.pipe_diam = row[0]
		angle.install_length = row[1]
		angle.save()

TReducerPieceDIN.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/TPieceReducerDIN.csv"), delimiter=";")
for row in data:
	if row[0]!='п»їDN Big':
		piece = TReducerPieceDIN()
		piece.pipe_diam_big = row[0]
		piece.pipe_diam_small = row[1]
		piece.install_length_big = row[2]
		piece.install_length_small = row[3]
		piece.save()

TPieceDIN.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/TPiece.DIN.csv"), delimiter=";")
for row in data:
	if row[0]!='п»їDN ':
		piece = TPieceDIN()
		piece.pipe_diam = row[0]
		piece.install_length = row[1]
		piece.save()

ReducerDIN.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/Reducer.DIN.csv"), delimiter=";")
for row in data:
	if row[0]!='п»їDN Big':
		reducer = ReducerDIN()
		reducer.pipe_diam_big = row[0]
		reducer.pipe_diam_small = row[1]
		reducer.install_length = row[2]
		reducer.save()

Caps.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/Caps.csv"), delimiter=";")
for row in data:
	if row[0]!='п»їDN':
		cap = Caps()
		cap.pipe_diam = row[0]
		cap.install_length = row[1]
		if row[2] != '':
			cap.TValueinterval = row[2]
		else:
			cap.TValueinterval = None
		if row[3] != '':
			cap.install_length_T = row[3]
		else:
			cap.install_length_T = None
		cap.save()

Reducer.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/reducers.ready.csv"), delimiter=";")
for row in data:
	if row[0]!= "Biggest pipediameter" and row[0]!= "п»їBiggest pipediameter":
		print(row[0], row[7], row[8])
		reducer = Reducer()
		print('im here')
		reducer.pipe_diam_big = row[0]
		reducer.install_length_inch = row[7]
		reducer.install_length_mm = row[8]
		reducer.small_pipe_diam1 = row[1]
		reducer.small_pipe_diam2 = row[2]
		if row[3] !='':
			reducer.small_pipe_diam3 =  row[3]
		else:
			reducer.small_pipe_diam3 = None
		if row[4] !='':
			reducer.small_pipe_diam4 =  row[4]
		else:
			reducer.small_pipe_diam4 = None
		if row[5] !='':
			reducer.small_pipe_diam5 =  row[5]
		else:
			reducer.small_pipe_diam5 = None
		if row[6] !='':
			reducer.small_pipe_diam6 =  row[6]
		else:
			reducer.small_pipe_diam6 = None
		reducer.save()
TPiece.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/tpieces_ready.csv"), delimiter = ";")
for row in data:
	if row[0] != 'п»їPipediameter in inches':
		tpiece = TPiece()
		tpiece.pipe_diam = row[0]
		tpiece.install_length = row[1]
		tpiece.save()
TReducer.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/treducerpieces.ready.csv"), delimiter=";")
for row in data:
	if row[0] != 'п»їprobably unnecessary':
		treducerpiece = TReducer()
		treducerpiece.pipe_diam_big= row[1]
		treducerpiece.pipe_diam_small = row[2]
		treducerpiece.install_length_big = row[3]
		treducerpiece.install_length_small = row[4]
		treducerpiece.save()
Valve.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/valves.ready.csv"), delimiter=";")
for row in data:
	if row[0]!= 'п»їPipediameter in inches':
		valve = Valve()
		valve.pipe_diam = row[0]
		if row[1] == '':
			valve.valve_150ibs = None
		else:
			valve.valve_150ibs = row[1]
		if row[2] == '':
			valve.valve_300ibs = None
		else:
			valve.valve_300ibs = row[2]
		if row[3] == '':
			valve.ball_150ibs = None
		else:
			valve.ball_150ibs = row[3]
		if row[4] == '':
			valve.ball_300ibs = None
		else:
			valve.ball_300ibs = row[4]
		if row[5] == '':
			valve.check_150ibs = None
		else:
			valve.check_150ibs =row[5]
		if row[6] == '':
			valve.check_300ibs = None
		else:
			valve.check_300ibs =row[6]
		valve.save()
#carbonsteel_pipes
CarbonSteelPipe.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/carbonsteel_pipes.ready.csv"), delimiter=";")
for row in data:
	if row[0] != 'п»їPipe diameter in inches':
		carbon_steel_pipe = CarbonSteelPipe()
		carbon_steel_pipe.pipe_diam =  row[0]
		carbon_steel_pipe.pipe_wallthick = row[1]
		carbon_steel_pipe.save()


# insertflanges
InsertFlang.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/insertflanges.ready.csv"), delimiter=";")
for row in data:
	if row[0] != 'п»їPipediameter in inches':
		insert_flang = InsertFlang()
		insert_flang.pipe_diam = row[0]
		if row[1] == '':
			insert_flang.ibs150 = None
		else:
			insert_flang.ibs150 = row[1]
		if row[2] == '':
			insert_flang.ibs300 = None
		else:
			insert_flang.ibs300 = row[2]
		if row[3] == '':
			insert_flang.ibs900 = None
		else:
			insert_flang.ibs600 = row[3]
		if row[4] == '':
			insert_flang.ibs900= None
		else:
			insert_flang.ibs900 = row[4]
		if row[5] == '':
			insert_flang.ibs1500= None
		else:
			insert_flang.ibs1500 = row[5]
		insert_flang.save()


SeamlessPipe.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/seamless_pipes.mistake.csv"), delimiter = ";")
for row in data:
	if row[0] != 'п»їPipediameter in mm ':
		seamlesspipe = SeamlessPipe()
		seamlesspipe.pipe_diam = row[0].replace(',', '.')
		seamlesspipe.pipe_wallthick = row[1].replace(',', '.')
		seamlesspipe.save()
WeldingBend.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/weldingbends.notready.csv"), delimiter = ";")
for row in data:
	if row[0] != 'п»їPipediameter in inches':
		weldbend = WeldingBend()
		weldbend.pipe_diam = row[0].replace(',', '.')
		weldbend.L_R_45_B = row[1].replace(',', '.')
		weldbend.L_R_90_R = row[2].replace(',', '.')
		weldbend.L_R_180 = None
		weldbend.S_R_180 = None
		weldbend.S_R_90_A = None
		if row[3] != '':
			weldbend.L_R_180 = row[3].replace(',', '.')
		if row[4] != '':
			weldbend.S_R_180 = row[4].replace(',', '.')
		if row[5] != '':
			weldbend.S_R_90_A = row[5].replace(',', '.')
		weldbend.save()
WeldingNeckFlangASAASTM.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/weldingneckflangesASAASTM.maybeready.csv"), delimiter = ";")
for row in data:
	if row[0] != 'п»їPipediameter in inches':
		weldneck = WeldingNeckFlangASAASTM()
		weldneck.pipe_diam = row[0].replace(',', '.')
		weldneck.lbs150RF1_16_H = row[1].replace(',', '.')
		weldneck.lbs300RF1_16_H = row[2].replace(',', '.')
		weldneck.lbs400RF1_4_H = row[3].replace(',', '.')
		weldneck.lbs600RF1_4_H = row[4].replace(',', '.')
		weldneck.lbs900RF1_4_H = None
		weldneck.lbs1500RF1_4_H = None
		weldneck.lbs2500RF1_4_H = None
		if row[5] != '':
			weldneck.lbs900RF1_4_H = row[5].replace(',', '.')
		if row[6] != '':
			weldneck.lbs1500RF1_4_H = row[6].replace(',', '.')
		if row[7] != '':
			weldneck.lbs2500RF1_4_H = row[7].replace(',', '.')
		weldneck.save()
Weldolet.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/weldolet.csv"), delimiter=";")
for row in data:
	if row[0]!='mainpipe in inches' and row[0] != 'п»ї' and row[0]!='' and row[0]!= 'п»їmainpipe in inches':
		weldolet = Weldolet()
		weldolet.pipe_diam = row[0]
		weldolet.size = row[1].encode('utf-8').decode('utf-8')
		if row[2] !='---' and row[2]!='':
			weldolet.weldolet_diam1 = row[2]
		else:
			weldolet.weldolet_diam1 = None
		weldolet.weldolet_diam2 = row[3]
		if  row[4]!='':
			weldolet.weldolet_diam3 = row[4]
		else:
			weldolet.weldolet_diam3 = None
		if  row[5]!='':
			weldolet.weldolet_diam4 = row[5]
		else:
			weldolet.weldolet_diam4 = None
		if row[6]!='':
			weldolet.weldolet_diam5 = row[6]
		else:
			weldolet.weldolet_diam5 = None
		if row[7]!='':
			weldolet.weldolet_diam6 = row[7]
		else:
			weldolet.weldolet_diam6 = None
		if row[8]!='':
			weldolet.weldolet_diam7 = row[8]
		else:
			weldolet.weldolet_diam7 = None
		if row[9]!='':
			weldolet.weldolet_diam8 = row[9]
		else:
			weldolet.weldolet_diam8 = None
		if row[10]!='':
			weldolet.weldolet_diam9 = row[10]
		else:
			weldolet.weldolet_diam9 = None
		if row[11]!='':
			weldolet.weldolet_diam10 = row[11]
		else:
			weldolet.weldolet_diam10 = None
		if row[12]!='':
			weldolet.weldolet_diam11 = row[12]
		else:
			weldolet.weldolet_diam11 = None
		if row[13]!='':
			weldolet.weldolet_diam12 = row[13]
		else:
			weldolet.weldolet_diam12 = None
		if row[14]!='':
			weldolet.weldolet_diam13 = row[14]
		else:
			weldolet.weldolet_diam13 = None
		if row[15]!='':
			weldolet.weldolet_diam14 = row[15]
		else:
			weldolet.weldolet_diam14 = None
		if row[16]!='':
			weldolet.weldolet_diam15 = row[16]
		else:
			weldolet.weldolet_diam15 = None
		if row[17]!='':
			weldolet.weldolet_diam16 = row[17]
		else:
			weldolet.weldolet_diam16 = None
		if row[18]!='':
			weldolet.weldolet_diam17 = row[18]
		else:
			weldolet.weldolet_diam17 = None
		weldolet.save()
WeldingNeckFlangDIN.objects.all().delete()
data = csv.reader(open("field/static/excel_sheets/weldingneckflangesDIM.csv"), delimiter=";")
for row in data:
	if row[0]!= "Noemwijdte" and row[0]!= "п»їNoemwijdte":
		weldingneck = WeldingNeckFlangDIN()
		weldingneck.pipe_diam = row[0]
		if row[1]!='':
			weldingneck.DIN2632ND10h = row[1]
		else:
			weldingneck.DIN2632ND10h = None
		if row[2]!='':
			weldingneck.DIN2633ND16h = row[2]
		else:
			weldingneck.DIN2633ND16h = None
		if row[3] != '':
			weldingneck.DIN2634ND25h = row[3]
		else:
			weldingneck.DIN2634ND25h = None
		if row[4]!='':
			weldingneck.DIN2635ND40h = row[4]
		else:
			weldingneck.DIN2635ND40h = None
		if row[5]!= '':
			weldingneck.DIN2636ND64h = row[5]
		else:
			weldingneck.DIN2636ND64h = None
		if row[6]!= '':
			weldingneck.DIN2637ND100h = row[6]
		else:
			weldingneck.DIN2637ND100h = None
		weldingneck.length = row[7]
		weldingneck.save()

AllSpieces.objects.all().delete()
AllSpieces(name='Carbon steel pipes').save()
AllSpieces(name='Insert flangs').save()
AllSpieces(name='Seamless pipes').save()
AllSpieces(name='T pieces').save()
AllSpieces(name='T reducers').save()
AllSpieces(name='Valves').save()
AllSpieces(name = 'Reducers').save()
AllSpieces(name = 'SPECIAL').save()
