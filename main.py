from imageai.Detection.Custom import DetectionModelTrainer
import tensorflow as tf


trainer = DetectionModelTrainer()

trainer.setModelTypeAsYOLOv3()

trainer.setDataDirectory(data_directory='model')

trainer.setTrainConfig(object_names_array=['rose'], batch_size=4, num_experiments=100)

trainer.trainModel()

# ImageAi = 2.1.6
# tenser 2.4.0
# numpy 1.19.3
# keras 2.4.3