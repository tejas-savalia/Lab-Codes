%Change the following:
%For practice blocks:
%   i = 1:10, in trial_traj.m "practice", fname line: "...trajectories%d",
%   pno, i), 

for pno = 1618
    fmake = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories',pno); 
    mkdir(fmake);
    fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\python_scripts\\data\\participants\\data%d\\master\\data%d.mat', pno, pno);
    load(fload);

    for i = 1:1
        [x, y] = trial_traj(participant, pno, i);
        fname = sprintf('python_scripts\\data\\participants\\data%d\\actual_trajectories\\trajectories11', pno);    
        save(fname, 'x', 'y');
    end
end




for pno = 1618
    fmake = sprintf('python_scripts\\data\\participants\\data%d\\ideal_trajectories',pno); 
    mkdir(fmake);
    fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\python_scripts\\data\\participants\\data%d\\master\\data%d.mat', pno, pno);
    load(fload);
    for i = 1:1
        [idealXs, idealYs] = ideal_trajectories(participant, pno, i);
        fname = sprintf('python_scripts\\data\\participants\\data%d\\ideal_trajectories\\ideal_trajectories11', pno);    
        save(fname, 'idealXs', 'idealYs');
    end
end
