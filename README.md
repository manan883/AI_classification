# AI classification

---
This project uses image classification on video. This model is trained on the intels image classification dataset


Image files are not uplodaded so the training_dataset folder will be empty. 

The model will train or load up a model if one is provided. Then as the video is being loaded live the data is being predicted by the model

# Demo
[![Watch the video](https://i9.ytimg.com/vi/owg6AqfX7Gk/mq2.jpg?sqp=CMjWk6wG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYAC0AWKAgwIABABGGUgXChNMA8=&rs=AOn4CLAcBMExDuV-pCNXqleCltEA_Uy8Jg)](https://youtu.be/owg6AqfX7Gk)

# Improvements to be made
Training data was trained with images the size (150,150) since thats what intels dataset uses. Therefore when predicting the image must be the same shape of (150,150) and clarity can be lost. Training with larger images on a faster machine can help accuracy for predictions.

Use OS.path to verify paths before saving/reading from it

Add YAML files to handle path variables

# Features I want to add
I want to use Meta's SAM to outline objects in the video and classify those specific objects live
