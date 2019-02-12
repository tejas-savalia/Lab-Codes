clearvars;
%Sudden_change = 0. Gradual change = 1.
%Speed = 0.         Accuracy = 1.
global participant_number; 
participant_number = input('Participant Number?');
participant(participant_number).change = 1;
participant(participant_number).emphasis = 0;
participant(participant_number).pNo = participant_number;
start;
initial_block;
practice;
after_effects;