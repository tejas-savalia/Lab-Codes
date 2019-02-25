mt = zeros(10, 64);
for block = 1:10
    for i = 1:64
    mt(block, i) = participant(1).practice.block(block).trial(i).movementTime;
    end
end
rmse = zeros(10, 64);
for block = 1:10
    rmse(block, :) = RMSEfromtrial(participant, block);
end
for block = 1:10
    scatter(mt(block, :), rmse(block, :))
    hold on;
end

