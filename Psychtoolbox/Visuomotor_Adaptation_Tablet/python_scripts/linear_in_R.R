library(e1071)
A = c()
B = c()
for (participant in 1:60){
  
  fname = paste("data_csvs/train_", toString(participant - 1), ".csv", sep = "")
  foo1 = read.csv(fname)
  foo1$rot_est_n1 = 90 - foo1$Curvature_n1
  foo1$rot_est_n = 90 - foo1$Curvature_n
  if (participant - 1 %% 4 == 0 || participant - 1 %% 4 == 1) {
    model = lm(foo1$rot_est_n~foo1$rot_est_n1 + foo1$Curvature_n - 1)
  }
  A = c(A, model$coefficients[1])
  B = c(B, model$coefficients[2])
}
model$coefficients[1]
