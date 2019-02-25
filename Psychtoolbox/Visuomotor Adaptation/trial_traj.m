%Function to obtain trial trajectories from xTrajectory and yTrajectory
%variables
function[xtrial_traj, ytrial_traj] = trial_traj(participant)
xtrial_traj{1} = participant(1).ib.block.trial(1).xTrajectory;
ytrial_traj{1} = participant(1).ib.block.trial(1).yTrajectory;

for i = 1:63
    last_cutoff = length(participant(1).ib.block.trial(i+1).xTrajectory);
    first_cutoff = length(participant(1).ib.block.trial(i).xTrajectory);
    xtrial_traj{i+1} = participant(1).ib.block.trial(64).xTrajectory(1+first_cutoff:last_cutoff);
    ytrial_traj{i+1} = participant(1).ib.block.trial(64).yTrajectory(1+first_cutoff:last_cutoff);
    
end
end

%Calculate xCenter yCenter from the screeen first
