from flask import Flask, request, send_file
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if not file:
        return "No file uploaded", 400

    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(file)

    # Perform data transformation (example: add a new column)
    df['new_column'] = df['existing_column'] * 2  # change as per your transformation logic

    # Convert the transformed DataFrame to CSV
    transformed_csv = 'transformed.csv'
    df.to_csv(transformed_csv, index=False)

    # Send the transformed CSV file back to the client
    return send_file(transformed_csv, mimetype='text/csv', download_name='transformed.csv', as_attachment=True)

def some_transformation_function(df):
    # Example transformation
    return df

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0', port=5000)
