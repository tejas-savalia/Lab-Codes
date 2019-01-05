sca;
close all;
clearvars;

PsychDefaultSetup(2);

screens = Screen('Screens');
screenNumber = max(screens);

white = WhiteIndex(screenNumber);
black = BlackIndex(screenNumber);
grey = white/2;

[window, windowRect] = PsychImaging('OpenWindow', screenNumber, grey);
[screenXPixels, screenYPixels] = Screen('WindowSize', window);
[xCenter, yCenter] = RectCenter(windowRect);

ifi = Screen('GetFlipInterval', window);
numSecs = 1;
numFrames = round(numSecs/ifi);
vb1 = Screen('Flip', window);
SetMouse(xCenter-1, yCenter-1, window);

dotColor = [1, 0, 0];
dotSizePix = 20;
HideCursor();
Screen('DrawDots', window, [xCenter, yCenter], dotSizePix, dotColor, [], 2);
Screen('Flip', window);    
for frame = 1:10*numFrames
    Screen('FillRect', window, [0, 0.5, 0.5]);
    [x, y, buttons] = GetMouse(window);
    r = sqrt((x - xCenter)^2 + (y - yCenter)^2);
    theta = acos((x - xCenter)/r);
    if buttons(1) 
        HideCursor();
        %SetMouse(x + r*cos(theta+pi/4), y + r*sin(theta+pi/4), window);
        Screen('DrawDots', window, [xCenter + r*cos(theta+pi/4), yCenter + r*sin(theta+pi/4)], dotSizePix, dotColor, [], 2);        
    end
    if ~buttons(1)
        SetMouse(xCenter, yCenter, window);
        Screen('DrawDots', window, [xCenter, yCenter], dotSizePix, dotColor, [], 2);        
    end
        
    
    Screen('Flip', window);
    
end
%SetMouse(400, 400, window)
KbStrokeWait;
    
sca;