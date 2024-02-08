import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

# Function to make predictions using the trained model
def make_predictions(tickets_out, capacity, month, day):
    # This is just a placeholder; implement your actual prediction logic here
    new_data = pd.DataFrame({
        'tickets_out': [tickets_out],
        'capacity': [capacity],
        'month': [month],
        'day': [day]
    })

    # Scale new data using the same scaler
    new_data_scaled = pd.DataFrame(scaler.transform(new_data), columns=new_data.columns)

    # Make predictions
    predicted_price = model.predict(new_data_scaled)
    return predicted_price[0]

# Step 1: Data Preprocessing
data = pd.read_csv('data/cinemaTicket_Ref.csv')

# Handle missing values
imputer = SimpleImputer(strategy='mean')

# Drop non-numeric columns for imputation
numeric_data = data.select_dtypes(include=['float64', 'int64'])

# Impute missing values
data_imputed = pd.DataFrame(imputer.fit_transform(numeric_data), columns=numeric_data.columns)

# Select relevant features
features = ['tickets_out', 'capacity', 'month', 'day']

# Extract the selected features and target variable
X = data_imputed[features]
y = data_imputed['ticket_price']

# Step 2: Feature Scaling
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 4: Model Selection
model = LinearRegression()

# Step 5: Model Training
model.fit(X_train, y_train)

# Step 6: Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')
