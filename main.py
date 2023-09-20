import streamlit as st
from PIL import Image
import pandas as pd

st.title("Irina Kovalenko")
st.subheader("_:blue[Data Science] graduate | :blue[NLP & Machine Learning] enthusiast_")
st.divider()

with st.sidebar:
    st.subheader("Contact")
    st.write(":telephone_receiver: +48 514 686 562 (WhatsApp)")
    st.write(":e-mail: iko905744@gmail.com")


    #Linkedin & Github icon redirecting to Linkedin account
    linkedin_url = "https://www.linkedin.com/in/irenakovalenko/"
    linkedin_logo = "https://windows.atsit.in/pl/wp-content/uploads/sites/21/2023/08/jak-dodac-logo-do-swojej-firmy-na-linkedin.jpg"
    github_url = "https://github.com/Irinakoli"
    github_logo = "https://allvectorlogo.com/img/2021/12/github-logo-vector.png"

    st.markdown(
        f"""
        <div style="display: flex; align-items: center;">
            <a href='{linkedin_url}' target='_blank'><img src='{linkedin_logo}' width='60' height='40' style="margin-right: 10px;"></a>
            <a href='{github_url}' target='_blank'><img src='{github_logo}' width='60' height='40'></a>
        </div>
        """,
        unsafe_allow_html=True
    )

    "---"

    st.subheader("**Languages**")
    st.write(":flag-ua:  native")
    st.write(":flag-ru:  native")
    st.write(":flag-pl:  native")
    st.write(":flag-gb:  full working proficiency")
    st.write(":flag-gr:  limited working proficiency")

    "---"

    st.subheader("**Skills**")

    skills = [{"name": "Research", "level": 5},
              {"name": "NLP", "level": 4},
              {"name" : "Machine Learning", "level" : 4},
              {"name": "Python", "level": 4},
              {"name": "Tableau & PowerBI", "level" : 3},
              {"name": "SQL", "level" : 2}
              ]

    bubble_style = 'style="display: inline-block; width: 20px; height: 20px; border-radius: 50%; margin-right: 5px;"'

    for skill in skills:
        skill_bubbles = "".join([f'<div class="skill-bubble-filled"></div>' if i < skill["level"] else f'<div class="skill-bubble-empty"></div>' for i in range(5)])
        st.markdown(f'<div class="skill-bubbles">{skill_bubbles}</div>', unsafe_allow_html=True)
        st.write(skill["name"])

    st.markdown(
    """
    <style>
    .skill-bubbles {
        display: flex;
        align-items: center;
        margin-bottom: 5px; /* Add spacing between skill bubbles */
    }
    .skill-bubble-filled {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: #007acc; /* Change color as needed */
        margin-right: 5px;
    }
    .skill-bubble-empty {
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background-color: #e0e0e0; /* Change color as needed */
        margin-right: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.subheader(":blue[**Education**] :books:")
with st.expander("**Data Science | Master programme at UMCS in Lublin (Poland) | 2021 - 2023**"):
    st.markdown("- _Python programming (Machine Learning projects) - pandas, scikit learn, matplotlib, plotly, seaborn_")
    st.markdown("- _Business Intelligence tools - Tableau, PowerBI_")
    st.markdown("- _basic R & SQL_")

with st.expander("**Information Architecture | Master programme at UMCS in Lublin (Poland) | 2020 - 2022**"):
    st.markdown("- _basic Hadoop & KNIME_")
    st.markdown(" - _Canva_")

with st.expander("**Tourism & Hospitality | Bachelor programme at UMCS in Lublin (Poland) | 2016 - 2019**"):
    st.markdown("- _customer service_")
    st.markdown("- _administration tasks & reservation systems_")

"---"

st.subheader(":blue[**Projects**]")

projects = [
    {
        "name": "The causes of lower life expectancy in US, comparing to other rich countries",
        "tools" : ["Tableau", "Wordpress", "Redmine"],
        "image": "life_expectancy.PNG",
        "github_link": "https://project.ds.net.pl/test-drive/",
    },
    {
        "name": "Sentiment analysis of Trip Advisor Reviews (university thesis project)",
        "tools" : [
            "LLMs : BERT, BERTopic, Ekman (for emotion detection)",
            "spacy",
            "parts of speech tagging",
            "topic modeling"
        ],
        "image": "sentiment_analysis_app.PNG",
        "streamlit_app_link": "https://irinakkoli-nlp-cy.streamlit.app/",
        "github_link": "https://github.com/Irinakoli/Irinakoli.github.io/blob/main/sentiment_analysis_Cyprus.ipynb",
    },

    {
        "name": "Bank churn prediction - Supervised Classification (Random Forest Classifier)",
        "tools" : ["scikit learn", "pandas", "seaborn", "plotly", "ALE", "Lime"],
        "image" : "churn_prediction.PNG",
        "streamlit_app_link" : "https://irinakkoli-bank-churn-prediction-app.streamlit.app/",
        "github_link": "https://github.com/Irinakoli/Irinakoli.github.io/blob/main/final_bank_churn%20(1).ipynb",

    }]


for project in projects:
    st.subheader(project["name"])
    st.image(project["image"], caption=", ".join(project["tools"]), use_column_width=True)
    st.markdown(f"**Tools:** {', '.join(project['tools'])}")

    # Check if Streamlit app link is available
    if "streamlit_app_link" in project:
        st.write(f"**Streamlit App:** [{project['name']}]({project['streamlit_app_link']})")

    # Check if GitHub link is available
    if "github_link" in project:
        st.write(f"**GitHub Repository:** [{project['name']}]({project['github_link']})")

    st.write("---")


"---"
st.subheader(":blue[**Experience**]")
with st.expander("**SUPPORT SPECIALIST**, Lingaro (Warsaw, Poland) | May 2022 - Dec 2022"):
    st.markdown("- research - market research, technical research in the field of NLP")
    st.markdown("- web scraping ecommerce reviews (BeautifulSoup, scrapy, UiPath studio)")
    st.markdown("- annotations of training dataset for Computer vision project (tool used - doccano)")
    st.markdown("- participating in dashboards' creation in PowerBI (logistic optimization project")

with st.expander("**TRAINEE**, Urban Yoga Lab (London (remote)) | May 2021 - June 2021"):
    st.markdown("- supporting the founder in market research regarding trends in hospitality, collaboration prospects etc.")
    st.markdown("- creating lists of networking and business events in hospitality")















