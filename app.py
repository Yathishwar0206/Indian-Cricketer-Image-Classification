import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import tempfile
import json
import time
import pyttsx3
import os
import gdown

MODEL_PATH = "cricketer_model.h5"
FILE_ID = "138hKrKI_uITK7rLlA1WrEcPiuuVZc7Xc"
GDRIVE_URL = f"https://drive.google.com/uc?id={FILE_ID}"

# Load model
def load_model():
    if not os.path.exists(MODEL_PATH):
        gdown.download(GDRIVE_URL, MODEL_PATH, quiet=False)
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    return model
# Side bar
st.set_page_config(page_title="Indian Cricketer Recognition",layout="centered")
st.sidebar.image("logo/logo.png",width=150)
st.sidebar.write("🧭 Navigation")
page = st.sidebar.radio("Go to",["Home","About Cricket","Image Classification","Indian Cricket Quiz","Contact"])
st.sidebar.write("Give the Image Take the Knowledge.")

# Common background
def set_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: 
            linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
            url("https://www.shutterstock.com/image-photo/beautiful-sports-stadium-green-grass-600nw-2428080603.jpg");
            background-size: cover;
            background-position: center;
        }
        h1, h2, h3, h4, h5, h6, p, span {
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )



# Home page
if page == "Home":
   set_bg()
   st.markdown("<h1 style='text-align:center;'>YR Indian Cricketer Image Classifier</h1>", unsafe_allow_html=True)
   st.caption("<h3 style='text-align:center;'> Give the Image Take the Knowledge. </h3>",unsafe_allow_html=True)
   st.logo("logo/logo.png",icon_image="logo/logo.png")
   st.set_page_config(layout='centered')
   col1, col2, col3 = st.columns([1,1,1.05])
   with col2:
       st.logo("logo/logo.png")
       st.image("logo/logo.png",width=300)

# About Cricket
elif page == "About Cricket":
   set_bg()
   st.title("🏏About the Indian Cricket")
   st.write("""
            Welcome to Our website!
            This page give information about the Indian Cricket.
            """)
   st.header("🏏YR Indian Cricketer Image Classifier")
   st.write("""
            We are providing the information about the Indian cricketer.
            Here you got the *player's role in the cricket, **Data of the Birth, **Runs and Wickets in ODI*,
            *Runs and Wickets in Test, **Runs and Wickets in IPL,  **Man of the Match, **Nick name of the player*,       
            *Info of the player*. These are datas given by ourself.
            """)
   st.write("We providing the knowledge about Indian Cricketer")
   
   st.header("📌 Introduction")
   st.write("""
            Cricket is more than just a sport in India—it is a national passion. 
            From colonial beginnings to global dominance, Indian cricket has evolved into one of the most powerful forces in world cricket.
            """)
   
   st.header("🕰 Early History (1721–1932)")
   st.write("""
            1.Cricket was introduced to India by the British East India Company in the early 18th century.  
            2.The first recorded cricket match in India was played in 1721.  
            3.Parsis were the first Indian community to adopt cricket.  
            4.The Board of Control for Cricket in India (BCCI) was founded in 1928.  
            5.India played its first Test match against England at Lord’s in 1932, led by C. K. Nayudu.  
            """)
   
   st.header("🏏 Growth & Struggles (1932–1970)")
   st.write("""
            India struggled initially due to lack of facilities and experience.  
            First Test victory came in 1952 against England in Madras (Chennai).  
            Legendary players like:
            *1. Vinoo Mankad*  
            *2. Polly Umrigar*  
            *3. Mansur Ali Khan Pataudi helped build the team’s foundation.*  
            India became strong in spin bowling, especially on home pitches.  
            """)
   
   st.header("🌟 Golden Era Begins (1970–1990)")
   st.write("""
            India won its first overseas Test series in 1971 (England & West Indies).  
            Famous spin quartet:  
            *1. Bishan Singh Bedi*  
            *2. Erapalli Prasanna*  
            *3. Bhagwat Chandrasekhar*  
            *4. Srinivas Venkataraghavan*  
            *5. Kapil Dev emerged as a world-class all-rounder.*  
            The biggest moment came in 1983:  
            India won the ICC Cricket World Cup
            Captain: Kapil Dev  
            Final victory against West Indies at Lord’s  
            This victory changed Indian cricket forever.  
            """)
   
   st.header("👑 Sachin Era & Professionalism (1990–2010)")
   st.write("""
            Sachin Tendulkar debuted in 1989 and became the face of Indian cricket.  
            India saw stars like:  
            *1. Rahul Dravid*  
            *2. Sourav Ganguly* 
            *3. Anil Kumble*  
            *4. VVS Laxman*  
            Historic wins:  
            2001 Test series vs Australia (Kolkata comeback)  
            
            India became:  
            *1. More professional*  
            *2. Stronger overseas*  
            
            India won:  
            ICC Champions Trophy 2002 (shared)  
            
            ICC T20 World Cup 2007 under MS Dhoni
            """)
   
   st.header("🏆 MS Dhoni Era – The Most Successful (2007–2017)")
   st.write("""
            MS Dhoni became captain and transformed Indian cricket.  
            Major achievements:  
            🏆 *T20 World Cup 2007*  
            🏆 *ODI World Cup 2011*  
            🏆 *Champions Trophy 2013*  
            
            India reached No.1 Test ranking.  
            Known for:  
            *1. Calm leadership*  
            *2. Strong team culture*  
            *3. Excellent finishers*  
            """)
   
   st.header("🔥 Modern Era (2017–Present)")
   st.write("""
            Virat Kohli led India to:  
            *1. Aggressive, fitness-driven cricket*   
            *2. Historic Test series win in Australia (2018–19)*  
            Rohit Sharma continued success with:  
            *Strong ICC performances*  
            
            India became dominant in:  
            *1. All formats*  
            *2. IPL influence*  
            
            *New stars*:  
            1. *Jasprit Bumrah*  
            2. *Ravindra Jadeja*  
            3. *Rishabh Pant*  
            4. *Shubman Gill*  
            5. *Yashasvi Jaiswal*  
            India won the ICC T20 World Cup 2024, ending an ICC trophy drought.
            """)
   st.header("🏟 Indian Premier League (IPL)")
   st.write("""
            1. *Revolutionized world cricket*  
            2. *Platform for young Indian talent*  
            3. *Brought financial power to Indian cricket*  
            4. *Made India the richest cricketing nation*  
            """)
   
   st.header("Conclusion")
   st.write("""
            Indian cricket’s journey—from colonial roots to world dominance—is a story of talent, passion, resilience, and evolution. 
            Today, India stands as a global cricket powerhouse, inspiring millions across the world.
            """)
# Prediction 
elif page == "Image Classification":
    set_bg()
    model = load_model()
    st.markdown(
        """
        <marquee behavior="scroll" direction="left" style="font-size:24px; color:white;">
        🏏 Indian Cricketer Prediction is Running...
        </marquee>
        """,
        unsafe_allow_html=True
        )
    
    # Streamlit UI
    st.markdown("<h1 style='text-align:center;'>🏏 Indian Cricketer Recognition with 🗣🔊 Voice output</h1>",unsafe_allow_html=True)
    st.write("Upload a cricketer image to get details with voice output")
    
    # Load class names
    with open("class_indices.json", "r") as f:
        class_indices = json.load(f)
        class_names = {v: k for k, v in class_indices.items()}

    # Load player info
    with open("Players.json", "r") as f:
        player_info = json.load(f)

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", width=250)

        img = image.resize((224, 224))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        class_index = np.argmax(prediction)
        confidence = np.max(prediction)

        class_name = class_names[class_index]
        
        confidence = np.max(prediction)
        if confidence >= 0.60:
            player = player_info.get(class_name)
            
            if player:
                st.subheader(player["displayName"])
                st.write("**Player Name** : ",player['displayName'])
                st.write("**Role in the Cricket** : ", player["role"])
                st.write("**Date of Birth** : ", player["born"])
                st.write("**Nation** : **Indian**")
                st.write("**Info of the Player** : ", player["info"])
                st.write("**Runs and Wickets in ODI**: ", player["ODI"])
                st.write("**Runs and Wickets in Test**: ", player["Test"])
                st.write("**Runs and Wickets in IPL** : ", player["IPL"])
                st.write("**Man of the Match Awards** : ", player["Man_of_the_Match"])
                st.write("**Nick Name of the Player** : ", player["Nickname"])
                
                info_text = (
                    f"Player Name : {player['displayName']}\n"
                    f"Role in the Cricket : {player['role']}\n"
                    f"Date of Birth : {player['born']}\n"
                    "Nation : Indian \n"
                    f"Info of the Player : {player['info']}\n"
                    f"Runs and Wickets in ODI : {player['ODI']}\n"
                    f"Runs and Wickets in Test : {player['Test']}\n"
                    f"Runs and Wickets in IPL : {player['IPL']}\n"
                    f"Man of the Match Awards : {player['Man_of_the_Match']}\n"
                    f"Nick name of the Player : {player['Nickname']}"
                    )
            else:
                st.write("Player information not available")
                info_text = "Player information not available."
        else:
            st.write("Player not confidently recognized")
            info_text = "Player not confidently recognized."
            
            # Voice Output Controls
        def generate_offline_audio(text):
            engine = pyttsx3.init()   # 🔥 re-init engine every time
            engine.setProperty("rate", 160)
            temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            temp_audio.close()
            engine.save_to_file(text, temp_audio.name)
            engine.runAndWait()
            engine.stop()
            return temp_audio.name
        st.markdown("### 🔊 Voice Output (Offline)")
        if st.button("▶ Play Voice (Offline)"):
            audio_file = generate_offline_audio(info_text)
            st.audio(audio_file, format="audio/wav")
        if st.button("⏹ Stop Voice"):
            st.stop()
    # Quiz
elif page == "Indian Cricket Quiz":
    set_bg()
    st.title("🤔 Indian Cricketer Quiz")
    st.write("Improve Your knowledge in Cricket")
    
    # Questions and Answers
    quiz = [
        {
            "question": "Which Indian cricketer is known for his famous last-over finish against Bangladesh in the 2018 Nidahas Trophy?",
            "options": ["MS Dhoni", "Dinesh Karthik", "Rohit Sharma", "Virat Kohli"],
            "answer": "Dinesh Karthik"
        },
        {
            "question": "Which Indian all-rounder is nicknamed 'Kung Fu Pandya' and captained Gujarat Titans to an IPL title?",
            "options": ["Hardik Pandya", "Ravindra Jadeja", "Shivam Dube", "Axar Patel"],
            "answer": "Hardik Pandya"
        },
        {
            "question": "Which Indian wicketkeeper-batsman scored the fastest double century in ODI cricket?",
            "options": ["Rishabh Pant", "Ishan Kishan", "KL Rahul", "MS Dhoni"],
            "answer": "Ishan Kishan"
        },
        {
            "question": "Which Indian fast bowler has a unique sling-arm action?",
            "options": ["Mohammed Shami", "Jasprit Bumrah", "Ishant Sharma", "Bhuvneshwar Kumar"],
            "answer": "Jasprit Bumrah"
        },
        {
            "question": "Which Indian batsman has scored centuries in all three formats?",
            "options": ["KL Rahul", "Shubman Gill", "Suresh Raina", "Rohit Sharma"],
            "answer": "KL Rahul"
        },
        {
            "question": "Who is the only Indian captain to win all ICC trophies?",
            "options": ["Virat Kohli", "MS Dhoni", "Kapil Dev", "Sourav Ganguly"],
            "answer": "MS Dhoni"
        },
        {
            "question": "Which Indian pacer is called the 'Yorker King'?",
            "options": ["Bumrah", "Natarajan", "Shami", "Siraj"],
            "answer": "Natarajan"
        },
        {
            "question": "Which spinner is famous for the carrom ball and mankad?",
            "options": ["Jadeja", "Ravichandran Ashwin", "Chahal", "Kuldeep"],
            "answer": "Ravichandran Ashwin"
        },
        {
            "question": "Who is called 'Sir Jadeja'?",
            "options": ["Hardik Pandya", "Ashwin", "Ravindra Jadeja", "Axar Patel"],
            "answer": "Ravindra Jadeja"
        },
        {
            "question": "Who played the match-winning knock at the Gabba in 2021?",
            "options": ["Rishabh Pant", "Gill", "Rahane", "Pujara"],
            "answer": "Rishabh Pant"
        }
        ]
    
    score = 0
    
    for i, q in enumerate(quiz):
        st.subheader(f"Q{i+1}.{q['question']}")
        selected = st.radio("Select your answer:",
                            q["options"], key=f"q{i}")
        if selected == q["answer"]:
            score += 1
    if st.button("✅ Submit Quiz"):
        st.success(f"Your score : {score}/{len(quiz)}")

        # Perfect score celebration
        if score == len(quiz):
            # Animation
            st.balloons()
            st.markdown("<h1 style='text-align:center;'> 🏆 PPERFECT SCORE 🏆 </h1>",unsafe_allow_html=True)
        placeholder = st.empty()
        for i in range(6):
            placeholder.markdown(
                "<h1 style=text-align:center;> 🎉🎉🎉🎉🎉🎉 </h1>",unsafe_allow_html=True
            )
            time.sleep(0.4)
            placeholder.empty()       
    # Contact page
elif page == "Contact":
    set_bg()
    st.title("📞 Contact us")
    st.write("Feel free to reach out using the form below if you have any queries")
    
    # Contact form fields
    name = st.text_input("Name*")
    email_id = st.text_input("Email-id*")
    mobile_number = st.text_input("Mobile Number*")
    message = st.text_input("Description")
    
    if st.button("Submit"):
        if name and email_id and message:
            st.success("✅ Your request sent successfully ! Soon you reach the replay")
        else:
            st.error("❌ Please fill all the Fields")
    
    st.subheader("Contact Details")

    # Bank Contact details
    st.write("📲 Mobile : +91 9385365443")
    st.write("☎ Landline : 044-123456")
    st.write("📧 Email-id : babumani429@gmail.com")


    st.write("🌐 website : www.yrindiancricketerimageclassification.com")




