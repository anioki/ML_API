# ML_API
API for predicting telephone price range  
## Project description  
### Structure of project 

```` 
app
    ├── data                        - contains train and validation data
    │   ├── train.csv               - train set 
    │   └── val.csv                 - validation set (must contain target values)
    ├── models                      - this folder contains a trained estimator.
    │   └── finalized_model.pickle  - trained estimator. 
    │
    ├── settings                    - here you can store different constant values, connection parameters, etc.
    │   ├── constants.py            - multiple constants storage for their convenient usage.
    │   └── specifications.json     - specifications of your data preprocessing operations.   
    │   
    ├── utils                       - this folder contains instruments we'll use to work with dataset.
    │   ├── __init__.py             - init file for the package. 
    │   ├── dataloader.py           - dataloader. 
    │   ├── dataset.py              - class dedicated for giving info about the dataset.
    │   ├── predictor.py            - predictor.
    │   └── trainer.py              - train script.
    │ 
    ├── app.py                      - route, app.
    │
    ├── requirements.txt
    │
    └── Dockerfile
````   
### In work  
API has only one command: /predict GET and data for prediction.
Data format: battery_power, blue, dual_sim, fc, int_memory, mobile_wt, pc, px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi. Price_range is predicted value.  
For test the app run run.py. Output:  
![image](https://user-images.githubusercontent.com/77074682/122591409-997b3a00-d06b-11eb-99c6-1a1c1084bd94.png 'Output')
