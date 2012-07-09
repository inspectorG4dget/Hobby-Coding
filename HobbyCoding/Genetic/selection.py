'''
Created on Mar 16, 2012

@author: ashwin
'''

from random import choice as choose, sample, random as rand, uniform as randfloat
from population import *
from GP import *
from sys import exit as crash
from copy import deepcopy as clone

def tournamentSelect(pop, SCORES, scorefunc, scoreparams, T, N):
	""" Return N individuals from the population by conducting tournaments of size T.
		Each tournament has exactly one winner """
	from population import functify
	
#	from population import score
	answer = []
	for _ in xrange(N):
		gladiators = sample(pop, T)
		for g in gladiators:
			if functify(g) not in SCORES:
				SCORES[functify(g)] = scorefunc(g, *scoreparams)
		answer.append(max(gladiators, key=lambda p: SCORES[functify(p)]))
	
	return answer

def getRouletteWheel(population, SCORES, scorefunc, scoreparams):
	""" Return a fitness-proportional roulette wheel for the population"""
	from population import functify
	wheel={}
	top = 0.0
	for p in population:
		if functify(p) not in SCORES: SCORES[functify(p)] = scorefunc(p, *scoreparams)
	totalscore = abs(sum((SCORES[functify(p)] for p in population)))
	
	for p in population:
		fit = SCORES[functify(p)]/totalscore
		wheel[(top, top+fit)] = clone(p)
		top += fit
	
#	print 'returning wheel'	##
	return wheel

def rouletteWheelSelect(population, SCORES, scorefunc, scoreparams, N):
	""" Select N unique individuals from the population based on roulette wheel selection.
		If there are not at least N individuals in the population, ValueError is raised """
	
	if len(population) < N: raise ValueError("Cannot Select %d individuals from a population of %d" %(N, len(population)))
	
#	print 'getting wheel'	##
	wheel = getRouletteWheel(population, SCORES, scorefunc, scoreparams)
#	print 'got wheel'	##
	answer = []
	selection = set([])
	
	while N:
#		print 'while', N	##
		try:
#			print 'trying'	##
			r = randfloat(-1,0)
			slot = (s for s in wheel if s[1]<=r<=s[0]).next()
			answer.append(wheel[slot])
			selection.add(slot)
			N -= 1
		except:
#			print 'excepting'	##
			print r
			for slot in wheel: print slot
			raise
			crash()
	
	return answer