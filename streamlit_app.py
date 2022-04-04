import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import plotly.graph_objects as go


st.title('Pricing Models')

model_choice = st.radio("Select Models:", ['1', '2', '3', 'Suggested'])

ac = np.arange(1,50001)

model_dict = {"1":"No discounts, but buy in "}

if model_choice == '1':
    st.subheader("Model 1 Assumptions")
    st.write("No discounts, and Actions are purchased in packs of 200")

    ppa = st.slider("Test Price per Action:", min_value=0.00, max_value=.1, value=0.030, step=0.005, key=1)
    income_list = np.array([])
    income = ppa*200
    increment = ppa*200

    # counter = 1
    for i in np.arange(200,50001, 200):
    #     if counter < 10:
        for i in range(200):
            income_list = np.append(income_list, income)
        income += increment

    df_200_no = pd.DataFrame({'actions':ac,
                  'income':income_list})

    df_200_no['action_cost'] = 0.0033 * df_200_no['actions']
    df_200_no['wa_cost'] = 0.005 * df_200_no['actions']
    df_200_no['total_cost'] = df_200_no['action_cost'] + df_200_no['wa_cost']
    df_200_no['profit'] = ((df_200_no['income'] - df_200_no['total_cost'])/df_200_no['income'])*100
    df_200_no['profit2'] = ((df_200_no['income'] - df_200_no['action_cost'])/df_200_no['income'])*100

    a1, a2, a3 = st.columns(3)
    a1.metric('Profit with WhatsApp', value=f"{np.round(df_200_no['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without WhatsApp', value=f"{np.round(df_200_no['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa:.3f}")


    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['income'][:10000], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['total_cost'][:10000], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['profit'][:10000], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['profit2'][:10000], name='profit w/o WA', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig)


    st.write("No discounts, and Actions are purchased in packs of 1000")
    ppa2 = st.slider("Test Price per Action:", min_value=0.00, max_value=.1, value=0.030, step=0.005, key=2)
    income_list2 = np.array([])
    income2 = ppa2*1000
    increment2 = ppa2*1000

    # counter = 1
    for i in np.arange(1000,50001, 1000):
    #     if counter < 10:
        for i in range(1000):
            income_list2 = np.append(income_list2, income2)
        income2 += increment2


    df_1000_no = pd.DataFrame({'actions':ac,
                  'income':income_list2})

    df_1000_no['action_cost'] = 0.0033 * df_1000_no['actions']
    df_1000_no['wa_cost'] = 0.005 * df_1000_no['actions']
    df_1000_no['total_cost'] = df_1000_no['action_cost'] + df_1000_no['wa_cost']
    df_1000_no['profit'] = ((df_1000_no['income'] - df_1000_no['total_cost'])/df_1000_no['income'])*100
    df_1000_no['profit2'] = ((df_1000_no['income'] - df_1000_no['action_cost'])/df_1000_no['income'])*100

    a1, a2, a3 = st.columns(3)
    a1.metric('Profit with WhatsApp', value=f"{np.round(df_1000_no['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without WhatsApp', value=f"{np.round(df_1000_no['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa2:.3f}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['income'], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['total_cost'], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['profit'], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['profit2'], name='profit w/o WA', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig)

if model_choice == '2':
    st.subheader("Model 2 Assumptions")
    st.write("1) 10 x 200 Pack with 1 free 200 Pack")
    st.write("2) 1 x 1000 Pack with 1 free 200 Pack")

    ppa = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.03, step=0.005, key=3)
    income_list = np.array([])
    income = ppa*200
    increment = ppa*200


    counter = 1
    for i in np.arange(200,50001, 200):
        if counter < 10:
            for i in range(200):
                income_list = np.append(income_list, income)
            income += increment
            counter +=1
        else:
            for i in range(200):
                income_list = np.append(income_list, income)
            counter = 0
    st.subheader("1) 10 x 200 Pack with 1 free 200 Pack")
    df_200_disc = pd.DataFrame({'actions':ac,
                  'income':income_list})

    df_200_disc['action_cost'] = 0.0033 * df_200_disc['actions']
    df_200_disc['wa_cost'] = 0.005 * df_200_disc['actions']
    df_200_disc['total_cost'] = df_200_disc['action_cost'] + df_200_disc['wa_cost']
    df_200_disc['profit'] = ((df_200_disc['income'] - df_200_disc['total_cost'])/df_200_disc['income'])*100
    df_200_disc['profit2'] = ((df_200_disc['income'] - df_200_disc['action_cost'])/df_200_disc['income'])*100

    a1, a2, a3 = st.columns(3)
    a1.metric('Profit with WhatsApp', value=f"{np.round(df_200_disc['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without WhatsApp', value=f"{np.round(df_200_disc['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa:.3f}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['income'][:10000], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['total_cost'][:10000], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['profit'][:10000], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['profit2'][:10000], name='profit w/o WA', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig)


    st.subheader("2) 1 x 1000 Pack with 1 free 200 Pack")
    income_list2 = np.array([])
    ppa2 = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.03, step=0.005, key=4)
    income2 = ppa2*1000
    increment2 = ppa2*1000

    counter = 1
    for i in np.arange(200,50001, 200):
        if counter <= 5:
            for i in range(200):
                income_list2 = np.append(income_list2, income2)
    #         income += increment
            counter +=1
        else:
            for i in range(200):
                income_list2 = np.append(income_list2, income2)
            income2 += increment2
            counter = 0

    df_1000_disc = pd.DataFrame({'actions':ac,
                  'income':income_list2})

    df_1000_disc['action_cost'] = 0.0033 * df_1000_disc['actions']
    df_1000_disc['wa_cost'] = 0.005 * df_1000_disc['actions']
    df_1000_disc['total_cost'] = df_1000_disc['action_cost'] + df_1000_disc['wa_cost']
    df_1000_disc['profit'] = ((df_1000_disc['income'] - df_1000_disc['total_cost'])/df_1000_disc['income'])*100
    df_1000_disc['profit2'] = ((df_1000_disc['income'] - df_1000_disc['action_cost'])/df_1000_disc['income'])*100

    a1, a2, a3 = st.columns(3)
    a1.metric('Profit with WhatsApp', value=f"{np.round(df_1000_disc['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without WhatsApp', value=f"{np.round(df_1000_disc['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa2:.3f}")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['income'], name='income', mode='lines', line={'color':'blue'}))
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['total_cost'], name='total_cost', mode='lines', line={'color':'red'}))
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['profit'], name='profit', mode='lines', line={'color':'green'}))
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['profit2'], name='profit w/o WA', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig2)


if model_choice == '3':
    st.subheader("Model 3 Assumptions")
    st.write("1) 10 x 200 Pack with 1 free 100 Pack")
    st.write("2) 1 x 1000 Pack with 1 free 100 Pack")

    ppa = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.03, step=0.005, key=5)
    income_list = np.array([])
    income = ppa*200
    increment = ppa*200

    counter = 1
    for i in np.arange(200,50001, 200):
        if counter < 10:
            for i in range(200):
                income_list = np.append(income_list, income)
            income += increment
            counter +=1
        else:
            for i in range(100):
                income_list = np.append(income_list, income)
            counter = 0


    st.subheader("1) 10 x 200 Pack with 1 free 100 Pack")
    df_200_100 = pd.DataFrame({'actions':ac[:47800],
                  'income':income_list})

    df_200_100['action_cost'] = 0.0033 * df_200_100['actions']
    df_200_100['wa_cost'] = 0.005 * df_200_100['actions']
    df_200_100['total_cost'] = df_200_100['action_cost'] + df_200_100['wa_cost']
    df_200_100['profit'] = ((df_200_100['income'] - df_200_100['total_cost'])/df_200_100['income'])*100
    df_200_100['profit2'] = ((df_200_100['income'] - df_200_100['action_cost'])/df_200_100['income'])*100

    a1, a2, a3 = st.columns(3)
    a1.metric('Profit with WhatsApp', value=f"{np.round(df_200_100['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without WhatsApp', value=f"{np.round(df_200_100['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa:.3f}")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['income'][:10000], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['total_cost'][:10000], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['profit'][:10000], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['profit2'][:10000], name='profit w/o WA', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig)


    st.subheader("2) 1 x 1000 Pack with 1 free 100 Pack")
    income_list2 = np.array([])
    ppa2 = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.03, step=0.005, key=6)
    income2 = ppa2*1000
    increment2 = ppa2*1000

    counter = 1
    for i in np.arange(200,50001, 200):
        if counter <= 5:
            for i in range(200):
                income_list2 = np.append(income_list2, income2)
    #         income += increment
            counter +=1
        else:
            for i in range(100):
                income_list2 = np.append(income_list2, income2)
            income2 += increment2
            counter = 0

    df_1000_100 = pd.DataFrame({'actions':ac[:46500],
                  'income':income_list2})

    df_1000_100['action_cost'] = 0.0033 * df_1000_100['actions']
    df_1000_100['wa_cost'] = 0.005 * df_1000_100['actions']
    df_1000_100['total_cost'] = df_1000_100['action_cost'] + df_1000_100['wa_cost']
    df_1000_100['profit'] = ((df_1000_100['income'] - df_1000_100['total_cost'])/df_1000_100['income'])*100
    df_1000_100['profit2'] = ((df_1000_100['income'] - df_1000_100['action_cost'])/df_1000_100['income'])*100

    a1, a2, a3 = st.columns(3)
    a1.metric('Profit with WhatsApp', value=f"{np.round(df_1000_100['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without WhatsApp', value=f"{np.round(df_1000_100['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa2:.3f}")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['income'], name='income', mode='lines', line={'color':'blue'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['total_cost'], name='total_cost', mode='lines', line={'color':'red'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['profit'], name='profit', mode='lines', line={'color':'green'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['profit2'], name='profit w/o WA', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig2)


if model_choice == 'Suggested':
    st.subheader("Suggested:")
    st.write("1) 10 x 200 Pack with 1 free 100 Pack")
    st.write("2) 1 x 1000 Pack with 1 free 100 Pack")