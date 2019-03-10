

%for i = 1:10
%[x, y] = trial_traj(participant, i);
%fname = sprintf('python_scripts\\data\\pilot\\pilot_1\\actual_trajectories\\trajectories%d',i);
%save(fname, 'x', 'y');
%end

for i = 1:1
load('C:\Users\Tejas\Documents\Research\Lab-Codes\Psychtoolbox\Visuomotor Adaptation\Data\Pilot\Pilot_1\pilot_1.mat');
[idealXs, idealYs] = ideal_trajectories(participant, 1, i);
fname = sprintf('python_scripts\\data\\pilot\\pilot_1\\ideal_trajectories\\ideal_trajectories11');
save(fname, 'idealXs', 'idealYs');
end