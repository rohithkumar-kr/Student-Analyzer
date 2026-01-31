STUDENT ANALYZER – WEB APPLICATION
=================================

Student Analyzer is a Flask-based web application that analyzes student
performance data from a CSV file and presents insights through a modern,
responsive dashboard.

The project focuses on backend data processing using Pandas and frontend
visualization using Tailwind CSS and Chart.js.


FEATURES
--------------------------------------------------
• Upload CSV files containing student marks
• Automatically detects subject columns
• Calculates:
  - Student-wise average
  - Subject-wise average
• Grade assignment with pass/fail logic:
  - Student must score >= 40 in ALL subjects to pass
• Top 3 students podium ranking
• Total passed, failed, and pass percentage
• Interactive bar charts:
  - Student-wise performance
  - Subject-wise subject averages
• Fully responsive UI (desktop, tablet, mobile)
• Mobile-optimized table layout (no broken view)
• Error handling for invalid CSV or chart issues


TECH STACK
--------------------------------------------------
Backend:
• Python
• Flask
• Pandas

Frontend:
• HTML (Jinja templates)
• Tailwind CSS
• Chart.js


PROJECT STRUCTURE
--------------------------------------------------
```
📁Student Analyzer/
├── 📁 static/
│   └── 📁 css/
│       ├── 🎨 common.css
│       └── 🎨 result.css
├── 📁 templates/
│   ├── 🌐 index.html
│   └── 🌐 result.html
├── ⚙️ .gitignore
├── 🐍 app.py
└── 📄 requirements.txt
```


CSV FILE REQUIREMENTS
--------------------------------------------------
• CSV must contain a column named: Name
• Remaining columns should be numeric subjects
• Example:
  Name,Maths,Science,English
  Alice,78,82,90
  Bob,35,60,55


GRADE LOGIC
--------------------------------------------------
• If any subject < 40 → FAIL (Grade F)
• Otherwise grade based on average:
  - >= 90 → A
  - >= 75 → B
  - >= 60 → C
  - >= 40 → D


HOW TO RUN LOCALLY
--------------------------------------------------
1. Clone the repository
   git clone <your-repo-url>

2. Navigate to the project folder
   cd Student Analyzer

3. Create virtual environment
   python -m venv venv

4. Activate virtual environment
   Windows:
     venv\Scripts\activate
   Mac/Linux:
     source venv/bin/activate

5. Install dependencies
   pip install -r requirements.txt

6. Run the app
   python app.py

7. Open browser and visit
   http://127.0.0.1:5000


DEPLOYMENT
--------------------------------------------------
• The project is compatible with Render deployment
• requirements.txt is mandatory for deployment
• gunicorn is used as the production server


FUTURE IMPROVEMENTS
--------------------------------------------------
• Authentication system
• Export results as PDF/Excel
• Student-wise detailed profile
• Database integration
• Sorting and filtering in tables


AUTHOR
--------------------------------------------------
Built as a portfolio project to demonstrate:
• Flask backend development
• Pandas data analysis
• Responsive UI design
• Real-world CSV data handling

LICENSE
--------------------------------------------------
This project is open-source and free to use for learning and portfolio purposes.
