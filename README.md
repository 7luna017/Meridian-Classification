# Meridian-Classification
This is a method to predict the main target meridians of herbs by collecting the compound information and establishing the compound proportion matrix. In this package, we provide three modeling methods:  linear discriminant analysis (LDA),  logistic regression (LR) and support vector machine (SVM). We recommend to use the LR model, or make a choice based on the data comparing the results of the three models.
## Base Data.csv
This is the basic information of herbs collected through Chinese Pharmacopoeia (ChP) and TCMSP (Traditional Chinese Medicine Systems Pharmacology Database and Analysis Platform, http://tcmspw.com/tcmsp.php), including the name of herbs, the main targeted meridians, the number of targeted meridians, and the information of compounds.
## Modeling Data.csv
This is the CP matrix obtained by the meridian proportion method, and the data transformation is used to build the model.
## Meridian proportion method.R
The meridians set S1~s10 was established by single Meridian herbs of M1 and M2, and the CP matrix was calculated according to the proportion of herbs in the meridians set. If you want to use other meridians Data, please replace `Base Data.csv` with all herbs collected.
## lda.R
This procedure is an LDA model for classifying herbs targeting different meridians, including a feature screening process.
## data_partitioning.py
This procedure is used for machine learning part of the test set and training set division.
## LR.py
This procedure is an LR model for classifying herbs targeting different meridians, the model results are automatically output at the end of the run.
## SVM.py
This procedure is an SVM model for classifying herbs targeting different meridians, the model results are automatically output at the end of the run.
