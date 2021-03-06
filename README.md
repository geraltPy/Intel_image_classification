# Intel image classification
## Dataset
Dataset is used from kaggle link below,
https://www.kaggle.com/puneet6060/intel-image-classification/  

This Data contains around 25k images of size 150x150 distributed under 6 categories.  

<p>
   <img src="https://github.com/geraltPy/Intel_image_classification/blob/main/images/building.jpg" width="150" height="150"/>
   <img src="https://github.com/geraltPy/Intel_image_classification/blob/main/images/forest.jpg" width="150" height="150"/>
   <img src="https://github.com/geraltPy/Intel_image_classification/blob/main/images/glacier.jpg" width="150" height="150"/>
   <img src="https://github.com/geraltPy/Intel_image_classification/blob/main/images/mountian.jpg" width="150" height="150"/>
   <img src="https://github.com/geraltPy/Intel_image_classification/blob/main/images/sea.jpg" width="150" height="150"/>
   <img src="https://github.com/geraltPy/Intel_image_classification/blob/main/images/street.jpg" width="150" height="150"/>
</p>

- buildings -> 0
- forest -> 1 
- glacier -> 2 
- mountain -> 3 
- sea -> 4 
- street -> 5

The Train, Test and Prediction data is separated in each zip files. There are around 14k images in Train, 3k in Test and 7k in Prediction.  
This data was initially published on https://datahack.analyticsvidhya.com by Intel to host a Image classification Challenge.  

## Model
Finetuned MobileNetV3 on this dataset.   
Model is quantized using tf_lite converter to reduce the size from 25.6mb to 4.8mb for deployment.

## Results
Model is fine-tuned for 50 epochs with Dropout Layer of 0.2 in Dense layer and 
had ~91% validation accuracy.

## Deployment
Deployed using Heroku server, and tf_lite MobileNetV3 model.  
https://geraltpy-image-classifier.herokuapp.com/  

<p>
   <img src="https://github.com/geraltPy/Intel_image_classification/blob/main/images/webpage.png" width="900" height="450"/>
</p>
