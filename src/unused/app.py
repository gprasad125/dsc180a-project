import streamlit as st
import pandas as pd
import numpy as np
import math
import plotly.express as px
import plotly.graph_objects as go

# Load Data
@st.cache(allow_output_mutation=True)
def loadData(url):

    return pd.read_csv(url)
url = "../data/out/tweets_cleaned.csv"
df = loadData(url)

major_parties = ["Democrat", "Republican"]
df_major = df[df["term_partisanship"].isin(major_parties)]

dem_age = int(df[df["term_partisanship"] == "Democrat"]["year"].mean())
rep_age = int(df[df["term_partisanship"] == "Republican"]["year"].mean())

# Make Visualizations 
bin_width= 10
nbins_dems = math.ceil((df_major["year"].max() - df_major["year"].min()) / bin_width)

fig_1 = px.histogram(df_major, x = "year", nbins = nbins_dems, color = "term_partisanship", title = "Distribution of Birth Years for Congressional Reps. From the Two Major Parties", color_discrete_map={"Republican":"#da4868", "Democrat":"#0096FF"})

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

top_ten = df["term_state"].value_counts()[0:10].index
top_ten_df = df[df["term_state"].isin(top_ten)]
top_ten_df.dropna(inplace = True)
tt_pv = pd.pivot_table(top_ten_df, index = "country", columns = "term_state", values = "SentimentScore", aggfunc = np.mean)
fig_3 = px.imshow(tt_pv)

scores = df[df["SentimentScore"] <= 5.0]
scores_by_age = pd.DataFrame(scores.groupby(["SentimentScore", "country"])["age_when_posted"].mean()).reset_index()
fig_4 = px.scatter(scores_by_age, x = "SentimentScore", y = "age_when_posted", color = "country")

fig_4.update_traces(marker=dict(size=18,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))

# Change the bar mode
fig_2.update_layout(title_text = "# of Tweets For Each Country By State", title_x = 0.5, barmode='group')


st.header("DSC180A Initial EDA")
st.subheader("Gokul Prasad")
st.write("The dataframe:")
st.dataframe(df)

options = np.array(["Visualization 1", "Visualization 2", "Visualization 3", "Visualization 4"])

choice = st.selectbox(label = "Select a visualization", options=options)

if choice == "Visualization 1":
    st.header("Distribution of Birth Years Among Congress Members")
    st.plotly_chart(fig_1)
    st.write(
        "We can see that there is an overwhelming majority of Republicans in our dataset. We can also see that both parties skew fairly old, with the average birth year of Democrats being " + str(dem_age) + ", while Republicans are typically born in " + str(rep_age))
elif choice == "Visualization 2":
    st.header("Distribution of Country Mentions by State")
    st.plotly_chart(fig_2)
    st.write(
        "The results here are not too surprising, given the context of the dataset. China overwhelmingly dominates every state's Twitter mentions. However, there are a few interesting observations:"
    )

    obs = [
        "Politicians from the two biggest Democratic states (California & New York) differ on which non-China country they tweet about more. Californians tweet much more about Iran, while New Yorkers tweet more about Canada.", 
        "Only 6 of the top 10 most tweeted-from states voted Republican in the last presidential election, but Republicans appear in nearly far more entries in the dataset than Democrats"
    ]

    for i in obs:
        st.markdown("- " + i)
elif choice == "Visualization 3":
    st.header("Sentiment Heatmap of Top Ten States by Country")
    st.plotly_chart(fig_3)
    st.write(
        "The heatmap again shows expected results; however, note that the two states closest to Canada are the most negative in sentiment towards the country."
    )
elif choice == "Visualization 4":
    st.header("Distribution of Age at Tweet For Each Sentiment Score by Country")
    st.plotly_chart(fig_4)
    st.write(
        "We can see that for each country, the spread of sentiment scores by age are roughly similar. Outliers are genuine standouts in the data, and not reflective of the data wholly."
    )
