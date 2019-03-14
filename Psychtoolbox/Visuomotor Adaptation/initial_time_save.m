pno = 1;
fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\Data\\Pilot\\Pilot_%d\\pilot_%d.mat', pno, pno);
load(fload);
initial_time = zeros(64, 1);
for i = 1:10
    for j = 1:64
        initial_time(j, 1) = participant(pno).practice.block(i).trial(j).initial_time;  
    end
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\initial_time\\initial_time%d', pno, i);
    save(fname, 'initial_time');

end
for i = 1:1
    for j = 1:64
        initial_time(j, 1) = participant(pno).ib.block(i).trial(j).initial_time;  
    end
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\\\initial_time\\initial_time0', pno);
    save(fname, 'initial_time');
end
for i = 1:1
    for j = 1:64
        initial_time(j, 1) = participant(pno).ae.block(i).trial(j).initial_time;  
    end
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\\\initial_time\\initial_time11', pno);
    save(fname, 'initial_time');
end
