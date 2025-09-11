import pandas as pd
from pathlib import Path
import xml.etree.ElementTree as ET

class CertificateGenerator:
    def __init__(self, template_svg_path):
        self.template_svg_path = template_svg_path
        self.output_svg_path = None
        self.template_content = None
        
    def load_template(self):
        """Load the template SVG file."""
        with open(self.template_svg_path, 'r') as f:
            self.template_content = f.read()

    def _replace_placeholders(self, content, name, position=''):
        """Replace placeholders in template content."""
        return (content
                .replace('{{Name}}', name)
                .replace('{{NAME}}', name)
                .replace('{{Position}}', position)
                .replace('{{POSITION}}', position))


    def generate_certificates(self, names_csv_path, certificates_per_column=9, spacing_inches=0.1):
        """Generate certificates from the template - just use the first name as a simple example."""
        # Load data from CSV
        df = pd.read_csv(names_csv_path)
        names = df['Name'].fillna('').astype(str).tolist() if 'Name' in df.columns else df.iloc[:, 0].fillna('').astype(str).tolist()
        positions = df['Position'].fillna('').astype(str).tolist() if 'Position' in df.columns else [''] * len(names)
        
        # Just use the first name and position as an example
        if names:
            content = self._replace_placeholders(self.template_content, names[0], positions[0] if positions else '')
            with open(self.output_svg_path, 'w', encoding='utf-8') as f:
                f.write(content)

    def generate_individual_certificates(self, names_csv_path, output_directory=None, filename_prefix="Certificate - "):
        """Generate one SVG per CSV row by simple placeholder replacement."""
        df = pd.read_csv(names_csv_path)
        if 'Name' not in df.columns:
            raise ValueError("CSV must contain a 'Name' column")
        
        if self.template_content is None:
            self.load_template()

        output_dir = Path(output_directory) if output_directory else Path('.')
        output_dir.mkdir(parents=True, exist_ok=True)

        def safe_filename(value: str) -> str:
            unsafe_chars = '<>:"/\\|?*'
            return ''.join('_' if ch in unsafe_chars else ch for ch in str(value)).strip().rstrip('. ')

        for _, row in df.iterrows():
            name = str(row['Name']) if pd.notna(row['Name']) else ''
            position = str(row['Position']) if 'Position' in df.columns and pd.notna(row['Position']) else ''
            
            content = self._replace_placeholders(self.template_content, name, position)
            output_path = output_dir / f"{filename_prefix}{safe_filename(name)}.svg"
            
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(content)

def main():
    template_path = "template.svg"
    names_path = "names.csv"
    
    generator = CertificateGenerator(template_path)
    generator.generate_individual_certificates(names_path)

if __name__ == "__main__":
    main() 