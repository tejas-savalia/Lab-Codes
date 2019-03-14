%for i = 1:10
%[x, y] = trial_traj(participant, i);
%fname = sprintf('python_scripts\\data\\pilot\\pilot_1\\actual_trajectories\\trajectories%d',i);
%save(fname, 'x', 'y');
%end
pno = 3;

for i = 1:10
fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\Data\\Pilot\\Pilot_%d\\pilot_%d.mat', pno, pno);
load(fload);
[idealXs, idealYs] = ideal_trajectories(participant, pno, i);
fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\ideal_trajectories\\ideal_trajectories%d', pno, i);
save(fname, 'idealXs', 'idealYs');
end
%}
% zeroth
%{
for i = 1:1
fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\Data\\Pilot\\Pilot_%d\\pilot_%d.mat', pno, pno);
load(fload);
[idealXs, idealYs] = ideal_trajectories(participant, pno, i);
fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\ideal_trajectories\\ideal_trajectories0', pno);
save(fname, 'idealXs', 'idealYs');
end
%}
%Eleventh
%{
for i = 1:1
fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\Data\\Pilot\\Pilot_%d\\pilot_%d.mat', pno, pno);
load(fload);
[idealXs, idealYs] = ideal_trajectories(participant, pno, i);
fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\ideal_trajectories\\ideal_trajectories11', pno);
save(fname, 'idealXs', 'idealYs');
end
%}