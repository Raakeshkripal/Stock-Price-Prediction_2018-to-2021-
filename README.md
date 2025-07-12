# Stock-Price-Prediction_2018-to-2021

# 📈 Stock Price Prediction using Machine Learning

This project leverages historical stock market data to predict future prices using machine learning techniques. The model is trained and evaluated on prominent Indian companies: **IOC**, **Sun Pharma**, **Reliance**, **ITC**, and **TCS**. The approach is generalized, allowing future predictions with updated datasets from the same or different companies.

---

## 🚀 Project Highlights

- ✅ Built with Python in Jupyter Notebook
- ✅ Uses historical data for five NSE-listed companies
- ✅ Predicts next-day closing stock price
- ✅ Scalable for other stocks or future time periods
- ✅ Focus on feature engineering, visualization, and model accuracy

---

## 🛠️ Tech Stack & Libraries

- Python 3.x
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- YFinance (for fetching stock data)
- Joblib (for saving models)
- Jupyter Notebook

---

## 📊 Dataset

Stock data for the following companies were used (2018–2021):

-  IOC (Indian Oil Corporation)
-  Sun Pharma
-  Reliance Industries
-  ITC Ltd
-  Tata Consultancy Services (TCS)

---

## 🔍 Methodology

1. **Data Preprocessing**
   - Handling missing values
   - Calculating moving averages
   - Feature scaling

2. **Feature Engineering**
   - Lag features (previous close, moving averages)
   - Technical indicators (optional)

3. **Model Training**
   - Train-Test Split
   - Linear Regression Model (or another ML model)
   - Model fitting and prediction

4. **Model Evaluation**
   - Mean Squared Error (MSE)
   - R² Score
   - Visual comparisons: actual vs predicted

---

## 📈 Results

The model shows a good trend-following prediction on the closing prices of the selected stocks. Visualization confirms that predictions closely match actual prices for short-term forecasting.

---

## 🔮 Future Scope

- ✅ Update the model with **current-year (2025 and beyond)** datasets for dynamic predictions.
- ✅ Add more features: RSI, MACD, Bollinger Bands.
- ✅ Deploy the model as a **web dashboard** using Flask/Streamlit.
- ✅ Integrate LSTM or other deep learning models for longer forecasting horizons.
- ✅ Real-time data updates using APIs.

---

## 🏷️ How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/stock-price-prediction.git
   cd stock-price-prediction

## Author
Raakesh kripal.VUK
**contact:** raakeshkripal.vuk@gmail.com
