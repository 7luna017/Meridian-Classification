import pandas as pd


### 1.import data and data preparation
data = pd.read_csv('Modeling Data.csv')
single_data = data.iloc[:len(data[data['Number.of.Meridians'] == 'single Meridian']),:]
double_data = data.iloc[len(data[data['Number.of.Meridians'] == 'single Meridian']):len(data[data['Number.of.Meridians'] == 'dual Meridian'])+len(data[data['Number.of.Meridians'] == 'single Meridian']),:]
multiple_data = data.iloc[len(data[data['Number.of.Meridians'] == 'dual Meridian'])+len(data[data['Number.of.Meridians'] == 'single Meridian']):len(data[data['Number.of.Meridians'] == 'dual Meridian'])+len(data[data['Number.of.Meridians'] == 'single Meridian'])+len(data[data['Number.of.Meridians'] == 'multiple Meridian']),:]


### 2.prepare testing dataset and training dataset
def Divide_the_data():
    train1 = single_data.sample(frac=0.70, replace=False, weights=None, random_state=None)
    test1 = single_data[~single_data.index.isin(train1.index)]

    train2 = double_data.sample(frac=0.70, replace=False, weights=None, random_state=None)
    test2 = double_data[~double_data.index.isin(train2.index)]

    train3 = multiple_data.sample(frac=0.70, replace=False, weights=None, random_state=None)
    test3 = multiple_data[~multiple_data.index.isin(train3.index)]

    xtrain1 = train1.iloc[:, 3:]
    ytrain1 = train1.iloc[:, :1]
    trainname1 = train1.iloc[:, 1]
    xtest1 = test1.iloc[:, 3:]
    ytest1 = test1.iloc[:, :1]
    testname1 = test1.iloc[:, 1]

    xtrain2 = train2.iloc[:, 3:]
    ytrain2 = train2.iloc[:, :1]
    trainname2 = train2.iloc[:, 1]
    xtest2 = test2.iloc[:, 3:]
    ytest2 = test2.iloc[:, :1]
    testname2 = test2.iloc[:, 1]

    xtrain3 = train3.iloc[:, 3:]
    ytrain3 = train3.iloc[:, :1]
    trainname3 = train3.iloc[:, 1]
    xtest3 = test3.iloc[:, 3:]
    ytest3 = test3.iloc[:, :1]
    testname3 = test3.iloc[:, 1]

    xtrain12 = xtrain1.append(xtrain2)
    xtrain = xtrain12.append(xtrain3)

    ytrain12 = ytrain1.append(ytrain2)
    ytrain = ytrain12.append(ytrain3)

    trainname12 = trainname1.append(trainname2)
    trainname = trainname12.append(trainname3)

    xtest12 = xtest1.append(xtest2)
    xtest = xtest12.append(xtest3)

    ytest12 = ytest1.append(ytest2)
    ytest = ytest12.append(ytest3)
    testname12 = testname1.append(testname2)
    testname = testname12.append(testname3)

    return xtrain, ytrain, xtest, ytest, trainname, testname, xtest1, xtest2, xtest3, ytest1, ytest2, ytest3