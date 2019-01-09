%Trial Structure
%Only one square at a time.
%90 degree rotation.
%Two cases: Gradual and Sudden
%RMSE, IDE and MT
%After effects stage
%Auditory cue
%Color change on hit
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
[screenXpixels, screenYpixels] = Screen('WindowSize', window);
[xCenter, yCenter] = RectCenter(windowRect);

ifi = Screen('GetFlipInterval', window);
numSecs = 10;
numFrames = round(numSecs/ifi);
vb1 = Screen('Flip', window);
SetMouse(xCenter-1, yCenter - 1, window);

dotColor = [1, 0, 0];
dotSizePix = 20;
HideCursor();
rotateBy = pi/4;
Screen('DrawDots', window, [xCenter, yCenter], dotSizePix, dotColor, [], 2);
Screen('Flip', window);    
Xs = [];
Ys = [];
for frame = 1:numFrames
    Screen('FillRect', window, [0, 0.5, 0.5]);
    [x, y, buttons] = GetMouse(window);
    theta = atan(y-yCenter/x-xCenter);
    r = (x-xCenter)/cos(theta);
    %theta = acos((x - xCenter)/r);
    
    baseRect = [0 0 100 100];

    squareTheta = [0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4];

    % Screen X positions of 6 rectangles
    squareXpos = 300*cos(squareTheta) + xCenter;
    squareYpos = 300*sin(squareTheta) + yCenter;
    numSqaures = length(squareXpos);

    % Set the colors to Red
    %allColors = [1 0 0; 0 1 0; 0 0 1];
    allColors = [1 0 0];

    % Make rectangle coordinates
    allRects = nan(4, 8);
    for i = 1:numSqaures
        allRects(:, i) = CenterRectOnPointd(baseRect, squareXpos(i), squareYpos(i));
    end

    % Draw the rect to the screen
    Screen('FillRect', window, allColors, allRects);

    if buttons(1) 
        HideCursor();
        %SetMouse(x + r*cos(theta+pi/4), y + r*sin(theta+pi/4), window);
        newX = (x-xCenter)*cos(rotateBy) + (y-yCenter)*sin(rotateBy);
        newY = -(x-xCenter)*sin(rotateBy) + (y-yCenter)*cos(rotateBy);
        Xs = [Xs newX];
        Ys = [Ys newY];
        %Change color when in rectangle. Will work with only one rectangle
        %shown
        if IsInRect(newX, newY, allRects)
            allColors = [0 1 0];
        end


        Screen('DrawDots', window, [xCenter+newX, yCenter+newY], dotSizePix, dotColor, [], 2);        
    end
    if ~buttons(1)
        SetMouse(xCenter, yCenter, window);
        Screen('DrawDots', window, [xCenter, yCenter], dotSizePix, dotColor, [], 2);        
    end
        
    Screen('Flip', window);
    
end
%SetMouse(400, 400, window)
KbStrokeWait;

% Flip to the screen
Screen('Flip', window);
KbStrokeWait;
    
sca;

scatter(Xs, -Ys);