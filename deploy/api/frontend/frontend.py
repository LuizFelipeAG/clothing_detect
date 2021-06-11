#from utils.model_utils import predict
import streamlit as st
import requests
from utils.io_utils import load_config

config = load_config()

st.title("Clothing Classifier")
url = st.text_input("Image url")

if url:
    response = requests.get(config["api"]["prediction_url"], params={"url": url})
    imageurl = response.json()['url']
    ctype = response.json()['predicted_class']
    predconf = response.json()['predicted_confidence']
    st.image(imageurl, width=200, caption=imageurl)
    st.write("Clothing type : ",ctype)
    st.write("Accuracy : ","{:.8f}%".format(predconf * 100))