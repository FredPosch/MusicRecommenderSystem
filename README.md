# Designing a music recommendation system based on content-based filtering

## Final Project in Unsupervised Machine Learning

This project uses a dataset obtained from kaggle that uses spotify songs that are enriched with several audio features.

## About the dataset:

The origina dataset is stored in the "data" folder and then called in the scripts.

## The exploratory data analysis and the data manipulation:

Both the EDA and the data manipulation are done in one script called "Exploratory_Data_Analysis".
This script also write csv's with the altered data, that the model implementation scripts need as input.

## Models:

In this project four different models are estimated. For each of these separate scripts were created.

### Model with the full dataset

This is the first Model that was estimated using all available features that were created in the data manipulation.
The script also includes an analysis of the popularity bias. The script is called "Model_Implementation_full".

### Model with the PCA selected dataset

The second model that was estimated used the data that was created with the pca analysis in the data manipulation.
The script is called "Model_Implementation_pca".

### Model with the

The second model only used the audio features of the data.
The script is called "Model_Implementation_audio_only".

### Final Model with genre selection

The last model is the modified version. It uses the same algorithm and the same dataset. However, the dataset is individually trained on a subset of the data of user-selected genres.
The script is called "Model_Implementation_genre_specific".

### Link to the dataset: 

https://www.kaggle.com/datasets/maharshipandya/-spotify-tracks-dataset?resource=download
