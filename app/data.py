from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

# Path to the CSV file
csv_file_path = r"C:\Users\Ev\Desktop\TRG Week 15\penguins_size.csv"

@app.route('/')
def load_data():
    try:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_file_path)
        # Convert the DataFrame to an HTML table
        html_table = df.to_html(classes='table table-striped', index=False)
        # Define a simple HTML template to render the table
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Data Table</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container mt-4">
                <h1 class="mb-4">Penguins Data</h1>
                {html_table}
            </div>
        </body>
        </html>
        """
        return render_template_string(html_template)
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"
    
@app.route('/torgersen')
def load_torgersen_data():
    try:
        # Load the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_file_path)
        # Remove rows with any missing values (NaN)
        df = df.dropna()
        # Filter the DataFrame for rows where the 'island' column is 'Torgersen'
        filtered_df = df[df['island'] == 'Torgersen']
        # Convert the filtered DataFrame to an HTML table
        html_table = filtered_df.to_html(classes='table table-striped', index=False)
        # Define a simple HTML template to render the table
        html_template = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Torgersen Data</title>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container mt-4">
                <h1 class="mb-4">Torgersen Island Data</h1>
                {html_table}
            </div>
        </body>
        </html>
        """
        return render_template_string(html_template)
    except Exception as e:
        return f"<h1>Error: {str(e)}</h1>"

if __name__ == '__main__':
    app.run(debug=True)