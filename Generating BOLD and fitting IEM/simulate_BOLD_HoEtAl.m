% function simulate_BOLD(voxNoiseRatio, NTFbaseline, NTFamp, NTFsig)

% incorrect is just a regular set of neural resps; correct --> take the off-channel neurons and give them gain (for every stim)

% NTFsig of 0.35 with notchwidth of 8 and gainFactor of 4 gives almost hte right shape (if you subtract the mean chan resp)

% default parameters (that will be manipulated)
voxNoiseScale = .5;
NTFbaseline = 0;
p.NTFamp = 1;
p.NTFsig = .35 
% GainFactor = [1.5 2]; % medium and high factors by which NTFs are multiplied for 'correct' trials (in off-channels)
% parameters of simulation (not usually changed)
normedNTF = 1;
p.notchwidth = 8; %must be an even number. governs width of off-channel 'notch' that undergoes gain. higher is narrower.
p.gainFactor = 4; %must be  <1 if using method 2 (slope of NTF) but >1 if using method 1 (sin wave function) see splice_NTFresponses function
p.nVox = 100;
p.nNTFs = 180;
p.stimOrient = [0 20 40 60 80 100 120 140 160];% 200  240 280 320 360]'; % or add in that each is shown plus or minus 5 deg?
p.nOrients = length(p.stimOrient);
p.nRuns = 8;
p.nPresentations = 4;
% p.nTrialsPerOrient = p.nRuns*p.nPresentations; % 4 per run and 8 runs, as per Ho et al. 2012
p.nTrials = p.nOrients*p.nPresentations*p.nRuns;
p.nSubs = 100;
x = linspace(0, pi-pi/(p.nOrients), p.nOrients);
% NTFcenters = [1:180]';
p.NTFcenters = linspace(0, pi-pi/p.nNTFs, p.nNTFs);

for sub = 1:p.nSubs
    voxelWeights = rand(p.nNTFs,p.nVox); % sampled as in Liu et al. (uniform dist)
    for vox = 1:p.nVox
        voxelWeights(:,vox) = voxelWeights(:,vox)/sum(voxelWeights(:,vox)); %normalized so each voxel's weights sum to 1
    end

    NTFresponses_Baseline = zeros(p.nOrients,p.nNTFs); % baseline resp of every NTF to every stim 
    NTFresponses_Gain = zeros(p.nOrients,p.nNTFs); % 'gained' resp of every NTF to every stim
    voxelResponses = zeros(p.nOrients*p.nPresentations, p.nVox, p.nRuns); % resp of every vox to every stim on every run
    p.nChans = 9;

    if sub==1
        figure(1)
        clf(1)
        hold on
    end
    % calculate NTF responses
    for NTF = 1:p.nNTFs
        if normedNTF ==1 % normalize area under the NTF
            NTFresponses_Baseline(:,NTF) = (1/sqrt(2*pi*(NTFsig)^2)) * p.NTFamp * exp(-(mod((x-p.NTFcenters(NTF)+pi/2),pi)-pi/2).^2 / (2*p.NTFsig^2)) + NTFbaseline;
            if sub==1 && mod(NTF,20)==1, plot([1:9], NTFresponses_Baseline(:,NTF)); end
        elseif normedNTF==0 % do not normalize
            NTFresponses_Baseline(:,NTF) = p.NTFamp * exp(-(mod((x-p.NTFcenters(NTF)+pi/2),pi)-pi/2).^2 / (2*p.NTFsig^2)) + NTFbaseline;
            if sub == 1 && mod(NTF,20)==1, plot([1:9], NTFresponses_Baseline(:,NTF)); end
        end
    end
    
    if sub == 1
        title('NTFresponses Baseline') 

        figure(2)
        clf(2)
        imagesc(NTFresponses_Baseline);
        colorbar;
        title('NTFresponses Baseline');


        fig_num = 3;
        clf(fig_num)
        figure(fig_num)
        plot([1:180],NTFresponses_Baseline(3,:))
        title('Orient #3 Responses across all NTFs');
    end

    or = zeros(p.nOrients*p.nPresentations,1); %,p.nRuns); % [ 9*4 ] , [8]
    stimPres = zeros(p.nOrients*p.nPresentations,1); %,p.nRuns);
    g = zeros(p.nOrients*p.nPresentations,p.nRuns);
    %% calculate voxel responses
    % voxelResponses = zeros(p.nVox, p.nOrients*p.nPresentations, p.nRuns);
    Cnt=1;
    for scan = 1:p.nRuns 
        for pres = 1:p.nPresentations % 4 presentations in each of 8 runs, from Ho et al.
            if scan <= p.nRuns/2
                NTFresponses = splice_NTFresponses(NTFresponses_Baseline, p,sub, Cnt);
                g(:,scan) = 1; % "accurate" trials
            elseif scan > p.nRuns/2
                NTFresponses = NTFresponses_Baseline;
                g(:,scan) = 2; % "inaccurate" trials
            end
            rows = (pres-1)*p.nOrients+1:(pres-1)*p.nOrients+p.nOrients;
            voxelResponses(rows,:,scan) = NTFresponses*voxelWeights; % [ p.nOrients p.nNTFs ]*[ p.nNTFs p.nVox ]
            % gives a [nOrients*nPresentations nVox nRuns] matrix with response of every voxel to every stim
            if scan==1
                or(rows) = [1:9]';
                stimPres(rows) = pres*ones(9,1);
            end   
            Cnt=Cnt+1;
        end
    end
    
    p.or = repmat(or,[p.nRuns 1]); % nTrials long, giving orientation of stim
    p.stimPres = repmat(stimPres,[p.nRuns 1]); % nTrials long, giving presentation # within run
    runs = repmat([1:p.nRuns],[p.nOrients*p.nPresentations 1]);
    p.runs = reshape(runs, [size(runs,1)*size(runs,2) 1]);
    p.g = reshape(g, [size(g,1)*size(g,2) 1]); %reshape to state acc versus inacc in a vector of length nTrials
    voxResp=[];
    for rr = 1:p.nRuns
        voxResp = cat(1, voxResp, voxelResponses(:,:,rr));
    end

    voxelNoiseSD = mean(mean(voxResp,1))*voxNoiseScale; %take mean across all trials for each voxel
    p.data(sub).voxelNoiseSD = voxelNoiseSD;
    % we will assume same SD of noise for each voxel, which we will scale by their mean activation across all stimuli
    % then sample from this noise distributions separately for each voxel, stim orient and presentation

    % Liu et al. specified sigma of Gaussian noise using mean of all voxels' responses per stimulus (see generateBOLDResp)
    % assuming same SD of noise for all voxels for a given stim orient, and then (I think) the actual noise on a given trial was sampled separately
    % they probably didn't intend there to be big differences in noise SD between stimuli, but did it this way for convenience (because of structure of
    % code)

    p.data(sub).voxResp = voxResp + normrnd(0,voxelNoiseSD, [p.nTrials, p.nVox]);
    
end

%% plot voxel BOLD responses for last subject
voxResp_perOrient = zeros(p.nOrients,p.nVox);
for orient = 1:p.nOrients
    voxResp_perOrient(orient,:) = mean(voxResp(p.or==orient,:),1);
end

fig_num = 6;
figure(fig_num)
clf(fig_num)
plot([1:p.nOrients],voxResp_perOrient(:,1))
ylim([min(min(min(voxResp_perOrient))) max(max(max(voxResp_perOrient)))])
hold on
plot([1:p.nOrients],voxResp_perOrient(:,21))
plot([1:p.nOrients],voxResp_perOrient(:,34))
plot([1:p.nOrients],voxResp_perOrient(:,41))
plot([1:p.nOrients],voxResp_perOrient(:,53))
plot([1:p.nOrients],voxResp_perOrient(:,61))
plot([1:p.nOrients],voxResp_perOrient(:,81))
plot([1:p.nOrients],voxResp_perOrient(:,95))
title('Voxel BOLD responses')


%END OF parent function


%% splice NTF responses function
function [NTFresp] = splice_NTFresponses(NTFresp_Base, p, sub, Cnt)
       
    %NTFresp is [9 x 180] representing 9 orientations and 180 NTFs     
    NTFresp = zeros(p.nOrients,p.nNTFs);
    
    s.x = linspace(0, pi-pi/(p.nOrients), p.nOrients);
    s.nCenters = linspace(0, pi-pi/(p.nNTFs), p.nNTFs);
    
    for orient = 1:p.nOrients
        if p.nOrients == 9
            % recall that p.stimOrient = [0 20 40 60 80 100 120 140 160];
            stim = s.x(orient);
            
            %Method #1
            %construct sine wave sq profile with low points at stim orient and 90deg from stim orient (peaks in between)
            % note, baseline here is 1 so that all NTFs have at least a gain of 1, some greater than 1
            gainDist = p.gainFactor * sin(2*(stim - s.nCenters)).^p.notchwidth + 1;
           
            %Method #2
%             gainDist = abs( p.gainFactor * -((mod((stim-p.NTFcenters+pi/2),pi)-pi/2)/p.NTFsig^2) .* exp(-(mod((stim-p.NTFcenters+pi/2),pi)-pi/2).^2 / (2*p.NTFsig^2)) ) + 1;
            
            %this will be used to specify gain for each NTF in the voxel
            NTFresp(orient,:) = NTFresp_Base(orient,:).*gainDist;
            
        else
            error('need to rewrite code to deal with nOrients not equal to 9!')
        end  
    end

    if sub == 1 && Cnt == 1
        fig_num = 4;
        figure(fig_num)
        clf(fig_num)
        plot([1:p.nOrients],NTFresp(:,1))
        ylim([min(min(min(NTFresp))) max(max(max(NTFresp)))])
        hold on
        plot([1:p.nOrients],NTFresp(:,21))
        plot([1:p.nOrients],NTFresp(:,41))
        plot([1:p.nOrients],NTFresp(:,61))
        plot([1:p.nOrients],NTFresp(:,81))
        plot([1:p.nOrients],NTFresp(:,101))
        plot([1:p.nOrients],NTFresp(:,121))    
        plot([1:p.nOrients],NTFresp(:,141))
        plot([1:p.nOrients],NTFresp(:,161))
        title('NTF responses')

        fig_num=5;
        figure(fig_num)
        clf(fig_num)
        imagesc(NTFresp);
        colorbar;
        title('Off-Chan Gained NTFs');

        fig_num = 3;
        figure(fig_num)
        hold on 
        plot([1:180],NTFresp(3,:))
        legend({'NTF Baseline', 'NTF Off-Chan Gain'})
        legend boxoff
        
    end
end

