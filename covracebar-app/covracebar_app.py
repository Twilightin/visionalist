

import streamlit as st

import plotly.graph_objects as go
from raceplotly.plots import barplot

import pandas as pd

cov=pd.read_csv('/covracebar-app/WHOcov_cleaned.csv',index_col=0)

cov['Date']=pd.to_datetime(cov['Date'])

cov.set_index('Date',inplace=True)

cov_monthly=cov.groupby('Country').resample('M').sum().reset_index()

clist=['United States of America', 'India', 'Brazil',
       'The United Kingdom', 'Russian Federation', 'Turkey', 'France',
       'Germany', 'Iran (Islamic Republic of)', 'Argentina', 'Spain',
       'Italy', 'Republic of Korea','China','Japan']


cov_disp=cov_monthly[cov_monthly['Country'].isin(clist)].copy()

cov_disp[cov_disp['Country']=='United States of America'].tail()

my_raceplot = barplot(cov_disp,  item_column='Country', value_column='Cumulative_cases', time_column='Date', top_entries=15)
my_raceplot.plot(title='COVID-19 Confirmed Cases', item_label = 'Top Country', value_label = 'Total Confirmed', frame_duration = 1000, date_format='%x')

fig1=my_raceplot.fig

fig1.update_layout(
    autosize=False,
    width=1200,
    height=800,
    margin=dict(
        l=50,
        r=50,
        b=100,
        t=100,
        pad=4
    )
)

# Plot!
st.plotly_chart(fig1)
