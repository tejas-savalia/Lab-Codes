function [rmse] = RMSE(xTrajectory, yTrajectory, xCenterPos, yCenterPos, xTargetPos, yTargetPos)

samples = length(xTrajectory);
idealXs = linspace(xCenterPos, xTargetPos, samples);
idealYs = linspace(yCenterPos, yTargetPos, samples);

rmse = sqrt(sum((xTrajectory - idealXs)^2 + (yTrajectory - idealYs)^2)/samples);

end
