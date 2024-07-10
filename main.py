import streamlit as st
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer


st.image(r"inno image.jpeg")

model=pickle.load(open(r"nb.pkl","rb"))
model1=pickle.load(open(r"nb1.pkl","rb"))



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
        st.image(r"spam image.jpeg")
      
    else:
        st.image(r"ham.png")

else:
     st.write("this email is","ham")

        
  

                  
