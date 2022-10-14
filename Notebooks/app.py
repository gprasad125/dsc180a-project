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
df["term_partisanship"] = df["term_partisanship"].apply(c.clean_state)
df["term_partisanship"].unique()

dems = df[df["term_partisanship"] == "Democrat"]
reps = df[df["term_partisanship"] == "Republican"]
othr = df[df["term_partisanship"].isin(["Independent", "Unknown"])]

# Make Visualizations 
bin_width= 10
nbins_dems = math.ceil((dems["year"].max() - dems["year"].min()) / bin_width)
nbins_reps = math.ceil((reps["year"].max() - reps["year"].min()) / bin_width)
nbins_othr = math.ceil((othr["year"].max() - othr["year"].min()) / bin_width)

m = px.histogram(df, x = "year", nbins = nbins_dems, color = "term_partisanship", title = "Distribution of Birth Years for Democratic Congressional Reps.")
dems_fig1 = px.histogram(dems, x = "year", nbins = nbins_dems, title = "Distribution of Birth Years for Democratic Congressional Reps.")
#reps_fig1 = px.histogram(reps, x = "year", nbins = nbins_reps, title = "Distribution of Birth Years for Republican Congressional Reps.", color = "red")
#othr_fig1 = px.histogram(othr, x = "year", nbins = nbins_othr)

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
    st.header("Distribution of Birth Years Among Congress Members")
    st.plotly_chart(m)
    #st.plotly_chart(reps_fig1)
   # st.plotly_chart(othr_fig1)
    st.write("We can see that very few Congresspersons are born post 1975, and that the majority of the Tweets in the dataset come from people born between 1950 - 1960.")
elif choice == "Visualization 2":
    st.header("Distribution of Country Mentions by State")
    st.plotly_chart(fig_2)

