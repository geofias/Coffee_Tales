# Global Coffee Trade and Disease Detection in Coffee Leaves
This repository contains two main projects:

1. **Global Coffee Trade EDA**: An exploratory data analysis (EDA) of global coffee trade data.
2. **Coffee Leaf Disease Detection**: A deep learning model to identify diseases in coffee leaf images.

## Global Coffee Trade EDA

### Overview
This project involves an exploratory data analysis (EDA) of global coffee trade data. The analysis aims to uncover insights and trends in the coffee trade industry. The results are presented in a dashboard created with Power BI.

### Features
- **Data Cleaning**: Handling missing values, outliers, and data normalization.
- **Data Visualization**: Creating insightful visualizations to identify trends and patterns.
- **Dashboard**: An interactive dashboard in Power BI to visualize the findings.

### Dashboard
The Power BI dashboard includes the following visualizations:

- Coffee production by country and consumption by coffee type
![Production](https://github.com/geofias/Coffee_Tales/assets/89147046/b30a8be3-b25a-4c70-9cac-af18d876c1d0)

- Coffee import trends
![Import](https://github.com/geofias/Coffee_Tales/assets/89147046/998ed593-e222-4aee-a737-27cf9f3e6f92)

- Coffee export trends
![Export](https://github.com/geofias/Coffee_Tales/assets/89147046/9822c200-9b03-46fb-8566-796b3a043bed)

### Files
- coffee_EDA.ipynb: Jupyter Notebook containing the EDA code.
- coffee_report.pbix: Power BI file for the dashboard.

[PDF Report](https://github.com/geofias/Coffee_Tales/blob/master/Global%20Coffee%20Trade%20Report.pdf)
[Article](https://github.com/geofias/Coffee_Tales/blob/master/Global%20Coffee%20Trade%20EDA.pdf)

## Coffee Leaf Disease Detection

### Overview
This project involves a deep learning model that identifies diseases in coffee leaf images. The model is deployed as a web application using Streamlit, allowing users to upload images of coffee leaves and receive predictions about potential diseases.

### Model
The model is built using TensorFlow and trained on a dataset of labeled coffee leaf images. It can identify several common diseases affecting coffee plants.

### Deployment
The model is deployed as a web application using Streamlit. You can access the application [here](https://coffeeleafdisease.streamlit.app/).

### Usage
**Upload Image**: Upload an image of a coffee leaf.
**Get Prediction**: The model processes the image and returns a prediction of the disease.

### Files
app.py: Streamlit application file.
model/coffee_model: Trained deep learning model.
requirements.txt: List of dependencies required to run the Streamlit application.

## Contributing
Feel free to submit issues or pull requests if you have any suggestions or improvements.

## Contact
For any questions or inquiries, please contact tamir-chong@hotmail.com
