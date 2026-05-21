from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def load_books():
    try:
        # books.csv থেকে ডেটা নেওয়া হচ্ছে
        df = pd.read_csv("books.csv", skiprows=1)
        df.columns = df.columns.str.strip()
        df = df.fillna("")
        return df.to_dict(orient="records")
    except Exception as e:
        print("Error loading csv:", e)
        return []

@app.route('/')
def home():
    books = load_books()
    return render_template('index.html', books=books)

if __name__ == '__main__':
    app.run()
