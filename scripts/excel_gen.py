import pandas as pd
import xlsxwriter

# Load cleaned data
room_income = pd.read_csv("../data/room_income.csv")
bcom_data = pd.read_csv("../data/bcom_data.csv")

# Clean column names
room_income.columns = room_income.columns.str.strip()
bcom_data.columns = bcom_data.columns.str.strip()

# Fix date column and add Booking Month
bcom_data['Booked on'] = pd.to_datetime(bcom_data['Booked on'], errors='coerce')
bcom_data['Booking Month'] = bcom_data['Booked on'].dt.to_period('M').astype(str)

# Monthly Bookings
monthly_bookings = bcom_data.groupby(['Booking Month', 'Status']).size().unstack(fill_value=0).reset_index()

# Calculate Profit (Accom + Other - Discount)
room_income['Profit'] = room_income['Accom'] + room_income['Other'] - room_income['Discount']

# Profit Per Room
profit_per_room = room_income[['Room', 'Profit']].copy()

# Occupancy Analysis
occupancy_analysis = room_income[['Room', 'Occupancy (%)', 'Avg Daily Tariff', 'Profit']].copy()

# Save all to a multi-sheet Excel file
with pd.ExcelWriter("../outputs/excel/Hotel_Analysis_Cleaned.xlsx", engine='xlsxwriter') as writer:
    room_income.to_excel(writer, index=False, sheet_name='Cleaned_Room_Income')
    bcom_data.to_excel(writer, index=False, sheet_name='Cleaned_Booking_Data')
    monthly_bookings.to_excel(writer, index=False, sheet_name='Monthly_Bookings')
    profit_per_room.to_excel(writer, index=False, sheet_name='Profit_Per_Room')
    occupancy_analysis.to_excel(writer, index=False, sheet_name='Occupancy_Analysis')
