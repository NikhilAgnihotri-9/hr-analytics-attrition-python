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



if __name__ == "__main__":
    file_path = "WA_Fn-UseC_-HR-Employee-Attrition.csv"

    df_clean = load_and_prepare_data(file_path)

    dept_summary = department_summary(df_clean)
    role_summary = role_attrition_summary(df_clean)

    print("\nDepartment Summary:")
    print(dept_summary)

    print("\nRole Attrition Summary:")
    print(role_summary)
