# Meridian-Classification
This is a method to predict the main target meridians of herbs by collecting the compound information and establishing the compound proportion matrix. In this package, we provide three modeling methods:  linear discriminant analysis (LDA),  logistic regression (LR) and support vector machine (SVM). We recommend to use the LR model, or make a choice based on the data comparing the results of the three models.
## Base Data.csv
This is the basic information of herbs collected through Chinese Pharmacopoeia (ChP) and TCMSP (Traditional Chinese Medicine Systems Pharmacology Database and Analysis Platform, http://tcmspw.com/tcmsp.php), including the name of herbs, the main targeted meridians, the number of targeted meridians, and the information of compounds.
## Modeling Data.csv
This is the CP matrix obtained by the meridian proportion method, and the data transformation is used to build the model.
## Meridian collection proportion method.R



