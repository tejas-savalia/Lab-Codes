%Trial Structure. Done.
%Inter trial and inter block interval code.
%Only one square at a time. Done
%90 degree rotation.
%Two cases: Gradual and Sudden
%RMSE, IDE and MT
%After effects stage
%Auditory cue
%Color change on hit. Changed random squares on hit. Done.
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

baseRect = [0 0 100 100];
numRects = 8;

squareTheta = [0, pi/4, pi/2, 3*pi/4, pi, 5*pi/4, 3*pi/2, 7*pi/4];

randomSquarePos = randi(length(squareTheta));
randomSquareTheta = squareTheta(randomSquarePos);
randomSquareXpos = 300*cos(randomSquareTheta) + xCenter;
randomSquareYpos = 300*sin(randomSquareTheta) + yCenter;

randomSquareColor = [1, 0, 0];
randomSquare = CenterRectOnPointd(baseRect, randomSquareXpos, randomSquareYpos);

%Screen('Flip', window);

numBlocks = 1;
numTrials = 2;

for block = 1:numBlocks
    %Code for inter block interval
    for trial = 1:numTrials
        %Code for inter-trial-interval
        for frame = 1:numFrames
        
            Screen('FillRect', window, [0, 0.5, 0.5]);
            [x, y, buttons] = GetMouse(window);
            theta = atan(y-yCenter/x-xCenter);
            r = (x-xCenter)/cos(theta);
            %theta = acos((x - xCenter)/r);

            % Draw the rect to the screen
            %Screen('FillRect', window, allColors, allRects);
            Screen('FillRect', window, randomSquareColor, randomSquare);



            if buttons(1) 
                HideCursor();
                %SetMouse(x + r*cos(theta+pi/4), y + r*sin(theta+pi/4), window);
                newX = (x-xCenter)*cos(rotateBy) + (y-yCenter)*sin(rotateBy);
                newY = -(x-xCenter)*sin(rotateBy) + (y-yCenter)*cos(rotateBy);
                Xs = [Xs newX];
                Ys = [Ys newY];
                %Change color when in rectangle. Will work with only one rectangle
                %shown
                inside = IsInRect(newX+xCenter, newY+yCenter, randomSquare);
                if inside
                    %printf('here');
                    randomSquarePos = randi(length(squareTheta));
                    randomSquareTheta = squareTheta(randomSquarePos);
                    randomSquareXpos = 300*cos(randomSquareTheta) + xCenter;
                    randomSquareYpos = 300*sin(randomSquareTheta) + yCenter;

                    randomSquareColor = [1, 0, 0];
                    randomSquare = CenterRectOnPointd(baseRect, randomSquareXpos, randomSquareYpos);
                    break;
                end


                Screen('DrawDots', window, [xCenter+newX, yCenter+newY], dotSizePix, dotColor, [], 2);        
            end
            if ~buttons(1)
                SetMouse(xCenter, yCenter, window);
                Screen('DrawDots', window, [xCenter, yCenter], dotSizePix, dotColor, [], 2);        
            end

            Screen('Flip', window);
        end
    end
 end
%SetMouse(400, 400, window)
KbStrokeWait;

% Flip to the screen
Screen('Flip', window);
KbStrokeWait;
    
sca;

scatter(Xs, -Ys);