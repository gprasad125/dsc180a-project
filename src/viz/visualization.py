import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as io

def make_visuals(inpath):

    # read in file
    df = pd.read_csv(inpath)

    # Visualization 1: grouped barplot
    state_v_country = pd.crosstab(df["term_state"], df["country"])
    state_v_country["total"] = state_v_country["Canada"] + state_v_country["China"] + state_v_country["Iran"]
    state_v_country.reset_index(inplace = True)
    fig_1 = go.Figure(
        data=[
            go.Bar(name='Canada', x = state_v_country["term_state"], y = state_v_country["Canada"], yaxis='y', offsetgroup=1),
            go.Bar(name='China', x = state_v_country["term_state"], y = state_v_country["China"], yaxis='y', offsetgroup=2),
            go.Bar(name='Iran', x = state_v_country["term_state"], y = state_v_country["Iran"], yaxis='y', offsetgroup=3),
        ],
        layout={
            'yaxis': {'title': '# of Mentions by State'}
        },
    )

    fig_1.update_layout(title_text = "# of Tweets For Each Country By State", title_x = 0.5, barmode='group')

    # Visualization 2: Heatmap
    top_ten = df["term_state"].value_counts()[0:10].index
    top_ten_df = df[df["term_state"].isin(top_ten)]
    top_ten_df.dropna(inplace = True)
    tt_pv = pd.pivot_table(top_ten_df, index = "country", columns = "term_state", values = "score", aggfunc = np.mean)
    fig_2 = px.imshow(tt_pv)

    # Visualization 3: Scatter plot
    scores = df[df["score"] <= 5.0]
    scores_by_age = pd.DataFrame(scores.groupby(["score", "country"])["age_when_posted"].mean()).reset_index()
    fig_3 = px.scatter(scores_by_age, x = "score", y = "age_when_posted", color = "country")

    fig_3.update_traces(marker=dict(size=18,
                                  line=dict(width=2,
                                            color='DarkSlateGrey')),
                      selector=dict(mode='markers'))

    outpath = "data/visuals/"
    io.write_image(fig_1, outpath + 'fig1.png')
    io.write_image(fig_2, outpath + 'fig2.png')
    io.write_image(fig_3, outpath + 'fig3.png')
    
    
    return "success"
