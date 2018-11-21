from imageai.Prediction.Custom import ModelTraining

model_trainer = ModelTraining()
model_trainer.setModelTypeAsResNet()
model_trainer.setDataDirectory("objectsToTrain")
model_trainer.trainModel(num_objects=257, num_experiments=100, batch_size=32, show_network_summary=True)