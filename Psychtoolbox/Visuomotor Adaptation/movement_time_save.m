pno = 7;
for pno = 28:58
    fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\python_scripts\\data\\participants\\data%d\\master\\data%d.mat', pno, pno);
    fmake = sprintf('python_scripts\\data\\participants\\data%d\\movement_time',pno); 
    mkdir(fmake);
    load(fload);
    movement_time = zeros(64, 1);
    for i = 1:10
        for j = 1:64
            movement_time(j, 1) = participant(pno).practice.block(i).trial(j).movementTime;  
        end
        fname = sprintf('python_scripts\\data\\participants\\data%d\\movement_time\\movement_time%d', pno, i);
        save(fname, 'movement_time');

    end
    for i = 1:1
        for j = 1:64
            movement_time(j, 1) = participant(pno).ib.block(i).trial(j).movementTime;  
        end
        fname = sprintf('python_scripts\\data\\participants\\data%d\\movement_time\\movement_time0', pno);
        save(fname, 'movement_time');
    end
    for i = 1:1
        for j = 1:64
            movement_time(j, 1) = participant(pno).ae.block(i).trial(j).movementTime;  
        end
        fname = sprintf('python_scripts\\data\\participants\\data%d\\\\movement_time\\movement_time11', pno);
        save(fname, 'movement_time');
    end
end