import warnings
from sklearn.externals import joblib
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')
import numpy as np
import pandas as pd
import data_partitioning
from sklearn.metrics import roc_curve, auc
from sklearn.metrics import classification_report
from sklearn.metrics import balanced_accuracy_score
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

## 1.training the model function
test_score = []
test1_score = []
test2_score = []
test3_score = []
test_balanced_accuracy = []
test1_balanced_accuracy = []
test2_balanced_accuracy = []
test3_balanced_accuracy = []
best_estimator = []
for j in range(0, 1000):
    np.random.seed(seed=j)
    xtrain, ytrain, xtest, ytest, trainname, testname, xtest1, xtest2, xtest3, ytest1, ytest2, ytest3 = data_partitioning.Divide_the_data()

    parameters = {
        "kernel": ("poly", "rbf")
        , "C": np.logspace(-9, 10, 10, base=2)
        , "gamma": np.logspace(-9, 10, 10, base=2)
    }
    GS = GridSearchCV(SVC(), parameters).fit(xtrain, ytrain)

    xpre = GS.predict(xtest)
    xpre1 = GS.predict(xtest1)
    xpre2 = GS.predict(xtest2)
    xpre3 = GS.predict(xtest3)

    test_score.append(GS.score(xtest, ytest))
    test1_score.append(GS.score(xtest1, ytest1))
    test2_score.append(GS.score(xtest2, ytest2))
    test3_score.append(GS.score(xtest3, ytest3))

    test_balanced_accuracy.append(balanced_accuracy_score(ytest, xpre))
    test1_balanced_accuracy.append(balanced_accuracy_score(ytest1, xpre1))
    test2_balanced_accuracy.append(balanced_accuracy_score(ytest2, xpre2))
    test3_balanced_accuracy.append(balanced_accuracy_score(ytest3, xpre3))
    best_estimator.append(GS.best_estimator_)

## 2.Save model parameters
path = 'Classifiter.model'
test_balanced_accuracy_max = np.argmax(test_balanced_accuracy)
joblib.dump(best_estimator[test_balanced_accuracy_max], path)

## 3.Invoke the saved model
model = joblib.load(path)
np.random.seed(seed=test_balanced_accuracy_max)
xtrain, ytrain, xtest, ytest, trainname, testname, xtest1, xtest2, xtest3, ytest1, ytest2, ytest3 = data_partitioning.Divide_the_data()

## 4.predict the testing data
testname = np.array(testname)
meridian = model.decision_function(xtest)

for i in range(0, len(meridian)):
    print("{name} belongs to the {meridian} meridian.".format(name=testname[i], meridian=meridian[i]))
## 5. model evaluation

### 5.1 balanced accuracy
xpre_best = model.predict(xtest)
xpre1_best = model.predict(xtest1)
xpre2_best = model.predict(xtest2)
xpre3_best = model.predict(xtest3)
print("Balance accuracy of single test:", balanced_accuracy_score(ytest1, xpre1_best))
print("Balance accuracy of double test:", balanced_accuracy_score(ytest2, xpre2_best))
print("Multi-tested balance accuracy:", balanced_accuracy_score(ytest3, xpre3_best))
print("Test balance accuracy:", balanced_accuracy_score(ytest, xpre_best))

### 5.2 classification_report
print("classification_report:\n", classification_report(ytest, xpre_best))

### 5.3 Compute AUC
ytest_meridian = ytest.values
ytest_meridian[ytest_meridian == 'Lung'] = 1
ytest_meridian[ytest_meridian == 'Liver'] = 0
ytest_meridian = ytest_meridian.astype('int64')
ytest_meridian = pd.DataFrame(ytest_meridian, dtype='int64')

fpr, tpr, threshold = roc_curve(ytest_meridian, meridian)
roc_auc = auc(fpr, tpr)
print("AUC:", roc_auc)