import unittest
from pathlib import Path
import xml.etree.ElementTree as ET

class TestImageReferences(unittest.TestCase):
    def test_xhtml_image_paths_exist(self):
        repo_root = Path(__file__).resolve().parents[1]
        text_dir = repo_root / 'src' / 'epub' / 'text'
        images_dir = repo_root / 'src' / 'epub' / 'images'
        ns = {'xhtml': 'http://www.w3.org/1999/xhtml'}

        missing = []
        for xhtml_file in sorted(text_dir.glob('*.xhtml')):
            tree = ET.parse(xhtml_file)
            for img in tree.findall('.//xhtml:img', namespaces=ns):
                src = img.get('src')
                if src and src.startswith('../images/'):
                    rel_path = src[len('../images/'):]
                    if not (images_dir / rel_path).exists():
                        missing.append(f"{xhtml_file}: {src}")

        if missing:
            self.fail('Missing image files:\n' + '\n'.join(missing))

if __name__ == '__main__':
    unittest.main()

