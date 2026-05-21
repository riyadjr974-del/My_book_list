from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

def load_books():
    try:
        # CSV রিড করা হচ্ছে (১ম লাইন বাদ দিয়ে)
        df = pd.read_csv("books.csv", skiprows=1)
        
        # শুধুমাত্র প্রথম ৪টি কলাম নেওয়া হচ্ছে
        df = df.iloc[:, :4]
        
        # কলামের নামগুলো ইংরেজিতে সেট করে দিচ্ছি, যাতে বাংলা ফন্ট বা বানানের কোনো সমস্যা না হয়
        df.columns = ['serial', 'name', 'link', 'audio']
        
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
