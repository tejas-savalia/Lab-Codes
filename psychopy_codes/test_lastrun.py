#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on October 02, 2019, at 23:40
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.2.3'
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\psychopy_codes\\test_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_experiment_starts_now = visual.TextStim(win=win, name='text_experiment_starts_now',
    text='Ready?\n\nThe experiment starts now!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
noise = visual.NoiseStim(
    win=win, name='noise',
    noiseImage=None, mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5), sf=None,
    phase=0.0,
    color=[1,1,1], colorSpace='rgb',     opacity=1, blendmode='avg', contrast=1.0,
    texRes=128, filter=None,
    noiseType='Binary', noiseElementSize=0.0625, 
    noiseBaseSf=8.0, noiseBW=1,
    noiseBWO=30, noiseOri=0.0,
    noiseFractalPower=0.0,noiseFilterLower=1.0,
    noiseFilterUpper=8.0, noiseFilterOrder=0.0,
    noiseClip=3.0, imageComponent='Phase', interpolate=False, depth=-1.0)
noise.buildNoise()
circle = visual.Polygon(
    win=win, name='circle',
    edges=4000, size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
routineTimer.add(7.000000)
# update component parameters for each repeat
# keep track of which components have finished
trialComponents = [text_experiment_starts_now, noise, circle]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1
continueRoutine = True

# -------Run Routine "trial"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_experiment_starts_now* updates
    if text_experiment_starts_now.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_experiment_starts_now.frameNStart = frameN  # exact frame index
        text_experiment_starts_now.tStart = t  # local t and not account for scr refresh
        text_experiment_starts_now.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_experiment_starts_now, 'tStartRefresh')  # time at next scr refresh
        text_experiment_starts_now.setAutoDraw(True)
    if text_experiment_starts_now.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_experiment_starts_now.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_experiment_starts_now.tStop = t  # not accounting for scr refresh
            text_experiment_starts_now.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_experiment_starts_now, 'tStopRefresh')  # time at next scr refresh
            text_experiment_starts_now.setAutoDraw(False)
    
    # *noise* updates
    if noise.status == NOT_STARTED and tThisFlip >= 01.0-frameTolerance:
        # keep track of start time/frame for later
        noise.frameNStart = frameN  # exact frame index
        noise.tStart = t  # local t and not account for scr refresh
        noise.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(noise, 'tStartRefresh')  # time at next scr refresh
        noise.setAutoDraw(True)
    if noise.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > noise.tStartRefresh + 2.0-frameTolerance:
            # keep track of stop time/frame for later
            noise.tStop = t  # not accounting for scr refresh
            noise.frameNStop = frameN  # exact frame index
            win.timeOnFlip(noise, 'tStopRefresh')  # time at next scr refresh
            noise.setAutoDraw(False)
    if noise.status == STARTED:
        if noise._needBuild:
            noise.buildNoise()
    
    # *circle* updates
    if circle.status == NOT_STARTED and tThisFlip >= 3.0-frameTolerance:
        # keep track of start time/frame for later
        circle.frameNStart = frameN  # exact frame index
        circle.tStart = t  # local t and not account for scr refresh
        circle.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(circle, 'tStartRefresh')  # time at next scr refresh
        circle.setAutoDraw(True)
    if circle.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > circle.tStartRefresh + 4.0-frameTolerance:
            # keep track of stop time/frame for later
            circle.tStop = t  # not accounting for scr refresh
            circle.frameNStop = frameN  # exact frame index
            win.timeOnFlip(circle, 'tStopRefresh')  # time at next scr refresh
            circle.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_experiment_starts_now.started', text_experiment_starts_now.tStartRefresh)
thisExp.addData('text_experiment_starts_now.stopped', text_experiment_starts_now.tStopRefresh)
thisExp.addData('noise.started', noise.tStartRefresh)
thisExp.addData('noise.stopped', noise.tStopRefresh)
thisExp.addData('circle.started', circle.tStartRefresh)
thisExp.addData('circle.stopped', circle.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
