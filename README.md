# Certificate Generator

This Python application generates certificates from an SVG template. It now creates one SVG file per CSV row with simple placeholder replacement.

## Requirements

- Python 3.7 or higher
- Required packages (install using `pip install -r requirements.txt`):
  - svgwrite
  - pandas
  - lxml

## Usage

1. Prepare your files:
   - Create an SVG template file with these placeholders:
     - `{{Name}}`
     - `{{Position}}` (optional)
   - Create a CSV file with headers `Name` and optionally `Position`

2. Run the application:
   ```bash
   python nametag_generator.py
   ```

3. The application will:
   - Read the template SVG file
   - Replace `{{Name}}` and `{{Position}}` using values from each CSV row
   - Save a separate SVG file for each row named `Certificate - <Name>.svg`

## File Structure

- `template.svg`: SVG template containing `{{Name}}` and optionally `{{Position}}`
- `names.csv`: CSV file containing at least a `Name` column, and optional `Position`
- `Certificate - <Name>.svg`: Generated per-person SVG files in the project folder

## Customization

You can modify the following parameters in the code:
- Output directory and filename prefix for generated files (via parameters of `generate_individual_certificates`)

## Example

1. Create a template.svg file:
```svg
<svg width="100" height="50" viewBox="0 0 100 50">
  <rect width="100" height="50" fill="white" stroke="black"/>
  <text x="50" y="20" text-anchor="middle" dominant-baseline="middle">{{Name}}</text>
  <text x="50" y="35" text-anchor="middle" dominant-baseline="middle">{{Position}}</text>
</svg>
```

2. Create a names.csv file:
```csv
Name,Position
John Doe,Course Director
Jane Smith,ASM - Program
Bob Johnson,Scribe
```

3. Run the application to generate per-person SVG files named like `Certificate - John Doe.svg`.