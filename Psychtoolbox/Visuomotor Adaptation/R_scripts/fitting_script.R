source('wald.R')
source('TruncNorm.R')

nsim = 12 
N = 64 #Number of Trials
nparticipants = 58

#True parameters
#Boundary height from a truncated normal
a = rtnorm(nsim, mu=0.15, sig = 0.05, lo = 0.05, hi = 0.30) 
#Drift rate from a truncated normal
v = rtnorm(nsim, mu = 0.3, sig = 0.1, lo = 0.1, hi = 0.5)

q_wald = c()
#Expected frequencies
f = c(0.1, 0.2, 0.2, 0.2, 0.2, 0.1)*N

#Fit parameters to save


cnt = 0
upfreq = 50


################################################################################

cons=function(cpar){
  penf=0
  pmn=.01
  if(cpar[1]<pmn){
    penf=penf+(pmn-cpar[1]) 
    cpar[1]=pmn
  }
  pmn=.01
  if(cpar[2]<pmn){
    penf=penf+(pmn-cpar[2]) 
    cpar[2]=pmn
  }
  pmn=.00015
  if(cpar[3]<pmn){
    penf=penf+(pmn-cpar[3]) 
    cpar[3]=pmn
  }
  ls=list(cpar,penf)
  return(ls)
}



waldPred <- function(par){
  
  #Parameters
  a = par[1]
  v = par[2]
  ter = par[3]
  q = quantile(data[[1]] - ter)
  #Cuts for quantiles
  cuts = c(0, q, Inf)
  p = c()
  
  for (i in (1:(length(cuts)-1))){
    p[i] = pwald(cuts[i+1], a, v) - pwald(cuts[i], a, v)
  }
  return(p)
}

gsqfun_wald <- function(par, freq){
  
  ls = cons(par)
  cpar = ls[[1]]
  pen = ls[[2]]
  p = waldPred(cpar)
  p = p/sum(p)
  #print (p)
  
  pf = p*sum(freq)
  pf
  
  gslev=1:length(freq)
  gslev=gslev[freq>0]
  
  gsq=2*sum(freq[gslev]*log(freq[gslev]/pf[gslev]))
  gsq = gsq + pen*gsq
  return (gsq)
}

wald_fit = function(f){
  par = c(0.1, 0.001, 0)
  comp = gsqfun_wald(par, f)
  
  while(TRUE){
    fit=optim(par,gsqfun_wald,freq=f)
    par=fit$par
    if((comp-fit$value)<=.001) break
    comp=fit$value
  }
  wald_par = par
  gsq = gsqfun_wald(par, f)
  
  ls = list(wald_par, gsq)
  return (ls)
}

######################################################################################################

#Running them loops

library(R.matlab)
f_a = c()
f_v = c()
f_ter = rep(0, nsim)
f_wald_gsq = rep(Inf, nsim)

si= 1
cnt = 0
upfreq = 50
a = 'data/participants/data'
c = '/initial_time/initial_time'
e = '.mat'
g = '/initial_time_wald_fits'
h = '/fits.csv'
for(participant in 1:nparticipants){
  path = paste(a, b, g, sep="")
  dir.create(path)
  
  if (participant == 7){
    next
  }
  for(si in 1:nsim){
    
    
    #runs the sim function above
    #q_wald=waldSimq(a[si], v[si], N)
    b = participant
    d = si-1
    data = readMat(paste(a, b, c, d, e, sep=""))
    #for (ter in seq(0, min(data[[1]]) - 0.001, length.out = 100)){
    #q_wald = quantile(data[[1]] - ter)
    f_wald = f
    
    #Creates a vector of observed frequency
    #  counts in each RT bin separated by
    #  quantiles from the exgsim function
    
    ls=wald_fit(f_wald)
    #return fit parameters and gsq values. 
    
    fpar=ls[[1]]
    newgval=ls[[2]]
    #if (newgval < f_wald_gsq[si]){
    f_a[si]=fpar[1]
    f_v[si]=fpar[2]
    f_wald_gsq[si]=newgval
    f_ter[si] = fpar[3]
    cnt=cnt+1
    
  }
  fits = data.frame(f_a, f_v, f_ter, f_wald_gsq)
  write.csv(fits, paste(path, h, sep=""))
  print(participant)
}
