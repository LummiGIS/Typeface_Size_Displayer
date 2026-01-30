import os

def create_typeface_html():
    # 1. Get the typeface name from the user
    typeface = input("Enter the typeface name (e.g., Arial, Times New Roman, Verdana): ").strip()
    
    # 2. Setup the directory and file path
    target_dir = r"C:\Temp"
    if not os.path.exists(target_dir):
        try:
            os.makedirs(target_dir)
        except Exception as e:
            print(f"Error creating directory: {e}")
            return

    # The file will be named after the typeface (e.g., Arial.html)
    file_path = os.path.join(target_dir, f"{typeface}.html")
    
    # 3. Define the point sizes requested
    sizes = [6, 8, 10, 12, 14, 16, 20, 24, 34, 45, 72]
    
    # 4. Generate the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{typeface} Sample</title>
        <style>
            body {{
                font-family: '{typeface}', sans-serif;
                margin: 40px;
                line-height: 1.2;
            }}
            .sample-line {{
                display: block;
                margin-bottom: 10px;
            }}
        </style>
    </head>
    <body>
    """
    
    for size in sizes:
        html_content += f'    <div class="sample-line" style="font-size: {size}pt;">{typeface} {size}</div>\n'
    
    html_content += """
    </body>
    </html>
    """
    
    # 5. Write the file to C:\Temp
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
        print(f"\nSuccess! Your file has been created at: {file_path}")
        print("Double-click the file to view it in your browser.")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

if __name__ == "__main__":
    create_typeface_html()