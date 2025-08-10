from datetime import datetime
from sklearn.metrics import accuracy_score,precision_score,roc_auc_score,recall_score,f1_score,confusion_matrix
current_year=datetime.now().year
def calc_wage(row,hours=40):
    if row["unit_of_wage"]=="Year":
        return int(row["prevailing_wage"])
    elif row["unit_of_wage"]=="Month":
        return int(row["prevailing_wage"]*12)
    elif row["unit_of_wage"]=="Week":
        return int(row["prevailing_wage"]*52)
    else: return int(row["prevailing_wage"]*52*hours)

def label_company_size(row):
    if row["no_of_employees"]<1022:
        return "Small"
    elif row["no_of_employees"]<2109:
        return "Medium"
    elif row["no_of_employees"]<3504:
        return "Large"
    else:
        return "Very Large"
    
def convert_continent(row):
    if row["continent"]=="Asia":
        return "Asia"
    elif row["continent"]=="North America":
        return "North America"
    elif row["continent"]=="Europe":
        return "Europe"
    else:
        return "other"
# "High School","Bachelor's","Master's","Doctorate
# def education_encoder(row):
#     if row["education_of_employee"]=="High School":
#         return "High School"
#     elif row["education_of_employee"]=="Bachelor's":
#         return 1
#     elif row["education_of_employee"]=="Master's":
#         return 2
#     else:
#         return 3
    
def calc_company_age(row):
    age=datetime.now().year-row["yr_of_estab"]
    return age

def evaluate_model(ytrue,ypred):
    """this function return these paramenters in the same squence as specified---->(model_accuracy,model_f1,model_precision,model_recall,model_roc_auc,model_confusion_matrix)"""
    model_accuracy=accuracy_score(ytrue,ypred)
    model_f1=f1_score(ytrue,ypred)
    model_precision=precision_score(ytrue,ypred)
    model_recall=recall_score(ytrue,ypred)
    model_roc_auc=roc_auc_score(ytrue,ypred)
    model_confusion_matrix=roc_auc_score(ytrue,ypred)
    
    return (model_accuracy,model_f1,model_precision,model_recall,model_roc_auc,model_confusion_matrix)