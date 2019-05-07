%pno = 1;
%pno = 1;
%{
for pno = 28:58
    fmake = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories',pno); 
    mkdir(fmake);
    fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\python_scripts\\data\\participants\\data%d\\master\\data%d.mat', pno, pno);
    load(fload);

    for i = 1:1
        [x, y] = trial_traj(participant, pno, i);
        fname = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories\\trajectories0', pno);    
        save(fname, 'x', 'y');
    end
end
%}
%{
for pno = 1:6
    %fmake = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories',pno); 
    %mkdir(fmake);
    fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\python_scripts\\data\\participants\\data%d\\master\\data%d.mat', pno, pno);
    load(fload);

    for i = 1:1
        [x, y] = trial_traj(participant, pno, i);
        fname = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories\\trajectories0', pno);    
        save(fname, 'x', 'y');
    end
end
%}
%{
for pno = 28:58
    fmake = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories',pno); 
    mkdir(fmake);
    fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\python_scripts\\data\\participants\\data%d\\master\\data%d.mat', pno, pno);
    load(fload);

    for i = 1:10
        [x, y] = trial_traj(participant, pno, i);
        fname = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories\\trajectories%d', pno, i);    
        save(fname, 'x', 'y');
    end
end
%}


%pno = 1;

for pno = 28:58
    fmake = sprintf('python_scripts\\data\\participants\\data%d\\ideal_trajectories',pno); 
    mkdir(fmake);
    fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\python_scripts\\data\\participants\\data%d\\master\\data%d.mat', pno, pno);
    load(fload);
    for i = 1:1
        [idealXs, idealYs] = ideal_trajectories(participant, pno, i);
        fname = sprintf('python_scripts\\data\\participants\\data%d\\ideal_trajectories\\ideal_trajectories0', pno);    
        save(fname, 'idealXs', 'idealYs');
    end
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