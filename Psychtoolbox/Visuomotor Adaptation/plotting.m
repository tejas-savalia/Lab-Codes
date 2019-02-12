last = length(participant(1).ae.block.trial(64).xTrajectory);
cut_off = length(participant(1).ae.block.trial(54).xTrajectory);
last_few = cut_off - last;
scatter(participant(1).practice.block(5).trial(64).xTrajectory, participant(1).practice.block(5).trial(64).yTrajectory); 
%hold on;
%scatter(participant(1).ae.block.trial(10).xTrajectory, participant(1).ae.block.trial(10).yTrajectory); 
