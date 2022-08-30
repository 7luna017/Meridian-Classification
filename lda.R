library(MASS)
###1.Divide the data
data<-read.csv("Modeling Data.csv",header=T)
data$y <- 1
data$y[data$group=="Liver"] <- 2
SM<-data[c(which(data$Number.of.Meridians=="single Meridian")),]
DM<-data[c(which(data$Number.of.Meridians=="dual Meridian")),]
MM<-data[c(which(data$Number.of.Meridians=="multiple Meridian")),]

###2.Select features and build models
lm <- lm(y ~ F1 + F2 + F3 + F4 +F5 + F6 +F7 + F8 +F9 + F10 +
                 F11 + F12 + F13 + F14 +F15 + F16 +F17 + F18 +F19 + F20, data = DM)
st<-stepAIC(lm,direction = "both")
lda <- lda(y ~ F1 + F2 + F3 + F5 + F6 + F7 + F8 + F9 + F10 + F13 + F14 + 
             F16 + F18, data = DM, method="mle", prior = c(0.5 , 0.5)) 

###3.Predict meridian
pre<-predict(lda,data)
pre1<-predict(lda,SM)
pre2<-predict(lda,DM)
pre3<-predict(lda,MM)
predict<-data.frame(cbind(data$herb,pre$class))
predict[predict == 1] = "Lung"
predict[predict == 2] = "Liver"
names(predict)<-c("herb","Meridian")
predict

###4.Evaluation model
Evaluate<-function(preds,test.label,positiveclass,negativeclass, bta=1){
  recall<-length(which(preds==test.label&preds==positiveclass))/length(which(test.label==positiveclass)) 
  precision<-length (which(preds==test.label&preds==positiveclass))/length(which(preds==positiveclass)) 
  specifity<-length(which(preds==test.label&preds==negativeclass))/length(which(test.label==negativeclass))
  F_score<-(bta*2)*precision*recall/(recall+precision)
  BACC<-(recall+specifity)/2
  return(c(F_score=F_score, BACC=BACC, recall=recall, precision=precision, specifity=specifity))
}
#all data
Evaluate(pre$class, data$y ,1,2,bta=1)
#single Meridian herb
Evaluate(pre1$class, SM$y ,1,2,bta=1)
#dual Meridian herb
Evaluate(pre2$class, DM$y ,1,2,bta=1)
#multiple Meridian herb
Evaluate(pre3$class, MM$y ,1,2,bta=1)






