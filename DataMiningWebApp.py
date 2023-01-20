import pandas as pd
import streamlit as st
import time
import webbrowser
from PIL import Image

st.title ("Data Mining Project: Self-Service Laundry Shop")

df = pd.read_csv("Cleaned_Dataset.csv")

#Select Location
Select = st.radio("Please select", ("Map", "Question 1", "Question 2", "Question 3"))

if Select == "Map":
    # set header
    st.header('Location of every customer')
    st.markdown('Map below is showing the location of every customer based on the coordinate given in the dataset.')
    people_loc_df = df[["latitude","longitude"]]
    #print "updating" message
    my_element = st.info("Updating...")
    for i in range(1):
        time.sleep(1)
    #Remove the message & others element
    my_element.empty()  
    #zoom level of the map
    zoom = 11
    #set map
    my_element = st.map(people_loc_df, zoom=zoom)
elif Select == "Question 1":
    # set header
    st.header('Question 1: Which generation of customer spend the most time in the shop?')
    
    # set subheader
    st.subheader('Exploratory Data Analysis')
    st.markdown('First, cut the time spent by the customer into bins of [10,20,30,40,50,60] and plotted a Bar chart for the binned time spent.')
    image = Image.open('Bar Chart for Binned Time Spent.jpg')
    st.image(image, caption='Bar Chart for Binned Time Spent')
    st.markdown('Based on the bar chart above, we can know that the time of most of the customer spent are at the range from 30 minutes to 40 minutes.')
    
    st.markdown('After that, cut the age of the customer into bins of [10,20,30,40,50,60] and plotted a Bar chart to show which age group has the highest total time spent in the laundry shop.')
    image = Image.open('Total Time Spent by Different Group Age of Customer.jpg')
    st.image(image, caption='Total Time Spent by Different Group Age of Customer')
    st.markdown('Based on the Bar chart above, we can see that the customers which are in the age range from 30 to 40 has the hightest time spent in the laundry shop.')
    
    # set subheader
    st.subheader('Clustering Analysis - K-Means')
    image = Image.open('K-Means(Clustering).jpg')
    st.image(image, caption='K-Means(Clustering)')
    st.markdown('Silhouette Score (n=7) =  0.3933169987159571')
    st.markdown('Silhouette score is a metric used to calculate the goodness of a clustering technique. Its value ranges from -1 to 1.')
    st.markdown('- 1: clusters are well apart from each other and clearly distinguished.')
    st.markdown('- 0: clusters are indifferent, or we can say that the distance between clusters is not significant.')
    st.markdown('- 1: clusters are assigned in the wrong way.')
    st.markdown('Since the score is 0.3933169987159571 which is below 1 and above 0, therefore we can say that the result is consider ok but not very good.')
    
elif Select == "Question 2":
    # set header
    st.header('Question 2: Which generation of customer spend the most time in the shop?')
    
    # set subheader
    st.subheader('Exploratory Data Analysis')
    st.markdown('First, visualize the relationship of the sales and the weather.')
    st.markdown('The first plot will be showing the sales during no rain day.')
    image = Image.open('Sales vs Date (No Rain).jpg')
    st.image(image, caption='Sales vs Date (No Rain)')
    
    st.markdown('The next plot will be showing the sales during rainny day.')
    image = Image.open('Sales vs Date (Rain).jpg')
    st.image(image, caption='Sales vs Date (Rain)')
    
    st.markdown('In order to observe the differences of the plots easilly, we combine both plot into one.')
    image = Image.open('Sales vs Date (Combine).jpg')
    st.image(image, caption='Sales vs Date (Rain)')
    st.markdown('From the graph above, we can see that there is a slight difference on the sales based on the weather, did it rain.')
    st.markdown('There is a slightly higher sales revenue when there is rain.')
    
    # set subheader
    st.subheader('Regression Model - Linear Regression')
    st.markdown('First, we construct a Linear Regression model using statemodels and the plot below is the result of it.')
    image = Image.open('Result regression model (statemodels).jpg')
    st.image(image, caption='Linear Regression model (statemodels)')
    
    st.markdown('Beside using statemodels, we also construct the Linear Regression model using sklearn.')
    image = Image.open('Result regression model (sklearn) 1.jpg')
    st.image(image, caption='Linear Regression model (sklearn)')
    image = Image.open('Result regression model (sklearn) 2.jpg')
    st.image(image, caption='Linear Regression model (sklearn)')
    
    # set subheader
    st.subheader('Regression Model - Decision Tree')
    image = Image.open('Decision Tree Regressor Result.jpg')
    st.image(image, caption='Decision Tree Regressor')
    st.markdown('Mean absolute error = 213.58')
    st.markdown('MSE :  80110.303842')
    st.markdown('RMSE :  283.037637')
    
elif Select == "Question 3":
    # set header
    st.header('Question 3: What types of customer will bring kids?')
    
    # set subheader
    st.subheader('Exploratory Data Analysis')
    st.markdown('First, we plot a bar chart to show the amount of customer who bring kids based on their races and gender.')
    image = Image.open('Customer who will bring kids.jpg')
    st.image(image, caption='Customer who will bring kids')
    st.markdown('Based on the Group Bar plot, we can find out that majority of the female, especially Malay Female like to bring kids to laundry. The amount of female malay is 457, higher than male malay. Indian female amount is 350, compare with Indian male is higher. However, when comparision between chinese male and female, chinese male amount slighty higher than chinese female. At last, Foreigner female amount is higher than foreigner male.')
    
    st.markdown('Next will be plotting a chart which shows the type of kids that a female customer bring to the laundry shop.')
    image = Image.open('Kids type that a female customer will bring.jpg')
    st.image(image, caption='Kids type that a female customer will bring')
    
    # set subheader
    st.subheader('Association Rule Minning')
    st.markdown('We also used Association Rule Minning to find out the characteristic of customer that will bring kids to the laundry shop.')
    image = Image.open('Association Rule Minning.jpg')
    st.image(image, caption='Association Rule Minning')

    # set subheader
    st.subheader('Feature Selection - Boruta')
    st.markdown('The first feature selection technique we used is Boruta Feature Selection. The plot below is showing the Boruta Features Score.')
    image = Image.open('Boruta Features Score.jpg')
    st.image(image, caption='Boruta Features Score')
    
    # set subheader
    st.subheader('Feature Selection - Information Gain')
    st.markdown('The second feature selection technique we used is Information Gain Feature Selection. The plot below is showing the Information Gain Features Score.')
    image = Image.open('Information Gain Features Score.jpg')
    st.image(image, caption='Information Gain Features Score')
    
    # set subheader
    st.subheader('Classification - SVM')
    st.markdown('Our first classification model is SVM.')
    st.markdown('We fit the model with Top 5 & 10 features (Information Gain & Boruta).')
    image = Image.open('ROC plot for SVM models.jpg')
    st.image(image, caption='ROC plot for SVM models')
    
    # set subheader
    st.subheader('Classification - KNN')
    st.markdown('Second classification model will be KNN.')
    st.markdown('We created the k-NN model with 10 neighbours and also fit the model with Top 5 & 10 features (Information Gain & Boruta).')
    image = Image.open('ROC plot for KNN models.jpg')
    st.image(image, caption='ROC plot for KNN models')
    
    # set subheader
    st.subheader('Stacked Ensemble Modeling')
    st.markdown('- Level-0 = {K-NN, SVM}')
    st.markdown('- Level-1 = SVM')
    image = Image.open('Stacked Emsemble model.jpg')
    st.image(image, caption='Stacked Emsemble model')
    
    # set subheader
    st.subheader('SMOTE')
    st.markdown('We created a KNN classifier in fit the model to SMOTE dataset & NON-SMOTE dataset in order to see the differences.')
    st.markdown('We also plotted a ROC chart to compare KNN classifier with and without SMOTE')
    image = Image.open('ROC plot for KNN with SMOTE and without SMOTE.jpg')
    st.image(image, caption='ROC plot for KNN with SMOTE and without SMOTE')
    
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////    
with open("Report.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Report",
                    data=PDFbyte,
                    file_name="Report.pdf",
                    mime='application/octet-stream')
