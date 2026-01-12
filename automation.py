# Libraries
import requests
import pandas as pd

# Your Gitlab API, acess token, project id and spreadsheet
api = 'http://your-gitlab-url/api/v4'
token = 'your_access_token'
project_id = '1234'
spreadsheet = 'C:/path/to/spreadsheet.xlsx'

headers = {'PRIVATE-TOKEN': token}

# Reads the spreadsheet. The sheet name is optional, in case there is more than one sheet
df = pd.read_excel(spreadsheet, sheet_name='SheetName')

# Filter by status
valid_status = ['Completed', 'Ongoing', 'Cancelled'] 
df_filters = df[df['Status'].isin(valid_status)]

# Loop 
for _, row in df_filters.iterrows():
    date = {'title': row['Task'],
            'description': row['Development'],
            'labels': row['Status']}

    # if a due date is provided, it is added as due_date
    if not pd.isna(row.get('Due Date')):
        date['due_date'] = str(row['Due Date'])

    url = f'{api}/projects/{project_id}/issues'

    # Sends the tasks as issues
    result = requests.post(url, headers=headers, json=date)

    if result.ok:
        print('Issue added!: ', row['Task'])
    else:
        print('Something went wrong!: ', result.status_code, result.text)