import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd

st.set_page_config(
    page_title='HR Analysis Rport',
    layout="wide",
    initial_sidebar_state="expanded",
)

tab1, tab2 = st.tabs(["Podstawowa analiza", "Graf umijętności"])
col1, col2 = st.columns([1, 1])

with st.sidebar:
    st.markdown("Welcome in Report")

with tab1:
    with col2:
        st.markdown('#')
        st.markdown('#')
        st.markdown('#')
        st.markdown('#')

        st.markdown(
            """<style>
        .big-font {
        font-size:500px !important;
        }
        </style> <center> Porównanie umijętności kandydatów </center>""", unsafe_allow_html=True)
        df = pd.read_csv('dane.csv', delimiter=';')
        st.bar_chart(df, x="Kandydat", y=["Git [%]", "Java [%]", "Docker [%]"])

        st.markdown('#')
        st.markdown('#')
        st.markdown('#')
        st.markdown('#')

    with col1:
        st.markdown('#')
        st.markdown('#')
        st.markdown('#')
        st.markdown('#')

        st.area_chart(df, x="Kandydat", y=["Git [%]", "Java [%]", "Docker [%]"])

    with col1:
        st.markdown('#')

        df = pd.read_csv('dane.csv', delimiter=';')

        st.markdown(
            """<style>
        .big-font {
        font-size:500px !important;
        }
        </style> <center> Tabela umijętności kandydatów </center>""", unsafe_allow_html=True)

        st.table(df)

with tab2:
    nodes = []
    edges = []

    nodes.append(Node(id="Candidate 1",
                      label="jan Kowalski",
                      size=25,
                      shape="circularImage",
                      image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png"))

    nodes.append(Node(id="git",
                      label="GIT",
                      size=25,
                      shape="circularImage",
                      image="https://www.programujodpodstaw.pl/wp-content/uploads/2022/01/Git-Icon-1788C.png"))

    nodes.append(Node(id="Java",
                      label="Java",
                      size=40,
                      shape="circularImage",
                      image="https://www.shareicon.net/data/128x128/2016/07/06/106572_java_512x512.png"))

    nodes.append(Node(id="Docker",
                      label="Docker",
                      size=25,
                      shape="circularImage",
                      image="https://www.svgrepo.com/show/349342/docker.svg"))

    nodes.append(Node(id="Java2",
                      label="Java",
                      size=25,
                      shape="circularImage",
                      image="https://www.shareicon.net/data/128x128/2016/07/06/106572_java_512x512.png"))

    nodes.append(Node(id="Candidate 2",
                      label="Jerzy Maślana",
                      size=25,
                      shape="circularImage",
                      image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png"))

    nodes.append(Node(id="git2",
                      label="GIT",
                      size=40,
                      shape="circularImage",
                      image="https://www.programujodpodstaw.pl/wp-content/uploads/2022/01/Git-Icon-1788C.png"))

    edges.append(Edge(source="Candidate 1",
                      label="works",
                      target="git2",
                      # **kwargs
                      )
                 )

    edges.append(Edge(source="Candidate 1",
                      label="works",
                      target="Docker",
                      # **kwargs
                      )
                 )

    edges.append(Edge(source="Candidate 2",
                      label="works",
                      target="git",
                      # **kwargs
                      )
                 )

    edges.append(Edge(source="Candidate 1",
                      label="works ",
                      target="Java",
                      # **kwargs
                      )
                 )

    edges.append(Edge(source="Candidate 2",
                      label="works ",
                      target="Java2",
                      # **kwargs
                      )
                 )

    config = Config(width=1000,
                    height=1000,
                    directed=True,
                    physics=True,
                    hierarchical=True,

                    # **kwargs
                    )

    return_value = agraph(nodes=nodes,
                          edges=edges,
                          config=config)


