
from flask import Flask, render_template_string
import psycopg2
import os
app = Flask(__name__)

@app.route("/")
def home():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        database=os.getenv("POSTGRES_DB", "mydatabase"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
)


    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM items ORDER BY id")
    items = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Записи из PostgreSQL</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f3f4f6;
                padding: 50px;
            }
            .container {
                background: white;
                padding: 30px;
                max-width: 600px;
                margin: auto;
            }
            h1 {
                color: #1f2937;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                border: 1px solid #ddd;
                padding: 12px;
                text-align: left;
            }
            th {
                background: #f3f4f6;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Записи из PostgreSQL</h1>
            <p>Эту страницу отдаёт Flask из контейнера app.</p>

            <table>
                <tr>
                    <th>ID</th>
                    <th>Название</th>
                </tr>
                {% for item in items %}
                <tr>
                    <td>{{ item[0] }}</td>
                    <td>{{ item[1] }}</td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </body>
    </html>
    """, items=items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
