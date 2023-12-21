import pandas as pd
import numpy as np
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

t = pd.read_csv("telecomdataset.csv")

t= t.dropna()

# Define a dictionary to map state abbreviations to numbers
state_to_number = {}

# Sample list of state abbreviations
state_abbreviations = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

# Assign a unique number to each state abbreviation
for i, state_abbreviation in enumerate(state_abbreviations):
    state_to_number[state_abbreviation] = i + 1  # Adding 1 to start numbering from 1 (optional)

# Test the mapping
state_abbreviation_to_convert = "TX"  # Replace with the state abbreviation you want to convert
if state_abbreviation_to_convert in state_to_number:
    state_number = state_to_number[state_abbreviation_to_convert]
    print(f"{state_abbreviation_to_convert} is assigned the number {state_number}")
else:
    print(f"{state_abbreviation_to_convert} not found in the mapping")

# You can now use the state_to_number dictionary to convert state abbreviations to numbers


# Create a list of tuples containing state numbers and state abbreviations
state_numbers_to_abbreviations = [(number, abbreviation) for abbreviation, number in state_to_number.items()]

# Sort the list by state number if needed
state_numbers_to_abbreviations.sort()

# Print the list
for state_number, state_abbreviation in state_numbers_to_abbreviations:
    print(f"{state_number}: {state_abbreviation}")


# Encode categorical features
label_encoder = LabelEncoder()
for col in t.columns:
    if t[col].dtype == 'object':
        t[col] = label_encoder.fit_transform(t[col])

tc= pd.DataFrame({
    "churn1":np.where(t["churn"]==1,1,0),
    })

t=pd.concat([t,tc], axis=1)

cd= "churn"
t.drop(columns=[cd], inplace=True)

# Split the data into training and testing sets
X = t.drop(columns=['churn1'])
y = t['churn1']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=3125)

# Standardize numeric features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Random Forest classifier
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)


st.markdown('# test')

#inputs
state
account length
international plan
voicemail plan
number of voice mail messages
customer service call