import streamlit as st
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


st.image(r"C:\Users\shiva\Downloads\inno image.jpeg")

model=pickle.load(open(r"C:\Users\shiva\MACHINE LEARNING\nb.pkl","rb"))
model1=pickle.load(open(r"C:\Users\shiva\MACHINE LEARNING\nb1.pkl","rb"))



st.title("EMAIL Spam & Ham CLASSIFIER")  
st.write("write an email to classify spam or ham")


# Text input
email_text = st.text_area('Enter your email:')
checking=model1.transform([email_text])
prediciton=model.predict(checking)[0]

# Predict button
if st.button('Classify'):
    if prediciton=="spam":
        st.write("the email is spam")
        st.image(r"C:\Users\shiva\spam image.jpeg")
      
    else:
        st.image(r"C:\Users\shiva\ham.png")

else:
     st.write("this email is","ham")

        
  

                  