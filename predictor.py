from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath(os.path.join(execution_path, "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
prediction.loadModel()

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "1.jpg"), result_count=3)

def guessTheImage():
    listOfPredictions = {}
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        listOfPredictions[eachPrediction] = eachProbability
    return listOfPredictions