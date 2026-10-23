# Student Analyzer – Web Application

Student Analyzer is a Flask-based web application that analyzes student performance data from CSV files and presents insights through a modern, responsive dashboard.

The project combines backend data processing using Pandas with frontend visualization using Tailwind CSS and Chart.js. It can run locally using Python or inside a Docker container.

## Features

- Upload CSV files containing student marks.
- Automatically detects numeric subject columns.
- Calculates student-wise and subject-wise averages.
- Assigns grades based on average marks and pass/fail rules.
- Identifies students who fail in any subject.
- Displays the top three students in a podium ranking.
- Shows total passed students, failed students, and pass percentage.
- Interactive charts for student performance and subject averages.
- Responsive dashboard for desktop, tablet, and mobile.
- Input validation for invalid CSV files.
- Docker support for consistent containerized execution.

## Tech Stack

**Backend**
- Python 3.13
- Flask
- Pandas
- NumPy
- Gunicorn

**Frontend**
- HTML and Jinja2 templates
- Tailwind CSS
- Chart.js
- Custom CSS

**Containerization**
- Docker
- Python Slim base image
- Gunicorn production server
- Non-root container execution

## Project Structure

```text
Student Analyzer/
├── static/
│   └── css/
│       ├── common.css
│       └── result.css
├── templates/
│   ├── index.html
│   └── result.html
├── .dockerignore
├── .gitignore
├── Dockerfile
├── app.py
├── README.md
└── requirements.txt
```

## CSV File Requirements

Your CSV file must contain a column named `Name`. The remaining numeric columns are treated as subject marks.

Example:

```csv
Name,Maths,Science,English
Alice,78,82,90
Bob,35,60,55
Charlie,88,91,85
Dana,65,72,70
```

**Important:** Numeric columns other than student names are treated as subjects. Avoid including numeric roll numbers or IDs as additional columns.

## Grade and Pass/Fail Logic

A student fails if they score below 40 in any subject.

| Condition | Grade / Result |
|---|---|
| Any subject below 40 | F – Fail |
| Average ≥ 90, with all subjects passing | A |
| Average ≥ 75, with all subjects passing | B |
| Average ≥ 60, with all subjects passing | C |
| Average ≥ 40, with all subjects passing | D |

Missing numeric values are filled using the mean of their respective subject columns.

The dashboard displays student averages, subject averages, grades, pass/fail statistics, top-three rankings, and interactive charts.

## Running Locally

### Prerequisites

- Python 3.13 recommended.
- pip package manager.

### 1. Clone the repository

```bash
git clone <your-repo-url>
```

### 2. Navigate to the project directory

```bash
cd "Student Analyzer"
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows PowerShell**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows Command Prompt**

```bat
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Start the application

```bash
python app.py
```

### 7. Open the application

Visit:

http://127.0.0.1:5000

## Running with Docker

Docker lets you run Student Analyzer in a container without installing the project's Python dependencies directly into your host Python environment.

### Prerequisites

- Docker Desktop on Windows or macOS, or Docker Engine on Linux.
- Docker daemon running.

### 1. Clone the repository

```bash
git clone <your-repo-url>
```

Navigate into the project directory:

```bash
cd "Student Analyzer"
```

### 2. Build the Docker image

Run this command from the directory containing the Dockerfile:

```bash
docker build -t student-analyzer:local .
```

This builds an image containing the Python runtime, application dependencies, templates, and static assets.

### 3. Create and run the container

```bash
docker run -d --name student-analyzer-test -p 127.0.0.1:5000:5000 student-analyzer:local
```

This starts the application in the background and maps host port 5000 to container port 5000.

### 4. Open the application

Visit:

http://127.0.0.1:5000

Upload your CSV file and analyze student performance as usual.

### 5. Stop the container

```bash
docker stop student-analyzer-test
```

### 6. Start the existing container again

```bash
docker start student-analyzer-test
```

You only need to create the container once. Use `docker stop` and `docker start` for subsequent sessions.

### 7. View container logs

```bash
docker logs student-analyzer-test
```

To follow logs continuously:

```bash
docker logs -f student-analyzer-test
```

Press `Ctrl+C` to stop following the logs. This does not stop the container.

### 8. Check running containers

```bash
docker ps
```

To include stopped containers:

```bash
docker ps -a
```

### 9. Remove the container when no longer needed

First stop it if it is running:

```bash
docker stop student-analyzer-test
```

Then remove it:

```bash
docker rm student-analyzer-test
```

Removing a container does not remove the Docker image.

### Rebuilding after code changes

If you change application code or the Dockerfile, rebuild the image:

```bash
docker build -t student-analyzer:local .
```

To use the updated image, stop and remove the old container, then recreate it using the updated image:

```bash
docker stop student-analyzer-test
docker rm student-analyzer-test
docker run -d --name student-analyzer-test -p 127.0.0.1:5000:5000 student-analyzer:local
```

If the container does not exist, skip the stop and remove commands.

## Docker Design Notes

- The application runs as a non-root user inside the container.
- Gunicorn serves Flask on port 5000.
- Flask debug mode is not enabled in the Docker configuration.
- `.dockerignore` excludes the local virtual environment, Git metadata, caches, and environment files from the Docker build context.
- Uploaded CSV files are processed in memory and are not permanently stored by the application.
- No database or persistent volume is required by the current implementation.
- Tailwind CSS and Chart.js are loaded from browser-side CDNs, so the user's browser needs internet access for those assets.

## Deployment

The application can be adapted for platforms such as Render that support Python web services or Docker-based deployments.

For a Python-based deployment, install dependencies from `requirements.txt` and use a production WSGI server such as Gunicorn.

For container-based deployment, build and run the supplied Docker image using the platform's supported deployment configuration. Configure the service's listening port according to the hosting platform's requirements.

## Future Improvements

- Authentication and user management.
- Export results to PDF or Excel.
- Student-wise detailed performance profiles.
- Database integration for persistent records.
- Sorting and filtering in student tables.
- Automated tests for CSV validation and grade calculations.
- Offline frontend assets without external CDN dependencies.

## Author

Built as a portfolio project to demonstrate:

- Flask backend development.
- Data processing and analysis using Pandas and NumPy.
- Responsive web dashboard development.
- CSV file handling and validation.
- Docker image creation and container management.

## License

This project is open-source and free to use for learning and portfolio purposes.
