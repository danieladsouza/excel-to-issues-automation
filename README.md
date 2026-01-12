## `Spreadsheet to GitLab Issues Automation` 📊➡️🐙

This project automates the creation of GitLab issues based on activities stored in an Excel spreadsheet. It reads structured data from the spreadsheet and creates issues via the GitLab API, reducing manual work and improving task tracking.

---

### `Features` 🛠️

* Read activities from an Excel spreadsheet;
* Filter records based on predefined status values;
* Automatically create GitLab issues with:

  * `Title`
  * `Description`
  * `Labels` based on status
  * `Due date` (when available)
* API integration using a private access token

---

### `Technologies and Concepts` 💻

* `Python` – Automation, data processing, and API integration
* `Pandas` – Reading and filtering Excel spreadsheets
* `Requests` – HTTP requests to the GitLab REST API
* `GitLab API` – Issue creation and project integration
* `Data validation` – Filtering rows and handling missing values

---

### `How to Use` 🚀

Clone this repository:

```bash
git clone <REPOSITORY_URL>
```

Install the dependencies:

```bash
pip install pandas requests
```

Configure the script:

```python
api = 'http://your-gitlab-url/api/v4'
token = 'your_private_token'
project_id = 'project_id'
spreadsheet = 'C:/path/to/spreadsheet.xlsx'
```

Run the script:

```bash
python automation.py
```

---

### `Spreadsheet Structure` 📄

The Excel file used contained the following columns:

* Task column
* Development column
* Status column
* Due date column

Feel free to modify the script to adapt it to your specific spreadsheet structure.

---

### `Use Case` 💡

Useful for teams that manage tasks in spreadsheets and want to automate their creation as GitLab issues, reducing manual effort and ensuring consistency.

---

### `Contact` 📧

- [E-mail](mailto:danieladsouzadias@gmail.com)
