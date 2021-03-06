# Criminal Justice CS Thesis

## Abstract  ##
As part of the world’s largest penal system, some United States prisons have taken to the use of algorithms to classify arrested individuals, predicting their likelihoods of recidivism for the purposes of setting bail, offering parole, etc. These algorithms are produced by private companies, usually proprietary, and rarely tested by independent researchers or in more than one trial before their application in the judicial system. They are demonstrably biased against people from historically-disadvantaged backgrounds. We attempted to determine how machine learning models would develop and perform compared to pre-existing algorithms given the same inputs. 
We began by testing individual machine learning algorithms and explored different parameter configurations to improve accuracy. Using those as component models, we employed two versions of ensemble machine learning models, utilizing multiple approaches in parallel in an effort to combine the component models’ strengths while mitigating their weaknesses. Our results were promising but overall inconclusive, partly due to the datasets being too small relative to their complexity for the machine learning approaches. The ensemble models did not show significantly improved accuracy, though we believe this is reflective more of the difficulty of exploring the necessarily-larger configuration space than an inherent shortcoming of ensemble machine learning approaches.

## To Run ##
Long-Final_test.py and broward_Norm_Script.py run the Meta Learner and Super Learner respectively. Both output the accuracy metrics of the model running on various data sets and export results to a formatted csv file.

## Extras  ##
Clustering and vector analysis tools were placed in the extra folder that helped us do preliminary analysis on new datasets. Additionally, multiple different configurations of the Super Learner are within the Ensemble_Learning folders that were not used for the final results of our thesis. 
