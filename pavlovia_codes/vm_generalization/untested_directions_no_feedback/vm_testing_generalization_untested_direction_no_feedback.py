#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.2.3),
    on May 15, 2020, at 20:34
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
expName = 'vm_testing_generalization_untested_direction_no_feedback'  # from the Builder filename that created this script
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
    originPath='C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\pavlovia_codes\\vm_generalization\\untested_directions_no_feedback\\vm_testing_generalization_untested_direction_no_feedback.py',
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
    size=[1280, 720], fullscr=True, screen=0, 
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

# Initialize components for Routine "baseline"
baselineClock = core.Clock()
inner = visual.Polygon(
    win=win, name='inner',
    edges=64, size=(0.7, 0.7),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixation = visual.Polygon(
    win=win, name='fixation',
    edges=64, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
mouse_fixation = event.Mouse(win=win)
x, y = [None, None]
mouse_fixation.mouseClock = core.Clock()
target = visual.Rect(
    win=win, name='target',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "rotated"
rotatedClock = core.Clock()
inner_2 = visual.Polygon(
    win=win, name='inner_2',
    edges=64, size=(0.7, 0.7),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixation_2 = visual.Polygon(
    win=win, name='fixation_2',
    edges=64, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
mouse_fixation_2 = event.Mouse(win=win)
x, y = [None, None]
mouse_fixation_2.mouseClock = core.Clock()
target_2 = visual.Rect(
    win=win, name='target_2',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)

# Initialize components for Routine "transfer"
transferClock = core.Clock()
inner_3 = visual.Polygon(
    win=win, name='inner_3',
    edges=64, size=(0.7, 0.7),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,0,0], lineColorSpace='rgb',
    fillColor=[0,0,0], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fixation_3 = visual.Polygon(
    win=win, name='fixation_3',
    edges=64, size=(0.05, 0.05),
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-1.0, interpolate=True)
mouse_fixation_3 = event.Mouse(win=win)
x, y = [None, None]
mouse_fixation_3.mouseClock = core.Clock()
target_3 = visual.Rect(
    win=win, name='target_3',
    width=(0.1, 0.1)[0], height=(0.1, 0.1)[1],
    ori=45, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1.0, depth=-3.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_baseline.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "baseline"-------
    # update component parameters for each repeat
    fixation.setPos([0, 0])
    # setup some python lists for storing info about the mouse_fixation
    mouse_fixation.x = []
    mouse_fixation.y = []
    mouse_fixation.leftButton = []
    mouse_fixation.midButton = []
    mouse_fixation.rightButton = []
    mouse_fixation.time = []
    mouse_fixation.clicked_name = []
    gotValidClick = False  # until a click is received
    target.setOpacity(1)
    target.setPos((target_x, target_y))
    core.wait(normal(0.75, 0.5))
    isi = normal(0.75, 0.5)
    thisExp.addData('isi', isi)
    mouse_fixation.setPos((0, 0))
    win.mouseVisible = False
    
    # keep track of which components have finished
    baselineComponents = [inner, fixation, mouse_fixation, target]
    for thisComponent in baselineComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    baselineClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "baseline"-------
    while continueRoutine:
        # get current time
        t = baselineClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=baselineClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inner* updates
        if inner.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            inner.frameNStart = frameN  # exact frame index
            inner.tStart = t  # local t and not account for scr refresh
            inner.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inner, 'tStartRefresh')  # time at next scr refresh
            inner.setAutoDraw(True)
        
        # *fixation* updates
        if fixation.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation.frameNStart = frameN  # exact frame index
            fixation.tStart = t  # local t and not account for scr refresh
            fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
            fixation.setAutoDraw(True)
        if fixation.status == STARTED:  # only update if drawing
            fixation.setOpacity(1 - fixation.overlaps(inner), log=False)
        # *mouse_fixation* updates
        if mouse_fixation.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_fixation.frameNStart = frameN  # exact frame index
            mouse_fixation.tStart = t  # local t and not account for scr refresh
            mouse_fixation.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_fixation, 'tStartRefresh')  # time at next scr refresh
            mouse_fixation.status = STARTED
            mouse_fixation.mouseClock.reset()
            prevButtonState = mouse_fixation.getPressed()  # if button is down already this ISN'T a new click
        if mouse_fixation.status == STARTED:
            if bool(not fixation.overlaps(inner)):
                # keep track of stop time/frame for later
                mouse_fixation.tStop = t  # not accounting for scr refresh
                mouse_fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_fixation, 'tStopRefresh')  # time at next scr refresh
                mouse_fixation.status = FINISHED
        if mouse_fixation.status == STARTED:  # only update if started and not finished!
            x, y = mouse_fixation.getPos()
            mouse_fixation.x.append(x)
            mouse_fixation.y.append(y)
            buttons = mouse_fixation.getPressed()
            mouse_fixation.leftButton.append(buttons[0])
            mouse_fixation.midButton.append(buttons[1])
            mouse_fixation.rightButton.append(buttons[2])
            mouse_fixation.time.append(mouse_fixation.mouseClock.getTime())
            buttons = mouse_fixation.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target]:
                        if obj.contains(mouse_fixation):
                            gotValidClick = True
                            mouse_fixation.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *target* updates
        if target.status == NOT_STARTED and tThisFlip >= isi-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            target.setAutoDraw(True)
        if target.status == STARTED:
            if bool(fixation.overlaps(target)):
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target, 'tStopRefresh')  # time at next scr refresh
                target.setAutoDraw(False)
        mouse_pos = mouse_fixation.getPos()
        new_mouse_pos = mouse_pos[0]*cos(pi*rotation/180) - mouse_pos[1]*sin(pi*rotation/180), mouse_pos[0]*sin(pi*rotation/180) + mouse_pos[1]*cos(pi*rotation/180)
        fixation.pos = new_mouse_pos[0], new_mouse_pos[1]
        if mouse_fixation.getPressed()[0]:
            fixation.opacity = 0
            if not (fixation.overlaps(inner)):
                fixation.opacity = 1
                win.flip()
                if (fixation.overlaps(target)):
                    target.opacity = 0
                    win.flip()
                continueRoutine = False 
        else:
            fixation.opacity = 1
            mouse_fixation.setPos((0, 0)) 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in baselineComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "baseline"-------
    for thisComponent in baselineComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inner.started', inner.tStartRefresh)
    thisExp.addData('inner.stopped', inner.tStopRefresh)
    thisExp.addData('fixation.started', fixation.tStartRefresh)
    thisExp.addData('fixation.stopped', fixation.tStopRefresh)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_fixation.x', mouse_fixation.x)
    thisExp.addData('mouse_fixation.y', mouse_fixation.y)
    thisExp.addData('mouse_fixation.leftButton', mouse_fixation.leftButton)
    thisExp.addData('mouse_fixation.midButton', mouse_fixation.midButton)
    thisExp.addData('mouse_fixation.rightButton', mouse_fixation.rightButton)
    thisExp.addData('mouse_fixation.time', mouse_fixation.time)
    thisExp.addData('mouse_fixation.clicked_name', mouse_fixation.clicked_name)
    thisExp.addData('mouse_fixation.started', mouse_fixation.tStart)
    thisExp.addData('mouse_fixation.stopped', mouse_fixation.tStop)
    thisExp.nextEntry()
    thisExp.addData('target.started', target.tStartRefresh)
    thisExp.addData('target.stopped', target.tStopRefresh)
    fixation.opacity = 1
    fixation.pos = ((0, 0))
    core.wait(1.0)
    #mouse_fixation.setPos((0, 0))
    
    # the Routine "baseline" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials'


# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_rotated_sudden.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "rotated"-------
    # update component parameters for each repeat
    fixation_2.setPos([0, 0])
    # setup some python lists for storing info about the mouse_fixation_2
    mouse_fixation_2.x = []
    mouse_fixation_2.y = []
    mouse_fixation_2.leftButton = []
    mouse_fixation_2.midButton = []
    mouse_fixation_2.rightButton = []
    mouse_fixation_2.time = []
    mouse_fixation_2.clicked_name = []
    gotValidClick = False  # until a click is received
    target_2.setOpacity(1)
    target_2.setPos((target_x, target_y))
    core.wait(normal(0.75, 0.5))
    isi = normal(0.75, 0.5)
    thisExp.addData('isi',isi)
    mouse_fixation_2.setPos((0, 0))
    win.mouseVisible = False
    
    # keep track of which components have finished
    rotatedComponents = [inner_2, fixation_2, mouse_fixation_2, target_2]
    for thisComponent in rotatedComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    rotatedClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "rotated"-------
    while continueRoutine:
        # get current time
        t = rotatedClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=rotatedClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inner_2* updates
        if inner_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            inner_2.frameNStart = frameN  # exact frame index
            inner_2.tStart = t  # local t and not account for scr refresh
            inner_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inner_2, 'tStartRefresh')  # time at next scr refresh
            inner_2.setAutoDraw(True)
        
        # *fixation_2* updates
        if fixation_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_2.frameNStart = frameN  # exact frame index
            fixation_2.tStart = t  # local t and not account for scr refresh
            fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_2, 'tStartRefresh')  # time at next scr refresh
            fixation_2.setAutoDraw(True)
        if fixation_2.status == STARTED:  # only update if drawing
            fixation_2.setOpacity(1 - fixation_2.overlaps(inner_2), log=False)
        # *mouse_fixation_2* updates
        if mouse_fixation_2.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_fixation_2.frameNStart = frameN  # exact frame index
            mouse_fixation_2.tStart = t  # local t and not account for scr refresh
            mouse_fixation_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_fixation_2, 'tStartRefresh')  # time at next scr refresh
            mouse_fixation_2.status = STARTED
            mouse_fixation_2.mouseClock.reset()
            prevButtonState = mouse_fixation_2.getPressed()  # if button is down already this ISN'T a new click
        if mouse_fixation_2.status == STARTED:
            if bool(not fixation_2.overlaps(inner_2)):
                # keep track of stop time/frame for later
                mouse_fixation_2.tStop = t  # not accounting for scr refresh
                mouse_fixation_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_fixation_2, 'tStopRefresh')  # time at next scr refresh
                mouse_fixation_2.status = FINISHED
        if mouse_fixation_2.status == STARTED:  # only update if started and not finished!
            x, y = mouse_fixation_2.getPos()
            mouse_fixation_2.x.append(x)
            mouse_fixation_2.y.append(y)
            buttons = mouse_fixation_2.getPressed()
            mouse_fixation_2.leftButton.append(buttons[0])
            mouse_fixation_2.midButton.append(buttons[1])
            mouse_fixation_2.rightButton.append(buttons[2])
            mouse_fixation_2.time.append(mouse_fixation_2.mouseClock.getTime())
            buttons = mouse_fixation_2.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target_2]:
                        if obj.contains(mouse_fixation_2):
                            gotValidClick = True
                            mouse_fixation_2.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *target_2* updates
        if target_2.status == NOT_STARTED and tThisFlip >= isi-frameTolerance:
            # keep track of start time/frame for later
            target_2.frameNStart = frameN  # exact frame index
            target_2.tStart = t  # local t and not account for scr refresh
            target_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_2, 'tStartRefresh')  # time at next scr refresh
            target_2.setAutoDraw(True)
        if target_2.status == STARTED:
            if bool(fixation_2.overlaps(target_2)):
                # keep track of stop time/frame for later
                target_2.tStop = t  # not accounting for scr refresh
                target_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_2, 'tStopRefresh')  # time at next scr refresh
                target_2.setAutoDraw(False)
        mouse_pos = mouse_fixation_2.getPos()
        new_mouse_pos = mouse_pos[0]*cos(pi*rotation/180) - mouse_pos[1]*sin(pi*rotation/180), mouse_pos[0]*sin(pi*rotation/180) + mouse_pos[1]*cos(pi*rotation/180)
        fixation_2.pos = new_mouse_pos[0], new_mouse_pos[1]
        if mouse_fixation_2.getPressed()[0]:
            fixation_2.opacity = 0
            if not (fixation_2.overlaps(inner_2)):
                fixation_2.opacity = 1
                win.flip()
                if (fixation_2.overlaps(target_2)):
                    target_2.opacity = 0
                    win.flip()
                continueRoutine = False 
        else:
            fixation_2.opacity = 1
            mouse_fixation_2.setPos((0, 0)) 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in rotatedComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rotated"-------
    for thisComponent in rotatedComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inner_2.started', inner_2.tStartRefresh)
    thisExp.addData('inner_2.stopped', inner_2.tStopRefresh)
    thisExp.addData('fixation_2.started', fixation_2.tStartRefresh)
    thisExp.addData('fixation_2.stopped', fixation_2.tStopRefresh)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_fixation_2.x', mouse_fixation_2.x)
    thisExp.addData('mouse_fixation_2.y', mouse_fixation_2.y)
    thisExp.addData('mouse_fixation_2.leftButton', mouse_fixation_2.leftButton)
    thisExp.addData('mouse_fixation_2.midButton', mouse_fixation_2.midButton)
    thisExp.addData('mouse_fixation_2.rightButton', mouse_fixation_2.rightButton)
    thisExp.addData('mouse_fixation_2.time', mouse_fixation_2.time)
    thisExp.addData('mouse_fixation_2.clicked_name', mouse_fixation_2.clicked_name)
    thisExp.addData('mouse_fixation_2.started', mouse_fixation_2.tStart)
    thisExp.addData('mouse_fixation_2.stopped', mouse_fixation_2.tStop)
    thisExp.nextEntry()
    thisExp.addData('target_2.started', target_2.tStartRefresh)
    thisExp.addData('target_2.stopped', target_2.tStopRefresh)
    fixation_2.opacity = 1
    core.wait(1.0)
    #mouse_fixation.setPos((0, 0))
    
    # the Routine "rotated" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 0 repeats of 'trials_2'


# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions_baseline.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "transfer"-------
    # update component parameters for each repeat
    fixation_3.setPos([0, 0])
    # setup some python lists for storing info about the mouse_fixation_3
    mouse_fixation_3.x = []
    mouse_fixation_3.y = []
    mouse_fixation_3.leftButton = []
    mouse_fixation_3.midButton = []
    mouse_fixation_3.rightButton = []
    mouse_fixation_3.time = []
    mouse_fixation_3.clicked_name = []
    gotValidClick = False  # until a click is received
    target_3.setOpacity(1)
    target_3.setPos((target_x, target_y))
    core.wait(normal(0.75, 0.5))
    isi = normal(0.75, 0.5)
    thisExp.addData('isi', isi)
    mouse_fixation_3.setPos((0, 0))
    win.mouseVisible = False
    
    # keep track of which components have finished
    transferComponents = [inner_3, fixation_3, mouse_fixation_3, target_3]
    for thisComponent in transferComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    transferClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    continueRoutine = True
    
    # -------Run Routine "transfer"-------
    while continueRoutine:
        # get current time
        t = transferClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=transferClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *inner_3* updates
        if inner_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            inner_3.frameNStart = frameN  # exact frame index
            inner_3.tStart = t  # local t and not account for scr refresh
            inner_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(inner_3, 'tStartRefresh')  # time at next scr refresh
            inner_3.setAutoDraw(True)
        
        # *fixation_3* updates
        if fixation_3.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            fixation_3.frameNStart = frameN  # exact frame index
            fixation_3.tStart = t  # local t and not account for scr refresh
            fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_3, 'tStartRefresh')  # time at next scr refresh
            fixation_3.setAutoDraw(True)
        if fixation_3.status == STARTED:  # only update if drawing
            fixation_3.setOpacity(1 - fixation_3.overlaps(inner_3), log=False)
        # *mouse_fixation_3* updates
        if mouse_fixation_3.status == NOT_STARTED and t >= 0-frameTolerance:
            # keep track of start time/frame for later
            mouse_fixation_3.frameNStart = frameN  # exact frame index
            mouse_fixation_3.tStart = t  # local t and not account for scr refresh
            mouse_fixation_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(mouse_fixation_3, 'tStartRefresh')  # time at next scr refresh
            mouse_fixation_3.status = STARTED
            mouse_fixation_3.mouseClock.reset()
            prevButtonState = mouse_fixation_3.getPressed()  # if button is down already this ISN'T a new click
        if mouse_fixation_3.status == STARTED:
            if bool(not fixation_3.overlaps(inner_3)):
                # keep track of stop time/frame for later
                mouse_fixation_3.tStop = t  # not accounting for scr refresh
                mouse_fixation_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(mouse_fixation_3, 'tStopRefresh')  # time at next scr refresh
                mouse_fixation_3.status = FINISHED
        if mouse_fixation_3.status == STARTED:  # only update if started and not finished!
            x, y = mouse_fixation_3.getPos()
            mouse_fixation_3.x.append(x)
            mouse_fixation_3.y.append(y)
            buttons = mouse_fixation_3.getPressed()
            mouse_fixation_3.leftButton.append(buttons[0])
            mouse_fixation_3.midButton.append(buttons[1])
            mouse_fixation_3.rightButton.append(buttons[2])
            mouse_fixation_3.time.append(mouse_fixation_3.mouseClock.getTime())
            buttons = mouse_fixation_3.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [target_3]:
                        if obj.contains(mouse_fixation_3):
                            gotValidClick = True
                            mouse_fixation_3.clicked_name.append(obj.name)
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # *target_3* updates
        if target_3.status == NOT_STARTED and tThisFlip >= isi-frameTolerance:
            # keep track of start time/frame for later
            target_3.frameNStart = frameN  # exact frame index
            target_3.tStart = t  # local t and not account for scr refresh
            target_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_3, 'tStartRefresh')  # time at next scr refresh
            target_3.setAutoDraw(True)
        if target_3.status == STARTED:
            if bool(fixation_3.overlaps(target_3)):
                # keep track of stop time/frame for later
                target_3.tStop = t  # not accounting for scr refresh
                target_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(target_3, 'tStopRefresh')  # time at next scr refresh
                target_3.setAutoDraw(False)
        mouse_pos = mouse_fixation_3.getPos()
        new_mouse_pos = mouse_pos[0]*cos(pi*rotation/180) - mouse_pos[1]*sin(pi*rotation/180), mouse_pos[0]*sin(pi*rotation/180) + mouse_pos[1]*cos(pi*rotation/180)
        fixation_3.pos = new_mouse_pos[0], new_mouse_pos[1]
        if mouse_fixation_3.getPressed()[0]:
            fixation_3.opacity = 0
            if not (fixation_3.overlaps(inner_3)):
                fixation_3.opacity = 1
                win.flip()
                if (fixation_3.overlaps(target_3)):
                    target_3.opacity = 0
                    win.flip()
                continueRoutine = False 
        else:
            fixation_3.opacity = 1
            mouse_fixation_3.setPos((0, 0)) 
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in transferComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "transfer"-------
    for thisComponent in transferComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('inner_3.started', inner_3.tStartRefresh)
    thisExp.addData('inner_3.stopped', inner_3.tStopRefresh)
    thisExp.addData('fixation_3.started', fixation_3.tStartRefresh)
    thisExp.addData('fixation_3.stopped', fixation_3.tStopRefresh)
    # store data for thisExp (ExperimentHandler)
    thisExp.addData('mouse_fixation_3.x', mouse_fixation_3.x)
    thisExp.addData('mouse_fixation_3.y', mouse_fixation_3.y)
    thisExp.addData('mouse_fixation_3.leftButton', mouse_fixation_3.leftButton)
    thisExp.addData('mouse_fixation_3.midButton', mouse_fixation_3.midButton)
    thisExp.addData('mouse_fixation_3.rightButton', mouse_fixation_3.rightButton)
    thisExp.addData('mouse_fixation_3.time', mouse_fixation_3.time)
    thisExp.addData('mouse_fixation_3.clicked_name', mouse_fixation_3.clicked_name)
    thisExp.addData('mouse_fixation_3.started', mouse_fixation_3.tStart)
    thisExp.addData('mouse_fixation_3.stopped', mouse_fixation_3.tStop)
    thisExp.nextEntry()
    thisExp.addData('target_3.started', target_3.tStartRefresh)
    thisExp.addData('target_3.stopped', target_3.tStopRefresh)
    fixation_3.opacity = 1
    fixation_3.pos = ((0, 0))
    core.wait(1.0)
    #mouse_fixation.setPos((0, 0))
    
    # the Routine "transfer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_3'


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
