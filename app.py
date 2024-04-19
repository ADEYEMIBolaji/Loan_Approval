{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d1188ec8-907b-4ec5-8ab2-5047faf328d6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[2], line 6\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mbeartype\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m beartype\n\u001b[1;32m----> 6\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mLoan_Approval_App\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mpredict_approval\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m Predictor\n\u001b[0;32m      9\u001b[0m Train \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdata/train.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     12\u001b[0m \u001b[38;5;129m@beartype\u001b[39m\n\u001b[0;32m     13\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21m__init__\u001b[39m(\n\u001b[0;32m     14\u001b[0m         \u001b[38;5;28mself\u001b[39m,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m     25\u001b[0m         Credit_History: \u001b[38;5;28mint\u001b[39m\n\u001b[0;32m     26\u001b[0m     ) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n",
      "File \u001b[1;32m~\\Desktop\\Desk\\Data\\Finance Loan Approval\\Loan_Approval_App\\__init__.py:5\u001b[0m\n\u001b[0;32m      1\u001b[0m {\n\u001b[0;32m      2\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcells\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m----> 5\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[43mnull\u001b[49m,\n\u001b[0;32m      6\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mce2c1ddf-e7d4-4dfa-9780-07e2362dc5cc\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      7\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m      8\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m      9\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: []\n\u001b[0;32m     10\u001b[0m   }\n\u001b[0;32m     11\u001b[0m  ],\n\u001b[0;32m     12\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     13\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mkernelspec\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     14\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_name\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPython 3 (ipykernel)\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     15\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     16\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     17\u001b[0m   },\n\u001b[0;32m     18\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage_info\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     19\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcodemirror_mode\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     20\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     21\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m\n\u001b[0;32m     22\u001b[0m    },\n\u001b[0;32m     23\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfile_extension\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.py\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     24\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmimetype\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/x-python\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     25\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     26\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbconvert_exporter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     27\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpygments_lexer\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     28\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.10.9\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     29\u001b[0m   }\n\u001b[0;32m     30\u001b[0m  },\n\u001b[0;32m     31\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m4\u001b[39m,\n\u001b[0;32m     32\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat_minor\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m\n\u001b[0;32m     33\u001b[0m }\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import pickle\n",
    "import gradio as gr\n",
    "import pandas as pd\n",
    "\n",
    "from beartype import beartype\n",
    "from Loan_Approval_App.predict_approval import Predictor\n",
    "\n",
    "\n",
    "Train = pd.read_csv(\"data/train.csv\")\n",
    "\n",
    "\n",
    "@beartype\n",
    "def __init__(\n",
    "        self,\n",
    "        Gender: str,\n",
    "        Married: bool,\n",
    "        Dependents: str,\n",
    "        Education: str,\n",
    "        Self_Employed: str,\n",
    "        Property_Area: str,\n",
    "        ApplicantIncome: int,\n",
    "        CoapplicantIncome: int,\n",
    "        LoanAmount: int,\n",
    "        Loan_Amount_Term: int,\n",
    "        Credit_History: int\n",
    "    ) -> None:\n",
    "\n",
    "    with gr.Blocks(gr.themes.Soft()) as demo:\n",
    "        Gender = ['Male', 'Female', 'Others']\n",
    "        Married = gr.Dropdown(label=\"Married\", choices=Train['Married'].drop_duplicates().dropna().values.tolist())\n",
    "        Dependents = gr.Dropdown(label=\"Dependents\", choices=Train['Dependents'].drop_duplicates().dropna().values.tolist())\n",
    "        Education = gr.Dropdown(label=\"Education\", choices=Train['Education'].drop_duplicates().dropna().values.tolist())\n",
    "        Property_Area = gr.Dropdown(label=\"Property_Area\", choices=Train['Property_Area'].drop_duplicates().dropna().values.tolist())\n",
    "    \n",
    "        with gr.Column():\n",
    "            CoapplicantIncome = gr.Textbox(label=\"CoapplicantIncome\", placeholder=\"Input CoapplicantIncome...\")\n",
    "            Self_Employed = gr.Radio([\"Yes\", \"No\"], label=\"Self Employed\")\n",
    "            ApplicantIncome = gr.Textbox(label=\"Applicant Income\", placeholder=\"Input Income...\")\n",
    "            LoanAmount = gr.Textbox(label=\"Loan Amount\", placeholder=\"Input Loan Amount...\")\n",
    "            Loan_Amount_Term = gr.Textbox(label=\"Loan Term\", placeholder=\"Input Loan Term...\")\n",
    "            Credit_History = gr.Radio([1.0, 0.0], label=\"Credit History\")\n",
    "            Gender = gr.Dropdown(Gender, label=\"Gender\")\n",
    "            generate_btn = gr.Button(\"Predict Approval\")\n",
    "            gr.Markdown(\"Predicted Approval:\")\n",
    "            output = gr.Text(label=\"Predict Approval\")\n",
    "    \n",
    "        generate_btn.click(fn=predict_approval, inputs=[Gender, Married, Dependents, Education, Self_Employed, Property_Area, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History],outputs=output)\n",
    "    \n",
    "    # if __name__ == \"__main__\":\n",
    "demo.launch(share=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ea9b6a8-816f-400a-999a-ece6c3ebac26",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
