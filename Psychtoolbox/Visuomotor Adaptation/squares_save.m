pno = 1;
fload = sprintf('C:\\Users\\Tejas\\Documents\\Research\\Lab-Codes\\Psychtoolbox\\Visuomotor Adaptation\\Data\\Pilot\\Pilot_%d\\pilot_%d.mat', pno, pno);
load(fload);
squares = zeros(64, 1);
xCenter = 960;
yCenter = 540;
for i = 1:10
    squares = participant(pno).practice.block(i).squares;  
    squareX = 300*cos(squares);
    squareY = 300*sin(squares);
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\squares\\angles\\squares%d', pno, i);
    save(fname, 'squares');
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\squares\\coordinates\\squares%d', pno, i);
    save(fname, 'squareX', 'squareY');
end

for i = 1:1
    squares = participant(pno).ib.block(i).squares;          
    squareX = 300*cos(squares);
    squareY = 300*sin(squares);
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\squares\\angles\\squares0', pno);
    save(fname, 'squares');
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\squares\\coordinates\\squares0', pno);
    save(fname, 'squareX', 'squareY');

end
for i = 1:1
    squares = participant(pno).ae.block(i).squares;  
    squareX = 300*cos(squares);
    squareY = 300*sin(squares);
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\squares\\angles\\squares11', pno);
    save(fname, 'squares');
    fname = sprintf('python_scripts\\data\\pilot\\pilot_%d\\squares\\coordinates\\squares11', pno);
    save(fname, 'squareX', 'squareY');

end


    %randomSquareTheta = participant(pno).practice.block(block).squares(i)   ;
    %randomSquareXpos = 300*cos(randomSquareTheta) + xCenter;
    %randomSquareYpos = 300*sin(randomSquareTheta) + yCenter;

