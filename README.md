# 🛠️ CSVTool – CSV to JSON/SQL Converter (CLI + Streamlit)

> A command-line and GUI-based Python tool that converts CSV files to JSON or SQL INSERT statements with optional row filtering. Built with Python, Pandas, and Streamlit.

---

## 🚀 Features

- ✅ Convert any CSV file to JSON or SQL format
- 🧪 Includes unit tests with `pytest`
- 📦 Clean project structure with virtual environment and logging
- 🌐 Streamlit UI for non-technical users
- 📁 Export JSON or SQL output directly from the interface

---

## 📂 Folder Structure

```
csvtool/
├── src/
│   └── cli.py            # Main CLI logic
├── tests/
│   └── test_cli.py       # Pytest unit tests
├── data.csv              # Example CSV (user provided)
├── apppy                 # Streamlit UI
├── requirements.txt      # All dependencies
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/csvtool.git
cd csvtool
```

### 2. Create and Activate Virtual Environment

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🖥️ CLI Usage

```bash
python src/cli.py --input data.csv --output-format json
```

### ✅ Options

| Option            | Description                                      |
|------------------|--------------------------------------------------|
| `--input` / `-i`  | Input CSV file path (required)                  |
| `--output-format` / `-f` | `json` or `sql` output format (required)    |
| `--filter-column` | Column name to filter by            |
| `--filter-value`  | Value to filter for                 |
| `--output` / `-o` | Output file name (default: `output`)            |
| `--table-name`    | (SQL only) name of the SQL table (default: `my_table`) |

### 🔁 Example Commands

```bash
# Convert full CSV to JSON
python src/cli.py --input data.csv --output-format json

# Filter and convert to SQL
python src/cli.py --input data.csv --output-format sql --filter-column country --filter-value Kenya
```

---

## 🧪 Running Unit Tests

```bash
pytest tests/
```

Sample test checks:
- Exact match filtering
- Invalid column errors
- Data integrity after filtering

---

## 📜 Logging

- Logs are printed to the console with timestamps and severity level
- Logging is set to `INFO` level and helps trace issues during execution

Example output:
```
2024-06-24 12:00:01 [INFO] Loading CSV: data.csv
2024-06-24 12:00:02 [INFO] Exported JSON to output.json
```

---

## 🌐 Streamlit UI (Optional GUI)

### Launch the app:

```bash
streamlit run app.py
```

### Features:
- Upload CSV
- Filtering
- Choose output format (`json` or `sql`)
- Download the result

> 🔽 Buttons appear to export and download the converted data directly.

---

## 📦 Example Output

### JSON
```json
{"id": 1, "name": "Alice", "age": 30}
{"id": 2, "name": "Bob", "age": 25}
```

### SQL
```sql
INSERT INTO my_table (id, name, age) VALUES (1, 'Alice', 30);
INSERT INTO my_table (id, name, age) VALUES (2, 'Bob', 25);
```

---

## 📌 Roadmap / To-Do

- [ ] Add support for Excel files
- [ ] Add database connection options (PostgreSQL, SQLite)
- [ ] Support multiple filter conditions
- [ ] Dockerize the CLI and Streamlit app

---

## 🧑‍💻 Contributing

1. Fork the repo
2. Create a feature branch: `git checkout -b feature-xyz`
3. Commit and push: `git commit -m "feat: added new feature"`  
4. Open a pull request

---

## 📄 License

MIT License – feel free to use, modify, and distribute with attribution.

---

## 🙌 Acknowledgements

Built with:
- [Python](https://www.python.org/)
- [Pandas](https://pandas.pydata.org/)
- [Streamlit](https://streamlit.io/)
- [Pytest](https://docs.pytest.org/)

---

## 👩‍💻 Author

Rebecca Shirievo  
> GitHub: [@cyb3rr31a](https://github.com/cyb3rr31a)  
> 💡 Keep learning. Keep building.
