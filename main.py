import streamlit as st
import pandas as pd
import datetime
from streamlit_elements import elements, mui, html
st.set_page_config(layout="wide")

df = pd.DataFrame([
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 08:30:00'),
        'Fuel': 40,
        'IsRefuel': False,
        'Refueled': 0,
        'Location': 'Al Qazemia',
        'Km': 1000
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 09:30:00'),
        'Fuel': 30,
        'IsRefuel': False,
        'Refueled': 0,
        'Location': 'Abushagra',
        'Km': 1030
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 10:30:00'),
        'Fuel': 60,
        'IsRefuel': True,
        'Refueled': 30,
        'Location': 'Al Nahda',
        'Km': 1080

    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 11:30:00'),
        'Fuel': 50,
        'IsRefuel': False,
        'Refueled': 0,
        'Location': 'Al Nahda',
        'Km': 1100
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 12:30:00'),
        'Fuel': 30,
        'IsRefuel': False,
        'Refueled': 0,
        'Location': 'Al Nahda',
        'Km': 1150
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-02 08:30:00'),
        'Fuel': 30,
        'IsRefuel': False,
        'Refueled': 0,
        'Location': 'Al Qazemia',
        'Km': 1220
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-02 09:30:00'),
        'Fuel': 10,
        'IsRefuel': False,
        'Refueled': 0,
        'Location': 'Abushagra',
        'Km': 1320
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-02 10:30:00'),
        'Fuel': 60,
        'IsRefuel': True,
        'Refueled': 50,
        'Location': 'Al Nahda',
        'Km': 1350
    },

])

df_n = pd.DataFrame([
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 12:30:00'),
        'IdleTime': 60,
        'IsEngineOn': True

    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 16:30:00'),
        'IdleTime': 180,
        'IsEngineOn': False
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-01 18:30:00'),
        'IdleTime': 30,
        'IsEngineOn': True
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-02 13:45:00'),
        'IdleTime': 80,
        'IsEngineOn': True

    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-02 16:00:00'),
        'IdleTime': 50,
        'IsEngineOn': True
    },
    {
        'Vehicle': 'Nidhin Car',
        'DateTime': datetime.datetime.fromisoformat('2024-01-02 20:30:00'),
        'IdleTime': 30,
        'IsEngineOn': False
    }
])

col1, col2 = st.columns(2)



with col1:
   with st.container(border=True):
        st.title("Daily Fuel Usage Analysis")
        d = st.date_input("Select Date", datetime.date(2024, 1, 2),key="s1")
        dt= datetime.datetime.fromordinal(d.toordinal())
        dtn=dt+datetime.timedelta(days=1)
        st.line_chart(data=(df[df.DateTime >= dt])[df.DateTime < dtn], x='DateTime', y='Fuel', color=None, width=0, height=0, use_container_width=True)
        st.divider()
        totalRefueled=(df[df.DateTime >= dt])[df.DateTime < dtn]["Refueled"].sum()
        totalRefueledYes = (df[df.DateTime >= dt-datetime.timedelta(days=1)])[df.DateTime < dt]["Refueled"].sum()
        c1,c2,c3 = st.columns(3)
        with c1:
            st.metric(label="Refueled", value=totalRefueled, delta=float(totalRefueled-totalRefueledYes))
        totalKm= (df[df.DateTime >= dt])[df.DateTime < dtn]["Km"].max()-(df[df.DateTime >= dt])[df.DateTime < dtn]["Km"].min()
        totalKmyes = (df[df.DateTime >= dt-datetime.timedelta(days=1)])[df.DateTime < dt]["Km"].max() - (df[df.DateTime >= dt-datetime.timedelta(days=1)])[df.DateTime < dt][
            "Km"].min()
        with c2:
            st.metric(label="Distance(kms)", value=totalKm, delta=float(totalKm - totalKmyes))
        totalCost = totalKm*(2.80/8)
        totalCostyes = totalKmyes*(2.80/8)
        with c3:
            st.metric(label="Total Cost(Dhms)", value=totalCost, delta=float(totalCost - totalCostyes))

with col2:
   with st.container(border=True):
        st.title("Daily Idle Time Analysis")
        dy = st.date_input("Select Date", datetime.date(2024, 1, 2),key="s2")
        dty= datetime.datetime.fromordinal(dy.toordinal())
        dtny=dty+datetime.timedelta(days=1)
        st.bar_chart(data=(df_n[df_n.DateTime >= dty])[df_n.DateTime < dtny], x='DateTime', y='IdleTime', color=None, width=0, height=0, use_container_width=True)
        st.divider()
        totalIdle = (df_n[df_n.DateTime >= dty])[df_n.DateTime < dtny]["IdleTime"].sum()
        totalIdleYes = (df_n[df_n.DateTime >= dty - datetime.timedelta(days=1)])[df_n.DateTime < dty]["IdleTime"].sum()
        df_nn=df_n[df_n.IsEngineOn==True]
        totalIdleE = (df_nn[df_nn.DateTime >= dty])[df_nn.DateTime < dtny]["IdleTime"].sum()
        totalIdleYesE = (df_nn[df_nn.DateTime >= dty - datetime.timedelta(days=1)])[df_nn.DateTime < dty]["IdleTime"].sum()
        totalIdleCost=totalIdle*(2.89/60)
        totalIdleCostY = totalIdleYes * (2.89 / 60)
        c1, c2, c3 = st.columns(3)
        with c1:
            st.metric(label="Total Idle Time(mins)", value=totalIdle, delta=float(totalIdle - totalIdleYes))
        with c2:
            st.metric(label="Total Idle Time Engine On(mins)", value=totalIdleE, delta=float(totalIdleE - totalIdleYesE))
        with c3:
            st.metric(label="Total Idle Time Cost(Dhms)", value=round(totalIdleCost,2), delta=round(float(totalIdleCost - totalIdleCostY),2))
