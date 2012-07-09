'''
Created on Mar 16, 2012

@author: ashwin
'''

from population import *
from selection import *
from mutation import *
from crossover import *
from settings import *
#from visualize import *
from itertools import imap, ifilter
from sys import exit as crash
from random import random as rand, uniform as Rand, sample
from time import sleep


def runGP(*args, **kwargs): #maxGenerations, targetscore, inputs, targets, popsize, ADFs, terminals, (genfunc, selectfunc, crossfunc), (crossprob, reprob, mutprob)):
	arguments = """ maxFitnessEvals targetscore
					popsize ADFs terminals genfunc 
					inputs targets
					height minheight
					scorefunc scoreparams elitism
					selectfunc selectparams
					crossfunc crossparams
					mutfunc mutparams
					crossprob mutprob""".split()
	
	if len(args) < len(arguments):
		raise TypeError("Missing Arguements: %s" %' '.join([a for a in arguments if a not in args]))

	# # # # # # PARAMETERS # # # # # #
		
	maxFitnessEvals = kwargs['maxFitnessEvals']
	targetscore = kwargs['targetscore']
	popsize = kwargs['popsize']
	ADFs = kwargs['ADFs']
	terminals = kwargs['terminals']
	genfunc = kwargs['genfunc']
	inputs = kwargs['inputs']
	targets = kwargs['targets']
	height = kwargs['height']
	minheight = kwargs['minheight']

	scorefunc = kwargs['scorefunc']
	scoreparams = kwargs['scoreparams']

	selectfunc = kwargs['selectfunc']
	selectparams = kwargs['selectparams']
	
	elitism = kwargs['elitism']
	crossfunc = kwargs['crossfunc']
	crossprob = kwargs['crossprob']
	crossparams = kwargs['crossparams']
	reprob = 1-crossprob

	mutfunc = kwargs['mutfunc']
	mutprob = kwargs['mutprob']
	mutparams = kwargs['mutparams']
#	logfile = open(kwargs['logfilepath'], 'w')

	# # # # # # /PARAMETERS # # # # # #
	
	e = False
	pop = genPop(popsize, height, minheight, genfunc, ADFs, terminals)
	SCORES = dict(((functify(f), scorefunc(f, *scoreparams)) for f in pop))
	best = None, None	# indiv, score
#	print 'len(pop):', len(pop)	##
	while maxFitnessEvals>0:
		print maxFitnessEvals, 	##
		
		newPop = sorted(pop, key=lambda p: scorefunc(p, *scoreparams), reverse=True)[:int(len(pop)*elitism)]
		maxFitnessEvals -= len(newPop)
		newpopsize = popsize - len(newPop)
		for _ in xrange(newpopsize/2):
#			print g,_	##
			
			r = rand()
			if r <= crossprob:
#				print 'gotta cross', g,_	##
#				print locals().keys(), '\n', globals().keys(); crash()	##
				p1,p2 = selectfunc(pop, *selectparams)
				if selectfunc == tournamentSelect: maxFitnessEvals -= selectparams[-2]
				elif selectfunc == rouletteWheelSelect: maxFitnessEvals -= len(pop)
#				print "crossing over", g,_	##
				children = list(crossfunc(p1, p2, *crossparams))
				
				for i,child in enumerate(children):
					m = rand()
					children[i] = max(mutfunc(child, *mutparams), key=lambda ch:scorefunc(ch, *scoreparams))
					maxFitnessEvals -= len(mutfunc(child, *mutparams))
				newPop.extend(children)
#				print "done crossing over", g,_	##
				
			else:
#				print locals().keys(), '\n', globals().keys(); crash()	##
#				print 'selecting by wheel for reprob'	##
				newbies = selectfunc(pop, *selectparams)
#				print 'selecting by wheel for reprob'	##
				if len(newbies) < 2: newbies += selectfunc(pop, *selectparams)
					
				for i,newb in enumerate(newbies):
					m = rand()
				newPop.extend(map(lambda c: max(mutfunc(c, *mutparams), key=lambda ch:scorefunc(ch, *scoreparams)), newbies))
#				newPop.extend(map(lambda c: mutfunc(c, *mutparams), newbies))
			
		pop = newPop
		for p in pop:
			if functify(p) not in SCORES: SCORES[functify(p)] = scorefunc(p, *scoreparams)
			
		fittest = max(newPop, key=lambda f: SCORES[functify(f)])
#		print '\nmaxscore:', max((scorefunc(p, *scoreparams) for p in pop))	##
#		print 'minscore:', min((scorefunc(p, *scoreparams) for p in pop))	##
		topscore = SCORES[functify(fittest)]
#		print 'topscore:', topscore	##
		if topscore >= best[1]:
#			print topscore	##
			best = [f for f in newPop if SCORES[functify(f)] == topscore], topscore
			if topscore >= targetscore:
				functifieds = imap(functify, newPop)
#				for f in functifieds:
#					if f not in SCORES:
#						SCORES[f] = scorefunc(f, *scoreparams)
				best = [f for f in functifieds if (f in SCORES and SCORES[f] == topscore)]
##				best += [f for f in functifieds if scorefunc(f, *scoreparams) == topscore]
#

				return best, maxFitnessEvals
		print topscore, functify(fittest)#, '\n'	##
		
		
#		print '\t', sorted(set([scorefunc(f, *scoreparams) for f in pop]))	##
#		print '-'*30	##
#		logfile.write("%s\t%s\n" %(topscore, functify(fittest)))
	
	topscore = max((imap(lambda f: SCORES[functify(f)], newPop)))
	answer = [functify(f) for f in newPop if SCORES[functify(f)] == topscore], maxFitnessEvals
#	logfile.write("%s"%'\n'.join(answer[0])); logfile.close()
	print "%s"%'\n'.join(answer[0])
	return answer

if __name__ == "__main__":
	print 'starting'
	
#	createVizSettings(setId)
	
	numInputs = len(INPUTS)
	_INPUTS = []
	delt = INPUTS[0][-1]
	for i in xrange(1, numInputs):
		_INPUTS.append([TARGETS[i-1]]+[INPUTS[i][-2]])
	INPUTS = _INPUTS
	TARGETS = TARGETS[1:]
	TERMINALS = map(float, [-1,0,1, delt]) + "x1 x2 x3".split() + [Rand(-1,1)]
	
	allparams = """ maxFitnessEvals 10**6
					targetscore 0
					popsize 100
					ADFs ADFs
					terminals TERMINALS
					genfunc generateRamped
					inputs INPUTS
					targets TARGETS
					height 4
					minheight 2
					scorefunc score
					scoreparams (gpParams['inputs'], gpParams['targets'])
					selectfunc tournamentSelect 
					selectparams (SCORES, gpParams['scorefunc'], gpParams['scoreparams'], 7, 2)
					mutfunc pointMutation
					mutparams (ADFs, TERMINALS)
					crossfunc crossover
					crossparams (maxheight,)
					crossprob 0.9
					mutprob 0.01
					elitism 0.1"""
#					scorefunc GMTIscore
#					scoreparams (gpParams['inputs'], gpParams['targets'])
#					selectfunc rouletteWheelSelect 
#					selectparams (SCORES, gpParams['scorefunc'], (gpParams['inputs'], gpParams['targets']), 2)
#					mutfunc headlessChickenMutation
#					mutparams (SCORES, ADFs, TERMINALS, gpParams['scorefunc'], gpParams['scoreparams'], maxheight)
	
	gpParams = {}
	for line in allparams.split('\n'):
		k,v = map(lambda s: s.strip(), line.strip().split(' ', 1))
		gpParams[k] = eval(v)
	
	MUTRATES = {(0, -5): 0,
				(-5,-10): 1,
				(-10,-15): 2,
				(-15,-20):3,
				(-20,None):4}
	
	answer = runGP(*gpParams.keys(), **gpParams)
	print 'answer:', answer
