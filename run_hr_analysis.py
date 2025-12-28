import pandas as pd

def load_and_prepare_data(file_path):
    df = pd.read_csv(file_path)

    selected_columns = [
        "Age",
        "Department",
        "JobRole",
        "MonthlyIncome",
        "YearsAtCompany",
        "Attrition"
    ]

    df_clean = df[selected_columns].copy()

    df_clean["AttritionFlag"] = df_clean["Attrition"].map({
        "Yes": 1,
        "No": 0
    })

    return df_clean

def department_summary(df_clean):
    dept_employee_count = (
        df_clean
        .groupby("Department")
        .size()
        .reset_index(name="EmployeeCount")
    )

    dept_attrition_rate = (
        df_clean
        .groupby("Department")["AttritionFlag"]
        .mean()
        .reset_index(name="AttritionRate")
    )

    dept_summary = dept_employee_count.merge(
        dept_attrition_rate,
        on="Department"
    )

    dept_summary["AttritionRatePercent"] = (
        dept_summary["AttritionRate"] * 100
    ).round(2)

    return dept_summary


def role_attrition_summary(df_clean):
    role_attrition = (
        df_clean
        .groupby("JobRole")["AttritionFlag"]
        .mean()
        .reset_index(name="AttritionRate")
    )

    role_attrition["AttritionRatePercent"] = (
        role_attrition["AttritionRate"] * 100
    ).round(2)

    return role_attrition

def generate_summary_text(dept_summary, role_summary):
    highest_attrition_dept = dept_summary.loc[
        dept_summary["AttritionRatePercent"].idxmax(), "Department"
    ]

    highest_attrition_role = role_summary.loc[
        role_summary["AttritionRatePercent"].idxmax(), "JobRole"
    ]

    summary = f"""
HR Attrition Analysis Summary

- The department with the highest attrition rate is {highest_attrition_dept}.
- The job role with the highest attrition rate is {highest_attrition_role}.
- Attrition is not evenly distributed and appears concentrated in specific roles and departments.

Recommended Actions:
- Prioritize retention strategies for high-risk roles.
- Review compensation and growth opportunities in high-attrition departments.
- Strengthen early-tenure engagement programs.
"""

    with open("hr_summary.txt", "w") as file:
        file.write(summary.strip())


if __name__ == "__main__":
    file_path = "WA_Fn-UseC_-HR-Employee-Attrition.csv"

    df_clean = load_and_prepare_data(file_path)

    dept_summary = department_summary(df_clean)
    role_summary = role_attrition_summary(df_clean)

    dept_summary.to_csv("department_summary.csv", index=False)
    role_summary.to_csv("role_attrition_summary.csv", index=False)

    generate_summary_text(dept_summary, role_summary)

    print("Files generated:")
    print("- department_summary.csv")
    print("- role_attrition_summary.csv")
    print("- hr_summary.txt")


