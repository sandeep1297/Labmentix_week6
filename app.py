import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page configuration
st.set_page_config(layout="wide", page_title="Data Visualizations Dashboard")

st.title("Comprehensive Data Visualizations Dashboard")
st.write("This dashboard presents various insights derived from transaction, insurance, and user engagement data, displayed in a grid layout.")

# Define a dictionary to hold file paths with the .xlsx extension
file_paths = {
    '1.1': '1.1.xlsx',
    '1.2': '1.2.xlsx',
    '1.3': '1.3.xlsx',
    '2.1': '2.1.xlsx',
    '2.2': '2.2.xlsx',
    '3.1': '3.1.xlsx',
    '3.2': '3.2.xlsx',
    '4.1': '4.1.xlsx',
    '4.2': '4.2.xlsx',
    '5.1': '5.1.xlsx',
    '5.2': '5.2.xlsx',
    '6.1': '6.1.xlsx',
    '6.2': '6.2.xlsx',
    '7.1': '7.1.xlsx',
    '7.2': '7.2.xlsx',
    '8.1': '8.1.xlsx',
    '8.2': '8.2.xlsx',
    '9.1': '9.1.xlsx',
    '9.2': '9.2.xlsx'
}

# --- Plotting Functions (Now using pd.read_excel and updated tick labels) ---

def plot_1_1(file_path):
    df = pd.read_excel(file_path)

    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Plot 'total_transactions' by 'transaction_type'
    df_transactions = df.sort_values(by='total_transactions', ascending=False)
    axes[0].bar(df_transactions['transaction_type'], df_transactions['total_transactions'])
    axes[0].set_title('Total Transactions by Payment Instrument')
    axes[0].set_xlabel('Payment Instrument')
    axes[0].set_ylabel('Total Transactions')
    axes[0].ticklabel_format(style='plain', axis='y') # Disable scientific notation
    axes[0].set_xticklabels(df_transactions['transaction_type'], rotation=90, ha='right')

    # Plot 'total_transaction_amount' by 'transaction_type'
    df_amount = df.sort_values(by='total_transaction_amount', ascending=False)
    axes[1].bar(df_amount['transaction_type'], df_amount['total_transaction_amount'])
    axes[1].set_title('Total Transaction Amount by Payment Instrument')
    axes[1].set_xlabel('Payment Instrument')
    axes[1].set_ylabel('Total Transaction Amount')
    axes[1].ticklabel_format(style='plain', axis='y') # Disable scientific notation
    axes[1].set_xticklabels(df_amount['transaction_type'], rotation=90, ha='right')

    plt.tight_layout()
    return fig

def plot_1_2(file_path):
    df = pd.read_excel(file_path)
    fig, axes = plt.subplots(1, 2, figsize=(18, 6))

    # Plot 'total_transactions' by 'transaction_type'
    df_transactions = df.sort_values(by='total_transactions', ascending=False)
    axes[0].bar(df_transactions['transaction_type'], df_transactions['total_transactions'])
    axes[0].set_title('Total Transactions by Payment Instrument (e.g., Maharashtra, Recharge & bill payments)')
    axes[0].set_xlabel('Payment Instrument')
    axes[0].set_ylabel('Total Transactions')
    axes[0].ticklabel_format(style='plain', axis='y') # Disable scientific notation
    axes[0].set_xticklabels(df_transactions['transaction_type'], rotation=90, ha='right')

    # Plot 'total_transaction_amount' by 'transaction_type'
    df_amount = df.sort_values(by='total_transaction_amount', ascending=False)
    axes[1].bar(df_amount['transaction_type'], df_amount['total_transaction_amount'])
    axes[1].set_title('Total Transaction Amount by Payment Instrument (e.g., Maharashtra, Recharge & bill payments)')
    axes[1].set_xlabel('Payment Instrument')
    axes[1].set_ylabel('Total Transaction Amount')
    axes[1].ticklabel_format(style='plain', axis='y') # Disable scientific notation
    axes[1].set_xticklabels(df_amount['transaction_type'], rotation=90, ha='right')

    plt.tight_layout()
    return fig

def plot_1_3(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='total_transaction_amount', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_sorted['state'], df_sorted['total_transaction_amount'])
    ax.set_title('Top 5 States by Total Transaction Amount (2022)')
    ax.set_xlabel('State')
    ax.set_ylabel('Total Transaction Amount')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['state'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_2_1(file_path):
    df = pd.read_excel(file_path)
    
    df_agg = df.groupby('brand_name').agg({
        'total_registered_users': 'sum',
        'total_app_opens': 'sum'
    }).reset_index()

    df_agg = df_agg.sort_values(by='total_registered_users', ascending=False)

    fig, ax = plt.subplots(figsize=(12, 7))

    bar_width = 0.35
    index = range(len(df_agg['brand_name']))

    bar1 = ax.bar([i - bar_width/2 for i in index], df_agg['total_registered_users'], bar_width, label='Total Registered Users', color='skyblue')
    bar2 = ax.bar([i + bar_width/2 for i in index], df_agg['total_app_opens'], bar_width, label='Total App Opens', color='lightcoral')

    ax.set_title('Number of Registered Users and App Opens by Device Brand')
    ax.set_xlabel('Device Brand')
    ax.set_ylabel('Count')
    ax.set_xticks(index)
    ax.set_xticklabels(df_agg['brand_name'], rotation=90, ha='right') # Updated for consistency
    ax.ticklabel_format(style='plain', axis='y')
    ax.legend()
    plt.tight_layout()
    return fig

def plot_2_2(file_path):
    df = pd.read_excel(file_path)
    # Sort the data by 'total_users_by_brand' in descending order
    df_sorted = df.sort_values(by='total_users_by_brand', ascending=False)

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(10, 6)) # Changed to fig, ax
    ax.bar(df_sorted['brand_name'], df_sorted['total_users_by_brand']) # Changed to ax.bar
    ax.set_title('Total Registered Users by Device Brand (e.g., Karnataka, 2021)') # Changed to ax.set_title
    ax.set_xlabel('Device Brand') # Changed to ax.set_xlabel
    ax.set_ylabel('Total Registered Users') # Changed to ax.set_ylabel
    ax.set_xticklabels(df_sorted['brand_name'], rotation=90, ha='right') # Changed to set_xticklabels and rotation=90
    ax.ticklabel_format(style='plain', axis='y') # Changed to ax.ticklabel_format
    plt.tight_layout()
    # plt.savefig('user_engagement_by_brand.png') # Removed savefig
    # plt.show() # Removed show
    return fig # Return fig for Streamlit

def plot_3_1(file_path):
    df = pd.read_excel(file_path)
    # Combine 'year' and 'quarter' for the x-axis
    df['time_period'] = df['year'].astype(str) + ' Q' + df['quarter'].astype(str)

    # Create subplots for the two charts
    fig, axes = plt.subplots(2, 1, figsize=(12, 10))

    # Plot 'total_premium_count' over time
    axes[0].plot(df['time_period'], df['total_premium_count'], marker='o')
    axes[0].set_title('Total Insurance Premium Count Over Time')
    axes[0].set_xlabel('Year and Quarter')
    axes[0].set_ylabel('Total Premium Count')
    axes[0].ticklabel_format(style='plain', axis='y') # Disable scientific notation
    axes[0].set_xticklabels(df['time_period'], rotation=90, ha='right')

    # Plot 'total_premium_amount' over time
    axes[1].plot(df['time_period'], df['total_premium_amount'], marker='o', color='orange')
    axes[1].set_title('Total Insurance Premium Amount Over Time')
    axes[1].set_xlabel('Year and Quarter')
    axes[1].set_ylabel('Total Premium Amount')
    axes[1].ticklabel_format(style='plain', axis='y') # Disable scientific notation
    axes[1].set_xticklabels(df['time_period'], rotation=90, ha='right')

    plt.tight_layout()
    # plt.show() # Removed show
    return fig # Return fig for Streamlit

def plot_3_2(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='total_premium_amount', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_sorted['state'], df_sorted['total_premium_amount'])
    ax.set_title('Top 5 States by Total Insurance Premium Amount (Latest Year/Quarter)')
    ax.set_xlabel('State')
    ax.set_ylabel('Total Insurance Premium Amount')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['state'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_4_1(file_path):
    df = pd.read_excel(file_path)
    # Sort the data by 'amount_growth' in descending order
    df_sorted = df.sort_values(by='amount_growth', ascending=False)

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(12, 7)) # Changed to fig, ax
    ax.bar(df_sorted['state'], df_sorted['amount_growth']) # Changed to ax.bar
    ax.set_title('States with the Highest Growth in Transaction Amount Year-over-Year (2021 vs 2022)') # Changed to ax.set_title
    ax.set_xlabel('State') # Changed to ax.set_xlabel
    ax.set_ylabel('Amount Growth') # Changed to ax.set_ylabel
    ax.set_xticklabels(df_sorted['state'], rotation=90, ha='right') # Changed to set_xticklabels and rotation=90
    ax.ticklabel_format(style='plain', axis='y') # Changed to ax.ticklabel_format
    plt.tight_layout()
    # plt.show() # Removed show
    return fig # Return fig for Streamlit

def plot_4_2(file_path):
    df = pd.read_excel(file_path)
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    df_volume = df.sort_values(by='total_transaction_volume', ascending=False)
    axes[0].bar(df_volume['state'], df_volume['total_transaction_volume'])
    axes[0].set_title('Total Transaction Volume per State (Latest Year/Quarter)')
    axes[0].set_xlabel('State')
    axes[0].set_ylabel('Total Transaction Volume')
    axes[0].ticklabel_format(style='plain', axis='y')
    axes[0].set_xticklabels(df_volume['state'], rotation=90, ha='right') # Updated for consistency

    df_value = df.sort_values(by='total_transaction_value', ascending=False)
    axes[1].bar(df_value['state'], df_value['total_transaction_value'])
    axes[1].set_title('Total Transaction Value per State (Latest Year/Quarter)')
    axes[1].set_xlabel('State')
    axes[1].set_ylabel('Total Transaction Value')
    axes[1].ticklabel_format(style='plain', axis='y')
    axes[1].set_xticklabels(df_value['state'], rotation=90, ha='right') # Updated for consistency

    plt.tight_layout()
    return fig

def plot_5_1(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='total_registered_users', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(df_sorted['district_name'], df_sorted['total_registered_users'])
    ax.set_title('Top 10 Districts by Total Registered Users (Latest Year/Quarter)')
    ax.set_xlabel('District Name')
    ax.set_ylabel('Total Registered Users')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['district_name'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_5_2(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='avg_app_opens_per_user', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(df_sorted['state'], df_sorted['avg_app_opens_per_user'])
    ax.set_title('State-wise Average App Opens per Registered User')
    ax.set_xlabel('State')
    ax.set_ylabel('Average App Opens Per User')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['state'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_6_1(file_path):
    df = pd.read_excel(file_path)
    df_top_10 = df.sort_values(by='total_premium_count', ascending=False).head(10)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(df_top_10['district'], df_top_10['total_premium_count'])
    ax.set_title('Top 10 Districts by Insurance Transaction Volume (e.g., 2022 Q3)')
    ax.set_xlabel('District')
    ax.set_ylabel('Total Premium Count')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_top_10['district'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_6_2(file_path):
    df = pd.read_excel(file_path)
    fig, axes = plt.subplots(1, 2, figsize=(20, 8))

    df_growth_amount = df.sort_values(by='growth_amount', ascending=False)
    axes[0].bar(df_growth_amount['state'], df_growth_amount['growth_amount'])
    axes[0].set_title('States with Significant Growth in Insurance Premium Amount (2021 vs 2022) - Absolute Growth')
    axes[0].set_xlabel('State')
    axes[0].set_ylabel('Growth Amount')
    axes[0].ticklabel_format(style='plain', axis='y')
    axes[0].set_xticklabels(df_growth_amount['state'], rotation=90, ha='right')

    df_percentage_growth = df.sort_values(by='percentage_growth', ascending=False)
    axes[1].bar(df_percentage_growth['state'], df_percentage_growth['percentage_growth'], color='orange')
    axes[1].set_title('States with Significant Growth in Insurance Premium Amount (2021 vs 2022) - Percentage Growth')
    axes[1].set_xlabel('State')
    axes[1].set_ylabel('Percentage Growth (%)')
    axes[1].ticklabel_format(style='plain', axis='y')
    axes[1].set_xticklabels(df_percentage_growth['state'], rotation=90, ha='right')

    plt.tight_layout()
    return fig

def plot_7_1(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='total_transaction_value', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(df_sorted['state'], df_sorted['total_transaction_value'])
    ax.set_title('Top 10 States by Total Transaction Value (Most Recent Data)')
    ax.set_xlabel('State')
    ax.set_ylabel('Total Transaction Value')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['state'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_7_2(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='total_transaction_count', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_sorted['district_name'], df_sorted['total_transaction_count'])
    ax.set_title("Top 5 Districts by Total Transaction Count in Maharashtra (2022 Q4)")
    ax.set_xlabel("District Name")
    ax.set_ylabel("Total Transaction Count")
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['district_name'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_8_1(file_path):
    df = pd.read_excel(file_path)
    df['pincode'] = df['pincode'].astype(str)
    df_sorted = df.sort_values(by='total_registered_users', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(df_sorted['pincode'], df_sorted['total_registered_users'])
    ax.set_title('Top 10 Pincodes by Registered Users (Latest Available Quarter)')
    ax.set_xlabel('Pincode')
    ax.set_ylabel('Total Registered Users')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['pincode'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_8_2(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='total_registered_users', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(df_sorted['state'], df_sorted['total_registered_users'])
    ax.set_title('States with the Highest Total Registered Users (Over All Time)')
    ax.set_xlabel('State')
    ax.set_ylabel('Total Registered Users')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['state'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_9_1(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='premium_count', ascending=False)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(df_sorted['district_name'], df_sorted['premium_count'])
    ax.set_title('Top 5 Districts by Insurance Premium Count (2021 Q2)')
    ax.set_xlabel('District Name')
    ax.set_ylabel('Premium Count')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['district_name'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

def plot_9_2(file_path):
    df = pd.read_excel(file_path)
    df_sorted = df.sort_values(by='total_insurance_premium_amount', ascending=False)
    fig, ax = plt.subplots(figsize=(12, 7))
    ax.bar(df_sorted['state'], df_sorted['total_insurance_premium_amount'])
    ax.set_title('Top 10 States by Total Insurance Premium Amount (Latest Year and Quarter)')
    ax.set_xlabel('State')
    ax.set_ylabel('Total Insurance Premium Amount')
    ax.ticklabel_format(style='plain', axis='y')
    ax.set_xticklabels(df_sorted['state'], rotation=90, ha='right') # Updated for consistency
    plt.tight_layout()
    return fig

# --- Streamlit Layout ---

plot_functions = {
    "Transaction Count and Amount per Payment Instrument (All Years/Quarters)": plot_1_1,
    "Quarterly Transaction Trend (Maharashtra, Recharge & Bill Payments)": plot_1_2,
    "Top 5 States by Total Transaction Amount (2022)": plot_1_3,
    "Number of Registered Users and App Opens by Device Brand (All Years/Quarters)": plot_2_1,
    "User Engagement: Registered Users by Device Brand (Karnataka, 2021)": plot_2_2,
    "Total Insurance Premium Count and Amount Over Time": plot_3_1,
    "Top 5 States by Total Insurance Premium Amount (Latest Year/Quarter)": plot_3_2,
    "States with Highest Growth in Transaction Amount Year-over-Year (2021 vs 2022)": plot_4_1,
    "Total Transaction Volume and Value per State (Latest Year/Quarter)": plot_4_2,
    "Top 10 Districts by Total Registered Users (Latest Year/Quarter)": plot_5_1,
    "State-wise Average App Opens per Registered User": plot_5_2,
    "Top 10 Districts by Insurance Transaction Volume (2022 Q3)": plot_6_1,
    "States with Significant Growth in Insurance Premium Amount (2021 vs 2022)": plot_6_2,
    "Top 10 States by Total Transaction Value (Most Recent Data)": plot_7_1,
    "Top 5 Districts by Total Transaction Count in Maharashtra (2022 Q4)": plot_7_2,
    "Top 10 Pincodes by Registered Users (Latest Available Quarter)": plot_8_1,
    "States with the Highest Total Registered Users (Over All Time)": plot_8_2,
    "Top 5 Districts by Insurance Premium Count (2021 Q2)": plot_9_1,
    "Top 10 States by Total Insurance Premium Amount (Latest Year and Quarter)": plot_9_2,
}

# Map plot titles to their corresponding file keys
file_key_map = {
    "Transaction Count and Amount per Payment Instrument (All Years/Quarters)": '1.1',
    "Quarterly Transaction Trend (Maharashtra, Recharge & Bill Payments)": '1.2',
    "Top 5 States by Total Transaction Amount (2022)": '1.3',
    "Number of Registered Users and App Opens by Device Brand (All Years/Quarters)": '2.1',
    "User Engagement: Registered Users by Device Brand (Karnataka, 2021)": '2.2',
    "Total Insurance Premium Count and Amount Over Time": '3.1',
    "Top 5 States by Total Insurance Premium Amount (Latest Year/Quarter)": '3.2',
    "States with Highest Growth in Transaction Amount Year-over-Year (2021 vs 2022)": '4.1',
    "Total Transaction Volume and Value per State (Latest Year/Quarter)": '4.2',
    "Top 10 Districts by Total Registered Users (Latest Year/Quarter)": '5.1',
    "State-wise Average App Opens per Registered User": '5.2',
    "Top 10 Districts by Insurance Transaction Volume (2022 Q3)": '6.1',
    "States with Significant Growth in Insurance Premium Amount (2021 vs 2022)": '6.2',
    "Top 10 States by Total Transaction Value (Most Recent Data)": '7.1',
    "Top 5 Districts by Total Transaction Count in Maharashtra (2022 Q4)": '7.2',
    "Top 10 Pincodes by Registered Users (Latest Available Quarter)": '8.1',
    "States with the Highest Total Registered Users (Over All Time)": '8.2',
    "Top 5 Districts by Insurance Premium Count (2021 Q2)": '9.1',
    "Top 10 States by Total Insurance Premium Amount (Latest Year and Quarter)": '9.2',
}

plot_keys = list(plot_functions.keys())

for i in range(0, len(plot_keys), 2):
    col1, col2 = st.columns(2)
    with col1:
        if i < len(plot_keys):
            plot_title_1 = plot_keys[i]
            file_key_1 = file_key_map[plot_title_1]
            try:
                st.subheader(plot_title_1)
                fig = plot_functions[plot_title_1](file_paths[file_key_1])
                st.pyplot(fig)
                plt.close(fig)
            except FileNotFoundError:
                st.error(f"Error: File not found for '{plot_title_1}'. Please ensure '{file_paths[file_key_1]}' is in the correct directory and spelled EXACTLY as shown (e.g., '1.1.xlsx').")
            except Exception as e:
                st.error(f"An unexpected error occurred while plotting '{plot_title_1}': {e}. Make sure the Excel file is correctly formatted and contains data on the first sheet, or specify 'sheet_name' in pd.read_excel if it's on another sheet.")

    with col2:
        if i + 1 < len(plot_keys):
            plot_title_2 = plot_keys[i+1]
            file_key_2 = file_key_map[plot_title_2]
            try:
                st.subheader(plot_title_2)
                fig = plot_functions[plot_title_2](file_paths[file_key_2])
                st.pyplot(fig)
                plt.close(fig)
            except FileNotFoundError:
                st.error(f"Error: File not found for '{plot_title_2}'. Please ensure '{file_paths[file_key_2]}' is in the correct directory and spelled EXACTLY as shown (e.g., '1.2.xlsx').")
            except Exception as e:
                st.error(f"An unexpected error occurred while plotting '{plot_title_2}': {e}. Make sure the Excel file is correctly formatted and contains data on the first sheet, or specify 'sheet_name' in pd.read_excel if it's on another sheet.")