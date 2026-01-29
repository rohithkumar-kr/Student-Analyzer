from flask import Flask, render_template, request
import pandas as pd

# ------------------ APP INIT ------------------
app = Flask(__name__)

# ------------------ HELPERS ------------------
def assign_grade(row, subject_columns):
    # Fail if any subject < 40
    if (row[subject_columns] < 40).any():
        return "F"

    avg = row["Average"]

    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


def get_failed_subjects(row, subject_columns):
    failed = [sub for sub in subject_columns if row[sub] < 40]
    return ", ".join(failed)


# ------------------ ROUTES ------------------
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    # ---- Load CSV ----
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]
    df = pd.read_csv(file)

    # ---- Validate CSV ----
    if "Name" not in df.columns:
        return "CSV must contain a 'Name' column", 400

    # Detect numeric subject columns dynamically
    subject_columns = df.select_dtypes(include="number").columns.tolist()

    if not subject_columns:
        return "CSV must contain numeric subject columns", 400

    # ---- Clean Data ----
    df[subject_columns] = df[subject_columns].fillna(
        df[subject_columns].mean()
    )

    # ---- Calculations ----
    df["Average"] = df[subject_columns].mean(axis=1)
    df["Grade"] = df.apply(assign_grade, axis=1, subject_columns=subject_columns)
    df["FailedSubjects"] = df.apply(
        lambda row: get_failed_subjects(row, subject_columns), axis=1
    )

    # ---- Class Statistics ----
    total_students = len(df)
    passed_students = (df["Grade"] != "F").sum()
    failed_students = (df["Grade"] == "F").sum()
    pass_percentage = round((passed_students / total_students) * 100, 2)

    # ---- Aggregations ----
    subject_avg = df[subject_columns].mean().to_dict()
    topper = df.loc[df["Average"].idxmax()].to_dict()

    top3_students = (
        df.sort_values(by="Average", ascending=False)
          .head(3)[["Name", "Average", "Grade"]]
          .to_dict(orient="records")
    )

    students = df[
        ["Name", "Average", "Grade", "FailedSubjects"]
    ].to_dict(orient="records")

    # ---- Render ----
    return render_template(
        "result.html",
        subject_avg=subject_avg,
        topper=topper,
        top3_students=top3_students,
        students=students,
        total_students=total_students,
        passed_students=passed_students,
        failed_students=failed_students,
        pass_percentage=pass_percentage
    )


# ------------------ RUN ------------------
if __name__ == "__main__":
    app.run(debug=True)
