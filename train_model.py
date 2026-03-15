import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

data = {
    "text": [
        # ---------------- RESUME ----------------
        "software developer resume python java cybersecurity skills experience education",
        "curriculum vitae data analyst machine learning projects skills education",
        "resume for cybersecurity analyst network security internship experience",
        "professional resume software engineer python programming experience",
        "job application resume computer science graduate networking skills",
        "resume web developer html css javascript portfolio projects",
        "cybersecurity resume penetration testing vulnerability assessment",
        "resume cloud engineer aws docker kubernetes experience",
        "cv data scientist python machine learning deep learning projects",
        "resume system administrator linux networking troubleshooting experience",
        "resume backend developer python django flask projects",
        "resume mobile developer android kotlin java application projects",
        "resume security analyst threat detection incident response experience",
        "resume database administrator sql database optimization experience",
        "resume devops engineer ci cd docker kubernetes pipeline experience",

        # ---------------- INVOICE ----------------
        "invoice number payment due billing address purchase order total amount",
        "company invoice payment receipt product purchase total cost",
        "billing statement invoice number amount due payment details",
        "invoice services provided consulting payment pending amount",
        "invoice product purchase quantity price tax total amount",
        "customer invoice billing information payment method order details",
        "purchase invoice product description unit price total bill",
        "invoice receipt order payment confirmation billing statement",
        "invoice generated software license purchase amount payable",
        "service invoice payment due consulting hours total bill",
        "invoice order confirmation payment details product purchase",
        "business invoice total cost tax payment invoice number",
        "invoice issued for maintenance service payment details",
        "online purchase invoice billing total amount paid",
        "order invoice product quantity price payment confirmation",

        # ---------------- NOTES ----------------
        "meeting notes project discussion agenda action items summary",
        "lecture notes cybersecurity networking protocols security concepts",
        "class notes operating systems memory management scheduling",
        "study notes cybersecurity exam encryption authentication protocols",
        "team meeting notes project timeline responsibilities discussion",
        "lecture notes machine learning supervised unsupervised algorithms",
        "notes research discussion cloud security architecture ideas",
        "project meeting brainstorming notes development tasks",
        "training notes ethical hacking penetration testing techniques",
        "course notes database management sql normalization concepts",
        "meeting summary discussion software development sprint planning",
        "lecture notes artificial intelligence neural networks concepts",
        "notes from seminar cybersecurity threats defense strategies",
        "class discussion notes computer networks protocols routing",
        "project notes planning application architecture system design"
    ],
    "label": [
        # Resume labels
        "Resume","Resume","Resume","Resume","Resume",
        "Resume","Resume","Resume","Resume","Resume",
        "Resume","Resume","Resume","Resume","Resume",

        # Invoice labels
        "Invoice","Invoice","Invoice","Invoice","Invoice",
        "Invoice","Invoice","Invoice","Invoice","Invoice",
        "Invoice","Invoice","Invoice","Invoice","Invoice",

        # Notes labels
        "Notes","Notes","Notes","Notes","Notes",
        "Notes","Notes","Notes","Notes","Notes",
        "Notes","Notes","Notes","Notes","Notes"
    ]
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer(ngram_range=(1,2))
X = vectorizer.fit_transform(df["text"])

model = MultinomialNB()
model.fit(X, df["label"])

joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("AI model trained successfully")