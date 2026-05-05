import os
import pandas as pd


def encode_excel(input_path):
    """
    Read an Excel file, convert categorical/text columns to numeric columns
    using one-hot encoding, and save the new file in the same directory
    with '-encoded' added to the file name.
    """

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found: {input_path}")

    # Read Excel file
    df = pd.read_excel(input_path)

    # Detect categorical columns
    categorical_columns = df.select_dtypes(include=["object", "category"]).columns

    print("Categorical columns found:")
    print(list(categorical_columns))

    # Apply one-hot encoding zz
    df_encoded = pd.get_dummies(df, columns=categorical_columns)

    # Create output path (same folder, new name)
    folder = os.path.dirname(input_path)
    filename = os.path.basename(input_path)

    name, ext = os.path.splitext(filename)

    output_path = os.path.join(folder, f"{name}-encoded{ext}")

    # Save file
    df_encoded.to_excel(output_path, index=False)

    print(f"✅ Done! File saved at: {output_path}")


if __name__ == "__main__":
    input_file = input("Enter path to your Excel file: ")

    encode_excel(input_file)
#done!
