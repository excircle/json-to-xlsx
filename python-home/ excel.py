import pandas as pd
import json


def main():
    x = [(1, 'John Doe', '123-456-7890', '{"package": "family", "price": "$399.99", "redeemed": "false", "package_members": {"husband": "joe", "wife": "jane", "kid": "malort"}}')]

    # Convert the list of tuples to a DataFrame
    df = pd.DataFrame(x, columns=['ID', 'Name', 'Phone', 'Package'])

    # Optionally, if you want to parse the JSON in the 'Package' column to individual columns, you can do so:
    df['Package'] = df['Package'].apply(json.loads)  # Parse the JSON string to a dictionary

    # Expand the 'Package' dictionary into separate columns
    package_df = df['Package'].apply(pd.Series)

    # Merge the new columns with the original DataFrame
    df = df.drop('Package', axis=1).join(package_df)

    # Save the DataFrame to an Excel file
    output_file = 'customer_data.xlsx'
    df.to_excel(output_file, index=False)

    print(f"Data has been saved to {output_file}")

if __name__ == '__main__':
    main()