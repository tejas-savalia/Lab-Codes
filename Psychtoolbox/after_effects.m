
%sca;
%close all;
%clearvars;

PsychDefaultSetup(2);

screens = Screen('Screens');
%screenNumber = max(screens);
screenNumber = 1;

white = WhiteIndex(screenNumber);
black = BlackIndex(screenNumber);
grey = white/2;

[window, windowRect] = PsychImaging('OpenWindow', screenNumber, grey);
[screenXpixels, screenYpixels] = Screen('WindowSize', window);
[xCenter, yCenter] = RectCenter(windowRect);

%ifi = Screen('GetFlipInterval', window);
%numSecs = 10;
%numFrames = round(numSecs/ifi);
%vb1 = Screen('Flip', window);
SetMouse(xCenter, yCenter, window);

dotColor = [1, 0, 0];
dotSizePix = 20;
HideCursor();
rotateBy = 0;
Screen('DrawDots', window, [xCenter, yCenter], dotSizePix, dotColor, [], 2);
Screen('Flip', window);    
Xs = {};
Ys = {};

baseRect = [0 0 100 100];
numRects = 4;

%Screen('Flip', window);

numBlocks = 1;
numTrials = numRects*1;



totalScore = 0;
times = zeros(numBlocks, numTrials);
initial_time = zeros(numBlocks, numTrials);
for block = 1:numBlocks
    
    squareTheta = repelem([pi/4, 3*pi/4, 5*pi/4, 7*pi/4], numTrials/4);
    i = randperm(length(squareTheta));
    randomSquareThetaVec = squareTheta(:, i);

    %Code for inter block interval
    newXs = [];
    newYs = [];
    blockScore = 0;

    Screen('FillRect', window, [0.5, 0.5, 0.5]);        
    Screen('TextSize', window, 30);
    DrawFormattedText(window, 'Ready?', xCenter - 100, yCenter, [1 0 0]);
    DrawFormattedText(window, 'Press any key to Continue', xCenter-350, yCenter + 100, [1 0 0]);
    Screen('Flip', window);
    KbStrokeWait;
    
    for trial = 1:numTrials
        randomSquareTheta = randomSquareThetaVec(trial);
        randomSquareXpos = 300*cos(randomSquareTheta) + xCenter;
        randomSquareYpos = 300*sin(randomSquareTheta) + yCenter;

        randomSquareColor = [1, 0, 0];
        randomSquare = CenterRectOnPointd(baseRect, randomSquareXpos, randomSquareYpos);

        %Code for inter-trial-interval
        %Auditary cue. 
        %Screen('FillRect', window, randomSquareColor, randomSquare);
        Screen('TextSize', window, 30);
        Screen('FillRect', window, [0, 0.5, 0.5])
        %DrawFormattedText(window, num2str(blockScore), screenXpixels*0.80 ,screenYpixels * 0.15, [1 0 0]);
        Screen('DrawDots', window, [xCenter, yCenter], dotSizePix, dotColor, [], 2);        
        Screen('Flip', window);    
       
        GetClicks();
        rand_interval = 0.2 + rand(1, 1)*(2 - 0.2);
        pause(rand_interval);
        
        
        tic;
        first_flag = true;
        while true
        
            Screen('FillRect', window, [0, 0.5, 0.5]);
            
            [x, y, buttons] = GetMouse(window);
            %theta = atan(y-yCenter/x-xCenter);
            %r = (x-xCenter)/cos(theta);
            %theta = acos((x - xCenter)/r);

            % Draw the rect to the screen
            %Screen('FillRect', window, allColors, allRects);
            Screen('FillRect', window, randomSquareColor, randomSquare);
            Screen('TextSize', window, 30);
            %DrawFormattedText(window, num2str(blockScore), screenXpixels*0.80 ,screenYpixels * 0.15, [1 0 0]);



            if buttons(1)
                if first_flag
                    initial_time(block, trial) = toc;
                    first_flag = false;
                end
                HideCursor();
                %SetMouse(x + r*cos(theta+pi/4), y + r*sin(theta+pi/4), window);
                newX = (x-xCenter)*cos(rotateBy) + (y-yCenter)*sin(rotateBy);
                newY = -(x-xCenter)*sin(rotateBy) + (y-yCenter)*cos(rotateBy);
                newXs = [newXs newX];
                newYs = [newYs newY];
                
                inside = IsInRect(newX+xCenter, newY+yCenter, randomSquare);
                
                if inside
                    %printf('here');
                    %randomSquareTheta = randomSquareThetaVec(trial+1);
                    %randomSquareXpos = 300*cos(randomSquareTheta) + xCenter;
                    %randomSquareYpos = 300*sin(randomSquareTheta) + yCenter;

                    %randomSquareColor = [1, 0, 0];
                    %randomSquare = CenterRectOnPointd(baseRect, randomSquareXpos, randomSquareYpos);


                    blockScore = blockScore + 1;
                    times(block, trial) = toc; 
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
        
        Screen('Flip', window);
        Xs{block} = newXs;
        Ys{block} = newYs;
        %display score
    end
    %display leaderboard.
   
    
    Screen('FillRect', window, [0.5, 0.5, 0.5]);        
    totalScore = totalScore + blockScore;
    Screen('TextSize', window, 30);
    %DrawFormattedText(window, num2str(totalScore), xCenter, yCenter, [1 0 0]);
    DrawFormattedText(window, 'Chill Out. Press any key to Continue', xCenter-450, yCenter, [1 0 0]);
    
    Screen('Flip', window);
    KbStrokeWait;
    
 end
%SetMouse(400, 400, window)
KbStrokeWait;

% Flip to the screen
Screen('Flip', window);
KbStrokeWait;
    
sca;

% Convert cell to a table and use first row as variable names
TX = cell2table(Xs);
TY = cell2table(Ys); 
% Write the table to a CSV file
writetable(TX,'afterEffectsX.csv');
writetable(TY,'afterEffectsY.csv');

%scatter(Xs{1}, -Ys{1});