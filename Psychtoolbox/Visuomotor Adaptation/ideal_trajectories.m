function [idealXs, idealYs] = ideal_trajectories(participant, pno, block)
xCenter = 960;
yCenter = 540;
[x, y] = trial_traj(participant, pno, block);

for i = 1:64
    randomSquareTheta = participant(pno).practice.block(block).squares(i)   ;
    randomSquareXpos = 300*cos(randomSquareTheta) + xCenter;
    randomSquareYpos = 300*sin(randomSquareTheta) + yCenter;
    samples = length(x{i});
    xratios = x{i}(1:samples)/sum(x{i}(1:samples));
    xratios = cumsum(xratios);
    yratios = y{i}(1:samples)/sum(y{i}(1:samples));
    yratios = cumsum(yratios);
    %ideal trajectory point spacings proportional to actual trajectory
    %point spacings. 
    idealXs{i} = (randomSquareXpos - xCenter)*xratios;
    idealYs{i} = (randomSquareYpos - yCenter)*yratios;
end
end