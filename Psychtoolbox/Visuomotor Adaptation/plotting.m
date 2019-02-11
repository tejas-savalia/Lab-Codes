last = length(participant(1).ae.block.trial(64).xTrajectory);
cut_off = length(participant(1).ae.block.trial(54).xTrajectory);
last_sixten = cut_off - last;
scatter(participant(1).ae.block.trial(64).xTrajectory(last:-1:cut_off), participant(1).ae.block.trial(64).yTrajectory(last:-1:cut_off)); 
hold on;
scatter(participant(1).ae.block.trial(10).xTrajectory, participant(1).ae.block.trial(10).yTrajectory); 
