# hr-analytics-attrition-python
Automated HR analytics report using Python for workforce planning.




# Automated HR Analytics Report for Workforce Planning Using Python

## Problem Statement
Organizations often rely on static Excel reports to understand employee attrition and workforce distribution. This project automates HR data analysis using Python to generate actionable insights for decision-makers.



## Dataset
This project uses a publicly available HR dataset created by IBM data scientists, containing employee demographics, job details, compensation, and attrition information.



## Business Questions
1. Which departments have the highest employee count and attrition rate?
2. Is attrition correlated with salary, age, or tenure?
3. Which job roles are most at risk of attrition?
4. What is the average tenure by department?
5. What actions can HR take based on these insights?



# HR Employee Attrition Analysis & Automation

This project analyzes employee attrition patterns using HR data and provides automated, repeatable insights to support data-driven retention strategies. The analysis focuses on attrition trends across departments, job roles, compensation levels, age, and tenure.



## Business Objectives

The primary goals of this analysis are to:
- Identify departments and job roles with higher attrition risk
- Understand how compensation, age, and tenure relate to attrition
- Provide actionable insights for HR decision-making
- Enable automated re-analysis when new employee data becomes available



## Dataset

- Source: IBM HR Analytics Employee Attrition Dataset
- Type: Synthetic / fictional HR dataset
- Records: Employee-level HR data including demographics, compensation, tenure, and attrition status

Note: While the dataset is fictional, the analysis approach and insights reflect real-world HR analytics practices.



## Tools & Technologies Used

- Python
- Pandas
- Matplotlib
- Jupyter Notebook
- Git & GitHub


## Project Structure

- `hr_attrition_analysis.ipynb`  
  Exploratory data analysis and visualization

- `run_hr_analysis.py`  
  Automated script to rerun analysis and generate output files

- `department_summary.csv`  
  Department-level attrition metrics

- `role_attrition_summary.csv`  
  Job role–level attrition metrics

- `hr_summary.txt`  
  Plain-English summary for stakeholders



## How to Run the Project

1. Clone the repository
2. Ensure Python is installed
3. Install required dependencies:
   pip install pandas matplotlib
4. Place the dataset in the project directory
5. Run the automation script:
   python run_hr_analysis.py



## Key Insights

- Attrition is not evenly distributed across the organization.
- Certain job roles exhibit consistently higher attrition risk.
- Employees with shorter tenure are more likely to leave.
- Compensation and departmental factors influence attrition patterns.



## Recommendations

- Focus retention efforts on high-attrition job roles.
- Review compensation and growth opportunities in vulnerable departments.
- Strengthen onboarding and early-career engagement initiatives.
- Use automated reporting to continuously monitor attrition trends.


