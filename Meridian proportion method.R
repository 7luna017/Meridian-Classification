library(dplyr)
library(scales)

###1.Partitioning the data set
alldata<-read.csv("base Data1.csv",header=T)
alldata<-alldata[c(1,2,15,16)]
SM<-alldata[c(which(alldata$Number.of.Meridians=="single Meridian")),]
DM<-alldata[c(which(alldata$Number.of.Meridians=="dual Meridian")),]
MM<-alldata[c(which(alldata$Number.of.Meridians=="multiple Meridian")),]
M1<-SM[c(which(SM$group=="Lung")),]
M2<-SM[c(which(SM$group=="Liver")),]

###2.Construct the meridian set
S1<-data.frame(Mol.ID=M1[c(2)][!duplicated(M1[c(2)]),])
S2<-data.frame(Mol.ID=M2[c(2)][!duplicated(M2[c(2)]),])

H1<-count(M1,Mol.ID)
ccs<-H1[order(H1$n, decreasing= T), ]
plot(ccs[,2],type="l")
dev.off()
S3<-H1[which(H1$n >= 4), ]
S3<-S3[c(1)]                            

H2<-count(M2,Mol.ID)
dds<-H2[order(H2$n, decreasing= T), ]
plot(dds[,2],type="l")
dev.off()
S4<-H2[which(H2$n >= 3), ]
S4<-S4[c(1)]

S5<-data.frame(Mol.ID=intersect(M1$Mol.ID,M2$Mol.ID))
S6<-data.frame(Mol.ID=setdiff(S1, S5))
S7<-data.frame(Mol.ID=setdiff(S2, S5))
S8<-data.frame(intersect(S3,S4))
S9<-data.frame(Mol.ID=setdiff(S3, S8))
S10<-data.frame(Mol.ID=setdiff(S4, S8))
S<-list(S1,S2,S3,S4,S5,S6,S7,S8,S9,S10)

###3.Construct CP matrix
listherb<-c(alldata[c(1)][!duplicated(alldata[c(1)]),])
listd<-paste0("D", 1:10)
cd<-matrix(0,nrow=length(listherb),ncol=length(listd),dimnames=list(listherb, listd))
for(i in 1:length(listherb)){
  H<-alldata[c(which(alldata$herb==listherb[i])),]
  for(j in 1:10){
  cd[i,j]<-length(intersect(S[[j]]$Mol.ID,H$Mol.ID))
}
}

listf<-paste0("F", 1:20)
cp<-matrix(0,nrow=length(listherb),ncol=length(listf),dimnames=list(listherb, listf))
for(i in 1:length(listherb)){
  H<-alldata[c(which(alldata$herb==listherb[i])),]
  for(j in 1:10){
    if(cd[i,j]>0)
    {cp[i,j]<-cd[i,j]/nrow(S[[j]])
    cp[i,j+10]<-cd[i,j]/nrow(H)}
  }
  }

###4.Arcsine of the data
MD<-asin(cp)
MD<-cbind(alldata[!duplicated(alldata[c(1)]),c(4,1,3)],MD)
write.csv(MD,"Modeling Data.csv",row.names=FALSE)