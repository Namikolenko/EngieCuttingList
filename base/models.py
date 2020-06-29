from django.db import models
import csv, sys, os
import django


class WeldingBend(models.Model):
	pipe_diam = models.FloatField('pipe diameter')
	L_R_90_R = models.FloatField('L.R. 90° R')
	L_R_45_B = models.FloatField('L.R. 45° B', null=True)
	L_R_180 = models.FloatField('L.R. 180°', null=True)
	S_R_180= models.FloatField('L.R. 180°', null=True)
	S_R_90_A = models.FloatField('S.R. 90° A', null=True)


class WeldingNeckFlangASAASTM(models.Model):
	pipe_diam = models.FloatField('pipe diameter')
	lbs150RF1_16_H = models.FloatField('150 lbs. 1/16 RF. H')
	lbs300RF1_16_H = models.FloatField('300 lbs. 1/16 RF. H')
	lbs400RF1_4_H = models.FloatField('400 lbs. 1/4 RF. H')
	lbs600RF1_4_H = models.FloatField('600 lbs. 1/4 RF. H')
	lbs900RF1_4_H= models.FloatField('900 lbs. 1/4 RF. H', null = True)
	lbs1500RF1_4_H = models.FloatField('1500 lbs. 1/4 RF. H', null = True)
	lbs2500RF1_4_H= models.FloatField('2500 lbs. 1/4 RF. H', null = True)


class WeldingNeckFlangDIN(models.Model): # not imported: exel file not covered to inch
	pipe_diam = models.FloatField('pipe diameter')
	DIN2632ND10h = models.FloatField('DIN 2632 ND 10 h', null = True)
	DIN2633ND16h = models.FloatField('DIN 2633 ND 16 h', null = True)
	DIN2634ND25h = models.FloatField('DIN 2634 ND 25 h', null = True)
	DIN2635ND40h = models.FloatField('DIN 2635 ND 40 h', null = True)
	DIN2636ND64h = models.FloatField('DIN 2636 ND 64 h', null = True)
	DIN2637ND100h = models.FloatField('DIN 2637 ND 100 h', null = True)
	length = models.FloatField('Length in mm')


class TPiece(models.Model):
	pipe_diam = models.FloatField('pipe diameter')
	install_length = models.FloatField('installation length')

	def __str__(self):
		return 'TPiece'


class TReducer(models.Model):
	pipe_diam_big = models.FloatField(' big pipe diameter')
	pipe_diam_small = models.FloatField('small pipe diameter')
	install_length_big = models.FloatField('M1 in mm')
	install_length_small = models.FloatField('M2 in mm')

	def __str__(self):
		return 'TReducer'


class Reducer(models.Model):
	pipe_diam_big = models.FloatField('diameter of big pipe')
	install_length_inch = models.FloatField('Installation length in inches')
	install_length_mm = models.FloatField('Installation length in mm')
	small_pipe_diam1 = models.FloatField('first small diameter')
	small_pipe_diam2 = models.FloatField('second small diameter')
	small_pipe_diam3 = models.FloatField('third small diameter', null = True)
	small_pipe_diam4 = models.FloatField('fourth small diameter', null = True)
	small_pipe_diam5 = models.FloatField('fifth small diameter', null = True)
	small_pipe_diam6 = models.FloatField('sixth small diameter', null = True)


class Weldolet(models.Model):
	pipe_diam = models.FloatField('pipe diameter')
	size = models.CharField('Size', max_length = 20)
	weldolet_diam1 = models.FloatField('weldolet diameter is 3/8',null = True)
	weldolet_diam2 = models.FloatField('weldolet diameter is 1/2')
	weldolet_diam3 = models.FloatField('weldolet diameter is 3/4',null = True)
	weldolet_diam4 = models.FloatField('weldolet diameter is 1',null = True)
	weldolet_diam5 = models.FloatField('weldolet diameter is 1.5',null = True)
	weldolet_diam6 = models.FloatField('weldolet diameter is 2',null = True)
	weldolet_diam7 = models.FloatField('weldolet diameter is 3',null = True)
	weldolet_diam8 = models.FloatField('weldolet diameter is 4',null = True)
	weldolet_diam9 = models.FloatField('weldolet diameter is 6',null = True)
	weldolet_diam10 = models.FloatField('weldolet diameter is 8',null = True)
	weldolet_diam11 = models.FloatField('weldolet diameter is 10',null = True)
	weldolet_diam12 = models.FloatField('weldolet diameter is 12',null = True)
	weldolet_diam13 = models.FloatField('weldolet diameter is 14',null = True)
	weldolet_diam14 = models.FloatField('weldolet diameter is 16',null = True)
	weldolet_diam15 = models.FloatField('weldolet diameter is 18',null = True)
	weldolet_diam16 = models.FloatField('weldolet diameter is 20',null = True)
	weldolet_diam17 = models.FloatField('weldolet diameter is 24',null = True)

class Valve(models.Model):
	pipe_diam = models.FloatField('pipe diameter')
	valve_150ibs = models.FloatField('Gate valve 150 ibs')
	valve_300ibs = models.FloatField('Gate valve 300 ibs', null = True)
	ball_150ibs = models.FloatField('Ball valve 150 ibs', null = True)
	ball_300ibs = models.FloatField('Ball valve 300 ibs', null = True)
	check_150ibs = models.FloatField('Check valve 150 ibs', null = True)
	check_300ibs = models.FloatField('Check valve 300 ibs', null = True)

	def __str__(self):
		return 'Valve'


class InsertFlang(models.Model):
	pipe_diam = models.FloatField('pipe diameter')
	ibs150 =  models.FloatField('150 ibs', null = True)
	ibs300 =  models.FloatField('300 ibs', null = True)
	ibs600 =  models.FloatField('600 ibs', null = True)
	ibs900=  models.FloatField('900 ibs', null = True)
	ibs1500 =  models.FloatField('1500 ibs', null = True)

	def __str__(self):
		return 'InsertFlang'


class Flange2with35(models.Model):
	pipe_diam = models.FloatField('pipe_diam')
	PN212 = models.FloatField('PN 2,5', null = True)
	PN6 = models.FloatField('PN 6', null = True)
	PN10 = models.FloatField('PN 10', null = True)
	PN16 = models.FloatField('PN 16', null = True)
	PN25 = models.FloatField('PN 25', null = True)
	PN40 = models.FloatField('PN 40', null = True)


class Flange11(models.Model):
	pipe_diam = models.FloatField('pipe_diam')
	PN212 = models.FloatField('PN 2,5', null = True)
	PN6 = models.FloatField('PN 6', null = True)
	PN10 = models.FloatField('PN 10', null = True)
	PN16 = models.FloatField('PN 16', null = True)
	PN25 = models.FloatField('PN 25', null = True)
	PN40 = models.FloatField('PN 40', null = True)
	PN63 = models.FloatField('PN 63', null = True)
	PN100 = models.FloatField('PN 100', null = True)
	PN160 = models.FloatField('PN 160', null = True)
	PN250 = models.FloatField('PN 250', null = True)
	PN320 = models.FloatField('PN 320', null = True)
	PN400 = models.FloatField('PN 400', null = True)


class Flange13(models.Model):
	pipe_diam = models.FloatField('pipe_diam')
	PN212 = models.FloatField('PN 2,5', null = True)
	PN6 = models.FloatField('PN 6', null = True)
	PN10 = models.FloatField('PN 10', null = True)
	PN16 = models.FloatField('PN 16', null = True)
	PN25 = models.FloatField('PN 25', null = True)
	PN40 = models.FloatField('PN 40', null = True)
	PN63 = models.FloatField('PN 63', null = True)
	PN100 = models.FloatField('PN 100', null = True)


class  Angle90(models.Model):
	pipe_diam = models.FloatField('pipe_diam')
	install_length = models.FloatField('installation length in mm')


class  Angle180(models.Model):
	pipe_diam = models.FloatField('pipe_diam')
	install_length = models.FloatField('installation length in mm')


class TPieceDIN(models.Model):
	pipe_diam = models.FloatField('pipe_diam')
	install_length = models.FloatField('installation length in mm')


class TReducerPieceDIN(models.Model):
	pipe_diam_big = models.FloatField('pipe_diam big')
	pipe_diam_small = models.FloatField('pipe_diam small')
	install_length_big = models.FloatField('install_length for big center pipe in mm')
	install_length_small = models.FloatField('install_length for small center pipe in mm')


class ReducerDIN(models.Model):
	pipe_diam_big = models.FloatField('pipe_diam big')
	pipe_diam_small = models.FloatField('pipe_diam small')
	install_length = models.FloatField('install_length for in mm')


class Caps(models.Model):
	pipe_diam = models.FloatField('pipe_diam')
	install_length = models.FloatField('installation length in mm')
	TValueinterval = models.FloatField('T value <= ', null = True)
	install_length_T = models.FloatField('installation length in mm', null = True)


class AllSpieces(models.Model):
	name = models.CharField(max_length=50)