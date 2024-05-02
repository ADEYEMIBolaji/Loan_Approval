# Loan Approval Predictions

Welcome to the Loan Approval Predictions project! Below you'll find essential information on how to navigate through the project, understand the data, and utilize the predictive model for determining loan eligibility.

## Data Source and Information

The dataset utilized for this project was obtained from Kaggle. It comprises 614 entries with 13 columns, encompassing various attributes related to loan applicants. Here's a breakdown of the columns:

1. Loan_ID: Unique identifier for each loan application
2. Gender: Gender of the applicant
3. Married: Marital status of the applicant
4. Dependents: Number of dependents the applicant has
5. Education: Education level of the applicant
6. Self_Employed: Whether the applicant is self-employed or not
7. ApplicantIncome: Income of the applicant
8. CoapplicantIncome: Income of the co-applicant
9. LoanAmount: Amount of loan applied for
10. Loan_Amount_Term: Term of the loan in months
11. Credit_History: Credit history of the applicant
12. Property_Area: Type of property area
13. Loan_Status: Status of the loan (target variable)

## Data Preprocessing and Model Building

To prepare the data for modeling, the following steps were undertaken:

1. Data splitting: The dataset was divided into training and testing sets.
2. Encoding and Scaling: Categorical data were encoded, and numerical features were scaled using standard scaler.
3. Model Selection: Gradient Boosting was chosen as the base model for its predictive performance.
4. Cross-validation and Hyperparameter Tuning: Grid search was performed to optimize model hyperparameters for better performance.

## Model Deployment and Explainability

The final model was saved using a Pipeline, encompassing data preprocessing steps and the trained classifier. Additionally, ShapAnalysis was conducted to provide insights into feature importance for model explainability.

The model was deployed using Gradio, enabling users to interactively input applicant details and receive predictions regarding loan eligibility. However, currently, the deployment requires cloning the repository to your local system. [Click here](http://127.0.0.1:7860) to access the deployed model.

Below is a screenshot of the web interface:

![Screenshot of Loan Approval Prediction Web Interface]([img]https://i.imgur.com/Cfu9zqZ.png[/img])

## Future Developments

The project remains open for further development, particularly in the following areas:

1. **Data Enrichment**: Sourcing real-world data that closely mirrors loan application scenarios to enhance model robustness.
2. **Deployment Enhancement**: Implementing deployment methods that eliminate the need for local repository cloning, making the model accessible via a web interface without additional steps.

Feel free to contribute or explore these avenues for further improving the project's utility and effectiveness.

Thank you for your interest in Loan Approval Predictions!
