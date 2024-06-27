import pickle
import gradio as gr
import pandas as pd

from beartype import beartype
from Loan_Approval_App.predict_approval import Predictor


Train = pd.read_csv("data/train.csv")


@beartype
def __init__(
        self,
        Gender: str,
        Married: bool,
        Dependents: str,
        Education: str,
        Self_Employed: str,
        Property_Area: str,
        ApplicantIncome: int,
        CoapplicantIncome: int,
        LoanAmount: int,
        Loan_Amount_Term: int,
        Credit_History: int
    ) -> None:

    with gr.Blocks(gr.themes.Soft()) as demo:
        Gender = ['Male', 'Female', 'Others']
        Married = gr.Dropdown(label="Married", choices=Train['Married'].drop_duplicates().dropna().values.tolist())
        Dependents = gr.Dropdown(label="Dependents", choices=Train['Dependents'].drop_duplicates().dropna().values.tolist())
        Education = gr.Dropdown(label="Education", choices=Train['Education'].drop_duplicates().dropna().values.tolist())
        Property_Area = gr.Dropdown(label="Property_Area", choices=Train['Property_Area'].drop_duplicates().dropna().values.tolist())
    
        with gr.Column():
            CoapplicantIncome = gr.Textbox(label="CoapplicantIncome", placeholder="Input CoapplicantIncome...")
            Self_Employed = gr.Radio(["Yes", "No"], label="Self Employed")
            ApplicantIncome = gr.Textbox(label="Applicant Income", placeholder="Input Income...")
            LoanAmount = gr.Textbox(label="Loan Amount", placeholder="Input Loan Amount...")
            Loan_Amount_Term = gr.Textbox(label="Loan Term", placeholder="Input Loan Term...")
            Credit_History = gr.Radio([1.0, 0.0], label="Credit History")
            Gender = gr.Dropdown(Gender, label="Gender")
            generate_btn = gr.Button("Predict Approval")
            gr.Markdown("Predicted Approval:")
            output = gr.Text(label="Predict Approval")
    
        generate_btn.click(fn=predict_approval, inputs=[Gender, Married, Dependents, Education, Self_Employed, Property_Area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History],outputs=output)
    
if __name__ == "__main__":