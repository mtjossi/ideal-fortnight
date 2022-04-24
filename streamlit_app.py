import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

import plotly.graph_objects as go


st.title('Pricing Models')
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;justify-content: center} </style>', unsafe_allow_html=True)
model_choice = st.radio("Select Models:", ['1', '2', '3', 'Suggested'])

ac = np.arange(1,50001)

# model_dict = {"1":"No discounts, but buy in packs of200"}

###################################1
###################################1
if model_choice == '1':
    st.subheader("Model 1 Assumptions")
    st.write("No discounts, and Actions are purchased in packs of 200")

    ppa = st.slider("Test Price per Action:", min_value=0.00, max_value=.1, value=0.030, step=0.005, key=1)
    max_cpa = st.number_input("Max Cost per Action", min_value=0.001, max_value=0.1, value=0.0054)
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
    cpa = np.linspace(0.0033, max_cpa, 50000)
    df_200_no['action_cost'] = cpa * df_200_no['actions']
    df_200_no['wa_cost'] = ((0.0088+0.005)+0.00185) * df_200_no['actions']
    df_200_no['total_cost'] = df_200_no['action_cost'] + df_200_no['wa_cost']
    df_200_no['profit'] = ((df_200_no['income'] - df_200_no['total_cost'])/df_200_no['income'])*100
    df_200_no['profit2'] = ((df_200_no['income'] - df_200_no['action_cost'])/df_200_no['income'])*100

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_200_no['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_200_no['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa*200:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")


    st.write("Displaying only first 10k actions")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['income'][:10000], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['total_cost'][:10000], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['profit'][:10000], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_200_no['actions'][:10000], y=df_200_no['profit2'][:10000], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
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
    df_1000_no['action_cost'] = cpa * df_1000_no['actions']
    df_1000_no['wa_cost'] = ((0.0088+0.005)+0.00185) * df_1000_no['actions']
    df_1000_no['total_cost'] = df_1000_no['action_cost'] + df_1000_no['wa_cost']
    df_1000_no['profit'] = ((df_1000_no['income'] - df_1000_no['total_cost'])/df_1000_no['income'])*100
    df_1000_no['profit2'] = ((df_1000_no['income'] - df_1000_no['action_cost'])/df_1000_no['income'])*100

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_1000_no['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_1000_no['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa2:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa2*1000:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")

    st.write("Displaying only first 10k actions")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['income'], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['total_cost'], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['profit'], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_1000_no['actions'], y=df_1000_no['profit2'], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig)

###################################2
###################################2
if model_choice == '2':
    st.subheader("Model 2 Assumptions")
    st.write("1) 10 x 200 Pack with 1 free 200 Pack")
    st.write("2) 1 x 1000 Pack with 1 free 200 Pack")

    ppa = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.03, step=0.005, key=3)
    max_cpa = st.number_input("Max Cost per Action", min_value=0.001, max_value=0.1, value=0.0054)
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
    cpa = np.linspace(0.0033, max_cpa, 50000)
    df_200_disc['action_cost'] = cpa * df_200_disc['actions']
    df_200_disc['wa_cost'] = ((0.0088+0.005)+0.00185) * df_200_disc['actions']
    df_200_disc['total_cost'] = df_200_disc['action_cost'] + df_200_disc['wa_cost']
    df_200_disc['profit'] = ((df_200_disc['income'] - df_200_disc['total_cost'])/df_200_disc['income'])*100
    df_200_disc['profit2'] = ((df_200_disc['income'] - df_200_disc['action_cost'])/df_200_disc['income'])*100

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_200_disc['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_200_disc['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa*200:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")

    st.write("Displaying only first 10k actions")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['income'][:10000], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['total_cost'][:10000], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['profit'][:10000], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_200_disc['actions'][:10000], y=df_200_disc['profit2'][:10000], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
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
            counter = 1

    
    df_1000_disc = pd.DataFrame({'actions':ac,
                  'income':income_list2})

    df_1000_disc['action_cost'] = cpa * df_1000_disc['actions']
    df_1000_disc['wa_cost'] = ((0.0088+0.005)+0.00185) * df_1000_disc['actions']
    df_1000_disc['total_cost'] = df_1000_disc['action_cost'] + df_1000_disc['wa_cost']
    df_1000_disc['profit'] = ((df_1000_disc['income'] - df_1000_disc['total_cost'])/df_1000_disc['income'])*100
    df_1000_disc['profit2'] = ((df_1000_disc['income'] - df_1000_disc['action_cost'])/df_1000_disc['income'])*100

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_1000_disc['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_1000_disc['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa2:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa2*1000:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['income'], name='income', mode='lines', line={'color':'blue'}))
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['total_cost'], name='total_cost', mode='lines', line={'color':'red'}))
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['profit'], name='profit', mode='lines', line={'color':'green'}))
    fig2.add_trace(go.Scatter(x=df_1000_disc['actions'], y=df_1000_disc['profit2'], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig2)

###################################3
###################################3
if model_choice == '3':
    st.subheader("Model 3 Assumptions")
    st.write("1) 10 x 200 Pack with 1 free 100 Pack")
    st.write("2) 1 x 1000 Pack with 1 free 100 Pack")

    
    ppa = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.03, step=0.005, key=5)
    max_cpa = st.number_input("Max Cost per Action", min_value=0.001, max_value=0.1, value=0.0054)
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
    cpa1 = np.linspace(0.0033, max_cpa, 50000)
    df_200_100['action_cost'] = cpa1[:47800] * df_200_100['actions']
    df_200_100['wa_cost'] = ((0.0088+0.005)+0.00185) * df_200_100['actions']
    df_200_100['total_cost'] = df_200_100['action_cost'] + df_200_100['wa_cost']
    df_200_100['profit'] = ((df_200_100['income'] - df_200_100['total_cost'])/df_200_100['income'])*100
    df_200_100['profit2'] = ((df_200_100['income'] - df_200_100['action_cost'])/df_200_100['income'])*100

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_200_100['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_200_100['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa*200:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")

    st.write("Displaying only first 10k actions")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['income'][:10000], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['total_cost'][:10000], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['profit'][:10000], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['profit2'][:10000], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
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
            counter = 1
    
    st.write(len(ac), len(income_list2))
    df_1000_100 = pd.DataFrame({'actions':ac[:45900],
                  'income':income_list2})

    cpa2 = np.linspace(0.0033, max_cpa, 50000)
    df_1000_100['action_cost'] = cpa2[:45900] * df_1000_100['actions']
    df_1000_100['wa_cost'] = ((0.0088+0.005)+0.00185) * df_1000_100['actions']
    df_1000_100['total_cost'] = df_1000_100['action_cost'] + df_1000_100['wa_cost']
    df_1000_100['profit'] = ((df_1000_100['income'] - df_1000_100['total_cost'])/df_1000_100['income'])*100
    df_1000_100['profit2'] = ((df_1000_100['income'] - df_1000_100['action_cost'])/df_1000_100['income'])*100

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_1000_100['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_1000_100['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa2:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa2*1000:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['income'], name='income', mode='lines', line={'color':'blue'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['total_cost'], name='total_cost', mode='lines', line={'color':'red'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['profit'], name='profit', mode='lines', line={'color':'green'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['profit2'], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig2)

###################################4
###################################4
if model_choice == 'Suggested':
    st.subheader("Suggested:")

    st.markdown("Shift cost of all third-party services to customer. \n"
    "- Average cost to send SMS: $0.076\n"
    f"- Average cost to send WhatsApp message: ${0.0088+0.005}\n"
    "- Average cost to send email: $0.00185\n\n"
    "So ask for upfront payment in blocks $10 for 3P service, which cannot be refunded, but no expiration date.\n"
    "- 1) 200 Pack @ $0.035/action. 1 stamp.\n"
    "- 2) 1000 Pack @ $0.035/action. 10 stamps."
    )

    image_ac = Image.open("./action_credits.png")
    image_ec = Image.open("./extra_credits.png")
    st.image(image=image_ac)
    st.image(image=image_ec)
    # ppa = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.035, step=0.005, key=7)
    # max_cpa = st.number_input("Max Cost per Action", min_value=0.001, max_value=0.1, value=0.0054)
    ppa = 0.035
    max_cpa=0.0054
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


    st.subheader("1) 200 Action Credit Pack")
    st.write("1 stamp")
    df_200_100 = pd.DataFrame({'actions':ac[:47800],
                  'income':income_list})

    cpa1 = np.linspace(0.0033, max_cpa, 50000)
    df_200_100['action_cost'] = cpa1[:47800] * df_200_100['actions']
    df_200_100['wa_cost'] = ((0.0088+0.005)+0.00185) * df_200_100['actions']
    df_200_100['total_cost'] = df_200_100['action_cost'] + df_200_100['wa_cost']
    df_200_100['profit'] = ((df_200_100['income'] - df_200_100['total_cost'])/df_200_100['income'])*100
    df_200_100['profit2'] = ((df_200_100['income'] - df_200_100['action_cost'])/df_200_100['income'])*100
    profit_3 = df_200_100.loc[2099, 'income'] - df_200_100.loc[2099, 'total_cost']
    profit_4 = df_200_100.loc[2099, 'income'] - df_200_100.loc[2099, 'action_cost']

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_200_100['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_200_100['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa*200:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")

    min_prof = np.round(df_200_100['profit'].tail(1).values[0], 2)
    max_prof = np.round(df_200_100['profit2'].tail(1).values[0], 2)
    st.success(f"Profit with Costs After 1st Free Pack: \${np.round(profit_3, 2)} / \${2000*ppa} = {(profit_3/(2000*ppa) *100):.2f}%")
    st.success(f"Profit without Costs After 1st Free Pack: \${np.round(profit_4, 2)} / \${2000*ppa} = {(profit_4/(2000*ppa) *100):.2f}%")

    st.write("Displaying only first 10k actions")
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['income'][:10000], name='income', mode='lines', line={'color':'blue'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['total_cost'][:10000], name='total_cost', mode='lines', line={'color':'red'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['profit'][:10000], name='profit', mode='lines', line={'color':'green'}))
    fig.add_trace(go.Scatter(x=df_200_100['actions'][:10000], y=df_200_100['profit2'][:10000], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig)


    st.subheader("2) 1000 Action Credit Pack")
    st.write("10 stamps")
    income_list2 = np.array([])
    # ppa2 = st.slider("Test Price per Action:", min_value=0.0, max_value=.1, value=0.035, step=0.005, key=8)
    ppa2 = 0.035
    income2 = ppa2*1000
    increment2 = ppa2*1000

    counter = 1
    for i in np.arange(200,50001, 100):
        if counter <= 10:
            for i in range(100):
                income_list2 = np.append(income_list2, income2)
    #         income += increment
            counter +=1
        else:
            for i in range(100):
                income_list2 = np.append(income_list2, income2)
            income2 += increment2
            counter = 1

    
    df_1000_100 = pd.DataFrame({'actions':ac[:49900],
                  'income':income_list2})
    cpa2 = np.linspace(0.0033, max_cpa, 50000)
    df_1000_100['action_cost'] = cpa2[:49900] * df_1000_100['actions']
    df_1000_100['wa_cost'] = ((0.0088+0.005)+0.00185) * df_1000_100['actions']
    df_1000_100['total_cost'] = df_1000_100['action_cost'] + df_1000_100['wa_cost']
    df_1000_100['profit'] = ((df_1000_100['income'] - df_1000_100['total_cost'])/df_1000_100['income'])*100
    df_1000_100['profit2'] = ((df_1000_100['income'] - df_1000_100['action_cost'])/df_1000_100['income'])*100
    profit_3_2 = df_1000_100.loc[1099, 'income'] - df_1000_100.loc[1099, 'total_cost']
    profit_4_2 = df_1000_100.loc[1099, 'income'] - df_1000_100.loc[1099, 'action_cost']

    a1, a2, a3, a4, a5 = st.columns(5)
    a1.metric('Profit with costs', value=f"{np.round(df_1000_100['profit'].tail(1).values[0], 2)}%")
    a2.metric('Profit without costs', value=f"{np.round(df_1000_100['profit2'].tail(1).values[0], 2)}%")
    a3.metric('Price per Action', value=f"{ppa2:.3f}")
    a4.metric('Max Cost per Action', value=f"{max_cpa:.4f}")
    a5.metric('Pack Price', value=f"${ppa2*1000:.2f}")
    st.write("Costs = Twilio WhatsApp (\$0.005 + \$0.0088) + SendInBlue email (\$0.00185)")

    min_prof2 = np.round(df_1000_100['profit'].tail(1).values[0], 2)
    max_prof2 = np.round(df_1000_100['profit2'].tail(1).values[0], 2)
    st.success(f"Profit with Costs After 1st Free Pack: \${np.round(profit_3_2, 2)} / \${1000*ppa2}  = {(profit_3_2/(1000*ppa2) *100):.2f}%")
    st.success(f"Profit without Costs After 1st Free Pack: \${np.round(profit_4_2, 2)} / \${1000*ppa2} = {(profit_4_2/(1000*ppa2) *100):.2f}%")

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['income'], name='income', mode='lines', line={'color':'blue'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['total_cost'], name='total_cost', mode='lines', line={'color':'red'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['profit'], name='profit', mode='lines', line={'color':'green'}))
    fig2.add_trace(go.Scatter(x=df_1000_100['actions'], y=df_1000_100['profit2'], name='profit w/o Costs', mode='lines', line={'color':'orange'}))
    st.plotly_chart(fig2)
