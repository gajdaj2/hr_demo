import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
from main import analysis

st.set_page_config(
    page_title='HR Analysis Raport',
    layout="wide",
    initial_sidebar_state="expanded",
)
keyword = st_tags(
    label='# Enter skills:',
    text='Press enter to add more',
    value=["Java"],
    suggestions=['Java', 'Python', 'C++', 'C#', 'C', 'JavaScript', 'PHP', 'Ruby', 'R', 'Go', 'Swift', 'SQL', 'Kotlin'],
    key="aljnf")
st.file_uploader("Upload Files", type=['pdf'])

option = st.selectbox(
    'How many resumes do you want to analyze?',
    ('1', '2', '3'))

check = st.button("Candidate Analysis")




if check:
    analysis()


