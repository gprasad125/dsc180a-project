import streamlit as st
import pandas as pd
import numpy as np
import math
import plotly.express as px
import plotly.graph_objects as go
import cleaning as c
import importlib
importlib.reload(c)

# Load Data
@st.cache(allow_output_mutation=True)
def loadData(url):

    return pd.read_csv(url)
url = "../Data/sampleData.csv"
df = loadData(url)

# clean / edit columns
df["year"] = df["birth"].apply(c.get_year)
df["term_state"] = df["term_state"].apply(c.clean_state)

# Make Visualizations 
bin_width= 10
nbins = math.ceil((df["year"].max() - df["year"].min()) / bin_width)
fig = px.histogram(df, x = "year", nbins = nbins)

state_v_country = pd.crosstab(df["term_state"], df["country"])
state_v_country["total"] = state_v_country["Canada"] + state_v_country["China"] + state_v_country["Iran"]
state_v_country.reset_index(inplace = True)
fig_2 = go.Figure(
    data=[
        go.Bar(name='Canada', x = state_v_country["term_state"], y = state_v_country["Canada"], yaxis='y', offsetgroup=1),
        go.Bar(name='China', x = state_v_country["term_state"], y = state_v_country["China"], yaxis='y', offsetgroup=2),
        go.Bar(name='Iran', x = state_v_country["term_state"], y = state_v_country["Iran"], yaxis='y', offsetgroup=3),
    ],
    layout={
        'yaxis': {'title': '# of Mentions by State'}
    },
)

# Change the bar mode
fig_2.update_layout(title_text = "# of Tweets For Each Country By State", title_x = 0.5, barmode='group')


st.header("DSC180A Initial EDA")
st.subheader("Gokul Prasad")
st.write("The dataframe:")
st.dataframe(df)

options = np.array(["Visualization 1", "Visualization 2", "Visualization 3"])

choice = st.selectbox(label = "Select a visualization", options=options)

if choice == "Visualization 1":
    st.write("Distribution of Birth Years Among Congressmen")
    st.plotly_chart(fig)
elif choice == "Visualization 2":
    st.plotly_chart(fig_2)

