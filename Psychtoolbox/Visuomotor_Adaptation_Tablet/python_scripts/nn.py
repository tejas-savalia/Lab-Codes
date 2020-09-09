# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 12:11:10 2020

@author: Tejas
"""
import torch
import pickle
import numpy as np
from torch import nn

curvatures_smooth = pickle.load(open('curvatures_smooth.pickle', 'rb'))
curvatures_tensor = torch.from_numpy(curvatures_smooth)
#%%
input_seq = curvatures_tensor[0].view(-1)[64:703]
ouput_seq = curvatures_tensor[0].view(-1)[65:704]
#%%
class Model(nn.Module):
    def __init__(self, input_size, output_size):
        super(Model, self).__init__()

        # Defining some parameters
        self.f_to_est = nn.Linear(input_size, output_size)
        self.s_to_est = nn.Linear(input_size, output_size)
        self.est_to_err = nn.Linear(output_size, output_size)
        self.err_to_f = nn.Linear(output_size, input_size)
        self.err_to_s = nn.Linear(output_size, output_size)
        #self.f_to_f = nn.Linear(input_size, input_size)
        #self.s_to_s = nn.Linear(input_size, input_size)
    
    def forward(self, x):
        
        batch_size = x.size(0)

        
        # Passing in the input and hidden state into the model and obtaining outputs
        f_out = self.fc(x, self.f_to_est)
        f_recurr = self.fc(self.f_to_est, self.f_to_est)
        s_out = self.fc(x, self.s_to_est)
        s_recurr = self.fc(self.s_to_est, self.s_to_est)
        
        
        # Reshaping the outputs such that it can be fit into the fully connected layer
        out = out.contiguous().view(-1, self.hidden_dim)
        out = self.fc(out)
        
        return out, hidden
 
    def init_hidden(self, batch_size):
        # This method generates the first hidden state of zeros which we'll use in the forward pass
        # We'll send the tensor holding the hidden state to the device we specified earlier as well
        hidden = torch.zeros(self.n_layers, batch_size, self.hidden_dim)
        return hidden