import numpy as np
import EnsembleModel
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from scipy import stats
import copy

class discreteSL(EnsembleModel.EnsembleModel):

    ##  takes in list of component models  ##
    def __init__(self, model_list):
        self.model_list = model_list
        self.model_accuracies = []
        self.best_model = model_list[0]

    ##  creates deep copy of dataset, with ith fold removed  ##
    def concatenate(self, folds, i):
        folds_copy = copy.deepcopy(folds)
        test = folds_copy.pop(i)
        return np.concatenate(folds_copy, axis=0), test

    ##  finds average accuracy for each model based on accuracy list  ##
    def mean_accuracies(self,accuracies_list,b):
        self.model_accuracies = [sum(x)/b for x in zip(*accuracies_list)]

    ##  selects model with best overall accuracy  ##
    def select_model(self):
        high_acc = 0
        high_indx = 0
        for i in range(len(self.model_list)):
            current_acc = self.model_accuracies[i]
            if(high_acc < current_acc):
                high_acc = current_acc
                high_indx = i
        self.best_model = self.model_list[i]

    ##  splits the dataset into b folds, and trains component  ##
    ##  models on each fold while keeping track of accuracy  ##
    def train(self, inputs, outputs, b=10):
        input_folds = np.array_split(inputs, b)
        output_folds = np.array_split(outputs, b)
        accuracies_list = []
        for i in range(len(input_folds)):
            x_train, x_test = self.concatenate(input_folds, i)
            y_train, y_test = self.concatenate(output_folds, i)
            self.fold_train(x_train, y_train)
            accuracies = self.fold_accuracy(x_test,y_test)
            accuracies_list.append(accuracies)
        self.mean_accuracies(accuracies_list,b)
        self.select_model()
        print(self.model_accuracies)
        print(self.best_model)

    ##  trains each model on input  ##
    def fold_train(self, x_train, y_train):
        for i in range(len(self.model_list)):
            self.model_list[i].train(x_train,y_train)

    ##  returns prediction from best model  ##
    def predict(self, x_test):
        return self.best_model.predict(x_test)

    ##  gets accuracy for each model in input ##
    def fold_accuracy(self, x_test, y_test):
        accuracies = []
        for i in range(len(self.model_list)):
            prediction = self.model_list[i].report_accuracy(x_test, y_test)
            accuracies.append(prediction)
        return accuracies

    ##  returns accuracy from best model  ##
    def report_accuracy(self, x_test, y_test):
        return self.best_model.report_accuracy(x_test, y_test)
