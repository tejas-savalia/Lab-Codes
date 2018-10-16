% function fit_IEM(p, BOLD_data)

%BOLD_data is [nTrials nVox] matrix in which rows are orients 1-9 stacked on top of each other nPresentations times, stacked nRuns times
    % nTrials is likely 288 (8 runs of 4 presentations of 9 orientations)
subtract_mean_chan = 0; % 0 or 1
Scolari = 1; %if Scolari sim, plot the data differently


m.a = 1; % channel amplitude
m.b = 0; % channel baseline (additive constant)
m.sinPower = 30; % with sinPower above about 8 or 10, the channels are narrow enough to NOT get rank deficient matrix
m.x = linspace(0, pi-pi/(p.nOrients), p.nOrients);
m.cCenters = linspace(0, pi-pi/p.nChans, p.nChans);%  + 0.5*pi/p.nOrients;
C = zeros(p.nOrients*(p.nRuns-2), p.nChans);
% C = zeros(p.nOrients*(p.nRuns-1), p.nChans);
accData = zeros(p.nSubs,p.nChans);
inaccData = zeros(p.nSubs,p.nChans);

% C2_unshifted = zeros(p.nSubs,p.nTrials,p.nChans);
% W_unshifted = zeros(p.nSubs,p.nOrients*p.nRuns/2,p.nVox);

figure(9)
clf(9)
hold on
%make design matrix (with channels - same number as Ho et al.)
for ii=1:p.nChans
    m.u = m.cCenters(ii);
    % HALF SIN WAVE RAISED TO POWER 6
    resp = m.a * sin(mod((m.x-m.u+pi/2),pi)).^m.sinPower + m.b;
%     pred = p.a * exp(-(mod((p.x-p.u+pi/2),pi)-pi/2).^2 / (2*p.sig^2)) + p.b;
    plot([1:9], resp)
    C(:,ii) = repmat(resp', (p.nRuns-2),1);      
%     C(:,ii) = repmat(resp', (p.nRuns-1),1);      
end
title('Channels, C1')

for sub = 1:p.nSubs

    %split data into training and test
%     trn = p.data(sub).voxResp; %[nTrials nVox]
    rCnt=1;
    
    if sub == 1
        meanAcc = mean(mean(p.data(sub).voxResp(p.g==1,:)));
        meanInacc =  mean(mean(p.data(sub).voxResp(p.g==2,:)));
    end
    
    for run = 1:p.nRuns/2 % just go through runs 1 - 4, then hold out run and run+nRuns/2, so that 2 runs held out each time
                            % note this ensures that 1 acc and 1 inacc run are held out, but only if the data are ordered with all runs of one type in first half of runs
        trnSet = ones(size(p.or));
        trnSet(p.runs==run) = 0;
        trnSet(p.runs==run+p.nRuns/2) = 0;

        trn = p.data(sub).voxResp(trnSet == 1,:);     % data from training scans
        tst = p.data(sub).voxResp(trnSet == 0,:);     % data from test scan
        trnor = p.or(trnSet == 1);
        tstor = p.or(trnSet == 0);
        trns = p.runs(trnSet == 1);
        tsts = p.runs(trnSet == 0);  
        trng = p.g(trnSet == 1);
        tstg = p.g(trnSet == 0);

        % first, average over all like orientations in the training set from each run.
        % stack them on top of each other
        uRuns = unique(trns)';
        tmp = zeros(p.nOrients*length(uRuns), size(trn,2));
        sCnt = 1;
        for ss=uRuns
            for ii=1:p.nOrients
                tmp((sCnt-1)*p.nOrients+ii,:) = nanmean(trn(trns==ss & trnor==ii,:));
            end
            sCnt = sCnt+1;
        end
        trnData = tmp;
        tstData = tst;

        % compute voxel-channel weights (do this jointly for speed and accuracy corr/incorr conditions)
        % as estimated based on the training set.
        w = C\trnData;   

        % weights only zigzag when sin power is ~8 or less (and also they give nans for x (C2) in that case )

        % these weights are arbitrary to an additive constant... only the shape of the function matters
        % NOTE: we invert the weights simultaneously for all trials, but it would be the same if each trial done separately
        x = inv(w*w')*w*tstData';
%         x = x - nanmean(x(:));% + nanmean(tst(:));
        chan = x';

        if rCnt==1
            C2 = [];
            task = [];
            overOr = [];
            W = [];
    %         accMean=[];
    %         inaccMean=[];
        end

        % concatenate the channel responses from this run
        C2 = [C2; chan];
        W = [W; w];

        % save the means of each condition
    %     accMean(rCnt) = nanmean(nanmean(tst(tstg==1,:)));
    %     inaccMean(rCnt) = nanmean(nanmean(tst(tstg==2,:)));

        task = [task; tstg];
        overOr = [overOr; tstor];
        
        %predict the test BOLD response (and see how it matches up)
        predictedBOLD = chan*w; %gives a 36 * 100 matrix (nTestTrials * nVox)
        predictedAcc = predictedBOLD(tstg==1,:);
        predictedInacc = predictedBOLD(tstg==2,:);
        fprintf('Subject %d\n', sub);
        mean_predAcc = mean(mean(predictedAcc));
        mean_predInacc = mean(mean(predictedInacc));
        mean_testBOLDAcc = mean(mean(tstData(tstg==1)));
        mean_testBOLDInAcc = mean(mean(tstData(tstg==2)));
        

        rCnt=rCnt+1;
    end

    % circular shift
    % recenter the response matrix (each row centered on the stimulus on that trial)
    for ii=1:size(C2,1)
       C2_centered(ii,:) = wshift('1D', C2(ii,:), overOr(ii)-ceil(p.nOrients/2));
    end

    accVTF=(nanmean(C2_centered(task==1, :)));%;+nanmean(lowMean);
    inaccVTF=(nanmean(C2_centered(task==2, :)));%+nanmean(highMean);

    accData(sub,:) = accVTF;
    inaccData(sub,:) = inaccVTF;
%     
%     C2_unshifted(sub,:,:) = C2;
%     W_unshifted(sub,:,:) = W;

end
% 

figure(10), clf, hold on
title('Full VTFs')
x_axis = (-80:20:90)';
x_axis = repmat(x_axis, 1, 2);
d=[]; sem=[];
if subtract_mean_chan == 0
    d(:,1) = mean(inaccData)';    
    sem(:,1) = (std(inaccData)./sqrt(size(inaccData,1)))';
    
    d(:,2) = mean(accData)';    
    sem(:,2) = (std(accData)./sqrt(size(accData,1)))';
    
elseif subtract_mean_chan ==1  %PLOT CHAN RESPS WITH MEAN SUBTRACTED

    inaccData_mean_subtracted = inaccData - mean(inaccData(:)); 
    d(:,1) = mean(inaccData_mean_subtracted)';  
    sem(:,1) = (std(inaccData_mean_subtracted)./sqrt(size(inaccData_mean_subtracted,1)))';

    accData_mean_subtracted = accData - mean(accData(:));  
    d(:,2) = mean(accData_mean_subtracted)';
    sem(:,2) = (std(accData_mean_subtracted)./sqrt(size(accData_mean_subtracted,1)))';
end
  
% plot(x_axis, d, 'o-', 'LineWidth', 2, 'MarkerSize', 10);
errorbar(x_axis, d, sem, 'o-', 'LineWidth', 2, 'MarkerSize', 10);

set(gca, 'FontSize', 20);
set(gca, 'XLim', [x_axis(1)-5, x_axis(end)+5]);
set(gca, 'XTick', [-80:40:90]);
plot(get(gca, 'XLim'), [0,0], 'k-', 'LineWidth', 2)        
xlabel('Offset from stimulus <deg>')
ylabel('Channel response (a.u.)')
legend({'Inacc Trials', 'Acc Trials'})
legend boxoff

% next do the folded VTFs on each trial type (low contrast, high contrast)
%fold the VTF curve in half like a calzone
x_axis = (0:20:90)';
x_axis = repmat(x_axis, 1, 2);
tmp = (fliplr(accData(:,1:4))+accData(:,6:9))./2;
accDataC = [accData(:,5), tmp];% concatenate the central datapoint (5), with the 'folded' data from 1:4 and 6:9
tmp = (fliplr(inaccData(:,1:4))+ inaccData(:,6:9))./2;
inaccDataC = [inaccData(:,5), tmp];%, highData(:,end)];

figure(11), clf, hold on
title('Collapsed VTFs')
d=[]; sem=[];

if subtract_mean_chan == 0    
    d(:,1) = mean(inaccDataC)';  %lowDataC is the folded data (two halves of the curve collapsed into one)
    sem(:,1) = (std(inaccDataC)./sqrt(size(inaccDataC,1)))';
   
    d(:,2) = mean(accDataC)';    
    sem(:,2) = (std(accDataC)./sqrt(size(accDataC,1)))';
elseif subtract_mean_chan ==1  %PLOT CHAN RESPS WITH MEAN SUBTRACTED
    d(:,1) = mean(inaccDataC)' - mean(inaccDataC(:));  
    sem(:,1) = (std(inaccDataC)./sqrt(size(inaccDataC,1)))';
    
    d(:,2) = mean(accDataC)' - mean(accDataC(:));
    sem(:,2) = (std(accDataC)./sqrt(size(accDataC,1)))';    
end
      
errorbar(x_axis, d, sem, 'o-', 'LineWidth', 2, 'MarkerSize', 10);

set(gca, 'FontSize', 20);
set(gca, 'XLim', [x_axis(1)-5, x_axis(end)+5]);
set(gca, 'XTick', [0:40:90]);
%         set(gca, 'YLim', [-.25, 1.5])
%         set(gca, 'YTick', [-.25:.25:1.5]);
plot(get(gca, 'XLim'), [0,0], 'k-', 'LineWidth', 2)        
xlabel('Offset from stimulus abs(<deg>)')
ylabel('Channel response (a.u.)')
legend({'Inacc Trials', 'Acc Trials'})
legend boxoff         


figure(12)
clf(12)
plot([1:9], w(:,1))
hold on
plot([1:9], w(:,4), 'r')
plot([1:9], w(:,10), 'k')
plot([1:9], w(:,16), 'c')
plot([1:9], w(:,26), 'm')
plot([1:9], w(:,57), 'g')
plot([1:9], w(:,91), 'b')
plot([1:9], w(:,85), '-o')
title('Sample of Voxel Weights')

% attempt to replicate Liu et al. ? 
% (adding different levels of noise, and using different channel and NTF widths)