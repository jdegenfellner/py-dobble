library(dplyr)
library(utils)

dat <- read.csv(file.choose(), header = FALSE, sep = ",")
dat[is.na(dat)] <- 0
dat
colSums(dat)

# Verify empirically if 2 random columns only have to symbols in common:
colnames(dat)
dim(dat)
dat <- dat[,2:58]
dim(dat)

all_comb <- combn(colnames(dat), 2)
n <- dim(all_comb)[2]
vals <- c()
for(i in 1:n){
  vals[i] <- sum(rowSums(dat[, all_comb[,i]])==2)
}
sum(!vals==1) # 0
