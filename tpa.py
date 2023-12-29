# These lines import necessary libraries for data manipulation, visualization, and machine learning.
import pandas as pd
import numpy as np
import streamlit as st

# Imports specific functionalities from scikit-learn needed for encoding data, splitting it, training a model, and evaluating it.
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Loads the telecom dataset into a DataFrame called 't'.
t = pd.read_csv("telecomdataset.csv")



# Drops any rows with missing values to ensure the quality of the data for analysis.
t= t.dropna()

# Initializes a dictionary to hold state abbreviations to unique number mappings.
state_to_number = {}

state_abbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Maps each state abbreviation to a unique number starting from 1.
for i, state_abbreviation in enumerate(state_abbreviations):
    state_to_number[state_abbreviation] = i + 1  # Adding 1 to start numbering from 1 (optional)

state_abbreviation_to_convert = "TX"  # Replace with the state abbreviation you want to convert
if state_abbreviation_to_convert in state_to_number:
    state_number = state_to_number[state_abbreviation_to_convert]
    print(f"{state_abbreviation_to_convert} is assigned the number {state_number}")
else:
    print(f"{state_abbreviation_to_convert} not found in the mapping")



state_numbers_to_abbreviations = [(number, abbreviation) for abbreviation, number in state_to_number.items()]

state_numbers_to_abbreviations.sort()

for state_number, state_abbreviation in state_numbers_to_abbreviations:
    print(f"{state_number}: {state_abbreviation}")




# Encodes categorical string variables into a numeric format suitable for modeling.
label_encoder = LabelEncoder()
for col in t.columns:
    if t[col].dtype == 'object':
        t[col] = label_encoder.fit_transform(t[col])


# Creates a new binary column 'churn1' indicating churn status.
t['churn1'] = np.where(t['churn'] == 1, 1, 0)

# Removes the original 'churn' column after encoding it.
t = t.drop(columns=['churn'])

state_abbreviation_to_convert = "AZ"  # Replace with the state abbreviation you want to convert
if state_abbreviation_to_convert in state_to_number:
    state_number = state_to_number[state_abbreviation_to_convert]
    print(f"{state_abbreviation_to_convert} is assigned the number {state_number}")
else:
    print(f"{state_abbreviation_to_convert} not found in the mapping")



# Prepares the feature matrix (X) and target vector (y), then splits them into training and testing sets.

X = t.drop(columns=['churn1'])
y = t['churn1']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3125)

# Prepares the feature matrix (X) and target vector (y), then splits them into training and testing sets.

clf = RandomForestClassifier(random_state=3125)
clf.fit(X_train, y_train)

# # Uses the trained classifier to make predictions on the test set.
# y_pred = clf.predict(X_test)




logo_url = "https://github.com/justinbrooks2552/telecom/raw/main/Logo.JPG"

col1, col2, col3 = st.columns([1,2,1])

with col2: 
    st.image(logo_url, use_container_width=True)


st.markdown(
    '<h1 style="text-align: center;">Telecom Customer Churn Rate</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<h4 style="text-align: center;">*For Internal Use Only*</h4>',
    unsafe_allow_html=True,
)



# List of state abbreviations
state_abbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
                       "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                       "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                       "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                       "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]



# # Increase font size with HTML and inline CSS
# st.markdown("""
#     <style>
#     .big-font {
#         font-size:16px !important;
#     }
#     </style>
#     <div class='big-font'>
#         Select Customer State
#     </div>
#     """, unsafe_allow_html=True)

# # Rest of your Streamlit app code


# Increase font size and make text bold with HTML and inline CSS
st.markdown("""
    <style>
    .big-and-bold-font {
        font-size:16px !important;
        font-weight: bold !important;
    }
    </style>
    <div class='big-and-bold-font'>
        Select Customer State
    </div>
    """, unsafe_allow_html=True)

# Rest of your Streamlit app code


# def main():
#     st.title('Select Your State Abbreviation')

stateoption = st.selectbox(
    '',
        state_abbreviations, 
        index=None, 
        placeholder="Select a state abbreviation..."
    )

st.write('***Customer lives in:***', stateoption)

# If-else statements for each state abbreviation
if stateoption == 'AL':
    stateoption = 1
elif stateoption == 'AK':
    stateoption = 2
elif stateoption == 'AZ':
    stateoption = 3
elif stateoption == 'AR':
    stateoption = 4
elif stateoption == 'CA':
    stateoption = 5
elif stateoption == 'CO':
    stateoption = 6
elif stateoption == 'CT':
    stateoption = 7
elif stateoption == 'DE':
    stateoption = 8
elif stateoption == 'FL':
    stateoption = 9
elif stateoption == 'GA':
    stateoption = 10
elif stateoption == 'HI':
    stateoption = 11
elif stateoption == 'ID':
    stateoption = 12
elif stateoption == 'IL':
    stateoption = 13
elif stateoption == 'IN':
    stateoption = 14
elif stateoption == 'IA':
    stateoption = 15
elif stateoption == 'KS':
    stateoption = 16
elif stateoption == 'KY':
    stateoption = 17
elif stateoption == 'LA':
    stateoption = 18
elif stateoption == 'ME':
    stateoption = 19
elif stateoption == 'MD':
    stateoption = 20
elif stateoption == 'MA':
    stateoption = 21
elif stateoption == 'MI':
    stateoption = 22
elif stateoption == 'MN':
    stateoption = 23
elif stateoption == 'MS':
    stateoption = 24
elif stateoption == 'MO':
    stateoption = 25
elif stateoption == 'MT':
    stateoption = 26
elif stateoption == 'NE':
    stateoption = 27
elif stateoption == 'NV':
    stateoption = 28
elif stateoption == 'NH':
    stateoption = 29
elif stateoption == 'NJ':
    stateoption = 30
elif stateoption == 'NM':
    stateoption = 31
elif stateoption == 'NY':
    stateoption = 32
elif stateoption == 'NC':
    stateoption = 33
elif stateoption == 'ND':
    stateoption = 34
elif stateoption == 'OH':
    stateoption = 35
elif stateoption == 'OK':
    stateoption = 36
elif stateoption == 'OR':
    stateoption = 37
elif stateoption == 'PA':
    stateoption = 38
elif stateoption == 'RI':
    stateoption = 39
elif stateoption == 'SC':
    stateoption = 40
elif stateoption == 'SD':
    stateoption = 41
elif stateoption == 'TN':
    stateoption = 42
elif stateoption == 'TX':
    stateoption = 43
elif stateoption == 'UT':
    stateoption = 44
elif stateoption == 'VT':
    stateoption = 45
elif stateoption == 'VA':
    stateoption = 46
elif stateoption == 'WA':
    stateoption = 47
elif stateoption == 'WV':
    stateoption = 48
elif stateoption == 'WI':
    stateoption = 49
elif stateoption == 'WY':
    stateoption = 50
else:
    st.write('') #**Please select a state abbreviation from the list.** Optional formatting text

st.divider()

accountlength = st.number_input("How long have they been a customer?", value=None, placeholder="Type a number...")
st.write('**Loyal Customer for**', accountlength, '**months**')


# Get unique 'accountlength' values and sort them
unique_account_lengths = sorted(t['accountlength'].unique())


# Looping through each possible account length
for length in unique_account_lengths:
    if accountlength == length:
       # st.write(f"You have selected an account length of {length}")
        break  # Exit the loop once the right account length is found


areacode = st.selectbox("Select Area Code Below", 
                        ('408', '415', '510'), index=None, placeholder="Select Area Code Below...")
st.write('**Customer Area Code is**', areacode)

if areacode == 408:
    areacode = 408
elif areacode == 415:
    areacode = 415
else: 
    areacode = 510


internationalplan = st.radio(
    "Does Customer Have International Plan?",
    ["Yes", "No"], index=None,
    )
if internationalplan =="Yes":
    st.write('***International Customer***')
else:
    st.write("***Not an International Customer***")

if internationalplan== "Yes":
    internationalplan= 1
else:
    internationalplan= 0


voicemailplan = st.radio(
    "**Does Customer Have Voicemail Plan?**",
    ["Yes", "No"], index=None
    )
if voicemailplan =="Yes":
    st.write('***Customer has Voicemail Plan***')
else:
    st.write("***Customer does not have Voicemail Plan***")

if voicemailplan== "Yes":
    voicemailplan= 1
else:
    voicemailplan= 0



# numbervmailmessages = st.number_input("How many voicemail messages does the customer have?", value=None, placeholder="Type a number...")
# st.write('**Customer has**', numbervmailmessages, '**voicemail messages**')


# # Get unique 'accountlength' values and sort them
# unique_number_vmail_messages = sorted(t['numbervmailmessages'].unique())


# # Looping through each possible vmails
# for vmail in unique_number_vmail_messages:
#     if numbervmailmessages == vmail:
#         break  # Exit the loop once the right account length is found
         

# # totaldayminutes = st.number_input('Total Day Minutes', min_value=0.0, max_value= 240.0, step=0.1)

# # st.write('Total Day Minutes Used:', totaldayminutes)


# totaldayminutes = st.number_input('Total Day Minutes', min_value=0.0, max_value=240.0, step=0.1)

# # Round the input to 1 decimal place
# totaldayminutes_rounded = round(totaldayminutes, 1)

# # Display the rounded value
# st.write(f'Total Day Minutes: {totaldayminutes_rounded}')


numbervmailmessages = st.number_input(
    'Input # of Customer Voicemails...', min_value=0, max_value=99, step= 1, format=None)
st.write('***Customer has*** ', numbervmailmessages, "***voicemails***")

st.divider()
totaldayminutes = st.number_input(
    'Input Total Day Minutes for Customer...', min_value=0.0, max_value=480.0, step= .1, format=None)
st.write('***Total Day Minutes used:*** ', totaldayminutes)

totaldaycalls = st.number_input(
    'Input Total Number of Calls Customer Made During Day Period...', min_value=0, max_value=4000, step= 1, format=None)
st.write('***Total Calls Made During Day Period:*** ', totaldayminutes)


totaldaycharge = st.number_input('Total Day Charge', min_value=0.00, max_value=240.00, step=0.01)
totaldaycharges_rounded = round(totaldaycharge, 2)
st.write(f'**Total Day Charge: ${totaldaycharges_rounded}**')

st.divider()

totaleveningminutes = st.number_input(
    'Input Total Evening Minutes for Customer...', min_value=0.0, max_value=480.0, step= .1, format=None)
st.write('***Total Evening Minutes used:*** ', totaleveningminutes)

totaleveningcalls = st.number_input(
    'Input Total Number of Calls Customer Made During Evening Period...', min_value=0, max_value=4000, step= 1, format=None)
st.write('***Total Calls Made During Evening Period:*** ', totaleveningcalls)


totaleveningcharge = st.number_input('Total Evening Charge', min_value=0.00, max_value=240.00, step=0.01)
totaleveningcharges_rounded = round(totaleveningcharge, 2)
st.write(f'Total Day Charge: ${totaleveningcharges_rounded}')

st.divider()

#total night
totalnightminutes = st.number_input(
    'Input Total Night Minutes for Customer...', min_value=0.0, max_value=480.0, step= .1, format=None)
st.write('***Total Night Minutes used:*** ', totalnightminutes)

totalnightcalls = st.number_input(
    'Input Total Number of Calls Customer Made During Night Period...', min_value=0, max_value=4000, step= 1, format=None)
st.write('***Total Calls Made During Night Period:*** ', totalnightcalls)


totalnightcharge = st.number_input('Total Night Charge', min_value=0.00, max_value=240.00, step=0.01)
totalnightcharges_rounded = round(totalnightcharge, 2)
st.write(f'Total Night Charge: ${totalnightcharges_rounded}')

st.divider()

#total international
totalinterminutes = st.number_input(
    'Input Total International Minutes for Customer...', min_value=0.0, max_value=480.0, step= .1, format=None)
st.write('***Total International Minutes used:*** ', totalinterminutes)

totalintercalls = st.number_input(
    'Input Total Number of Internatinoal Calls Made...', min_value=0, max_value=4000, step= 1, format=None)
st.write('***Total International Calls Made:*** ', totalintercalls)


totalintercharge = st.number_input('Total International Charge', min_value=0.00, max_value=240.00, step=0.01)
totalintercharges_rounded = round(totalintercharge, 2)
st.write(f'Total International Charge: ${totalintercharges_rounded}')



customerservicecalls = st.selectbox("Select Number of Customer Service Calls?",
                        ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'),
                        index=None, 
                        placeholder="Select Number of Customer Service Calls Made by Customer...")

st.write('**Customer Service Calls Made:**', customerservicecalls)



# Prepares a new dataset 'newdata' for making churn predictions.
newdata = pd.DataFrame({
    "state" : [stateoption],
    "accountlength" : [accountlength],
    "areacode" : [areacode],
    "internationalplan" : [internationalplan],
    "voicemailplan" : [voicemailplan],
    "numbervmailmessages" : [numbervmailmessages],
    "totaldayminutes" : [totaldayminutes],
    "totaldaycalls"  : [totaldaycalls],
    "totaldaycharge" : [totaldaycharge],
    "totaleveningminutes" : [totaleveningminutes],
    "totaleveningcalls" : [totaleveningcalls],
    "totaleveningcharge" : [totaleveningcharge],
    "totalnightminutes" : [totalnightminutes],
    "totalnightcalls" : [totalnightcalls],
    "totalnightcharge" : [totalnightcharge],
    "totalinterminutes" : [totalinterminutes],
    "totalintercalls" : [totalintercalls],
    "totalintercharge" : [totalintercharge],
    "customerservicecalls" : [customerservicecalls]      
})
newdata['churn']=clf.predict(newdata)

if st.button('Determine Churn', key='churn', type='primary'):
    prediction = newdata['churn']
    if any(prediction == 1):
        st.write('***Start Customer Retention Workflow***')
    else:
        st.write('***Thank for being a loyal customer, start customer loyalty workflow***')

