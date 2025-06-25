import argparse # For parsing command-line arguments
import pandas as pd # For reading and manipulationg CSV data
import json # Used if we need to process JSON natively
import sys # To exit the program on error
import os # Useful for future file checks

# Load the csv file
def load_csv(filepath):
    try:
        return pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"❌ File not found: {filepath}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error loading CSV: {e}")
        sys.exit(1)

def export_to_json(df, output_file):
    try:
        df.to_json(output_file, orient='records', lines=False, indent=2)
        print(f"✅ JSON exported to {output_file}")
    except Exception as e:
        print(f"❌ Failed to export JSON: {e}")
        sys.exit(1)

def export_to_sql(df, output_file, table_name='my_table'):
    try:
        with open(output_file, 'w') as f:
            for _, row in df.iterrows():
                columns = ', '.join(f"{col}" for col in df.columns)
                values = ', '.join(f"'{str(val).replace('\'', '\'\'')}'" for val in row)
                statement = f"INSERT INTO {table_name} ({columns}) VALUES ({values});\n"
                f.write(statement)
        print(f"✅ SQL exported to {output_file}")
    except Exception as e:
        print(f"❌ Failed to export SQL: {e}")
        sys.exit(1)

def filter_dataframe(df, column, value):
    if column and value:
        if column not in df.columns:
            print(f"❌ Column '{column}' not found in CSV.")
            sys.exit(1)
        return df[df[column].astype(str) == str(value)]

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert CSV to JSON or SQL with optional filtering.')
    parser.add_argument('--input', '-i', required=True, help='Input CSV file path')
    parser.add_argument('--output-format', '-f', required=True, choices=['json', 'sql'], help='Output format')
    parser.add_argument('--filter-column', help='Column name to filter by')
    parser.add_argument('--filter-value', help='Value to match in filter column')
    parser.add_argument('--output', '-o', default='output', help='Base name for output file')
    parser.add_argument('--table-name', default='my_table', help='(For SQL) Name of the SQL table')
    return parser.parse_args()

def main():
    args = parse_arguments()

    df = load_csv(args.input)

    if args.output_format == 'json':
        export_to_json(df, f"{args.output}.json")
    elif args.output_format == 'sql':
        export_to_sql(df, f"{args.output}.sql", args.table_name)

if __name__ == '__main__':
    main()

# Usage
# python src/cli.py --input data.csv --filter-column country --filter-value Kenya --output-format sql
# python src/cli.py --input data.csv --output-format json

