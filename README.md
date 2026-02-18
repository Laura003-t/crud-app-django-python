# 👥 Professional Staff Manager App

A comprehensive staff management system built with Django, designed for HR and administrators to maintain detailed records of employees, contact information, and organizational structure.

## 🚀 Features

- **📂 Comprehensive Employee Profiles**: Track names, staff IDs, titles, departments, units, divisions, and age.
- **📞 Contact Directory**: Store and access employee emails and phone numbers easily.
- **📅 Employment Tracking**: Log start dates and organizational positions.
- **🔐 Secure Audit Trail**: Automatically tracks which administrator added or updated an employee record.
- **🔍 Smart Searching**: Native ordering by Staff ID for easy record lookup.
- **🛠️ Admin Dashboard**: Full control over employee data via the Django admin interface.

## 🛠️ Tech Stack

- **Backend**: Python, [Django](https://www.djangoproject.com/)
- **Frontend**: Clean HTML Templates, CSS3
- **Database**: SQLite3
- **Authentication**: Django built-in Auth system

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd "Personally Built Staff Manager App"
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r staffmanager/requirements.txt
   ```

4. **Environment Variables**:
   Create a `.env` file in the `staffmanager` directory:
   ```env
   DEBUG=True
   SECRET_KEY=your_secret_key
   ```

5. **Run Migrations**:
   ```bash
   cd staffmanager
   python manage.py migrate
   ```

6. **Create an Admin Account**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the server**:
   ```bash
   python manage.py runserver
   ```

## 📝 Usage

1. Log in to the admin portal at `/admin`.
2. Add employees with their full organizational details.
3. Use the frontend interface to browse the employee directory and view contact information.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## 📄 License

MIT License
