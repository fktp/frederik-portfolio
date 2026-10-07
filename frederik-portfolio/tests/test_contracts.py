import importlib.util
import json
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("risk", ROOT / "scripts/risk.py")
risk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(risk)

class RiskPolicyTests(unittest.TestCase):
    def test_workflow_and_dependencies_are_high(self):
        for path in [".github/workflows/portfolio.yml", "Portfolio.csproj", "packages.lock.json", "wwwroot/staticwebapp.config.json", "scripts/ai_review.py"]:
            self.assertEqual(risk.risk_level([path]), "HIGH")
    def test_high_takes_precedence(self):
        self.assertEqual(risk.risk_level(["Home.razor", ".github/workflows/test.yml"]), "HIGH")
    def test_application_code_is_medium(self):
        self.assertEqual(risk.risk_level(["Home.razor"]), "MEDIUM")
    def test_copy_and_styles_are_low(self):
        self.assertEqual(risk.risk_level(["README.md", "wwwroot/css/app.css"]), "LOW")

class HostingContractTests(unittest.TestCase):
    def test_framework_and_base_path(self):
        xml = ET.parse(ROOT / "Portfolio.csproj")
        self.assertEqual(xml.findtext("PropertyGroup/TargetFramework"), "net10.0")
        self.assertIn('<base href="/"', (ROOT / "wwwroot/index.html").read_text())
    def test_security_headers_and_fallback(self):
        config = json.loads((ROOT / "wwwroot/staticwebapp.config.json").read_text())
        self.assertEqual(config['navigationFallback']['rewrite'], '/index.html')
        self.assertIn('/_framework/*', config['navigationFallback']['exclude'])
        self.assertEqual(config['globalHeaders']['X-Content-Type-Options'], 'nosniff')
        self.assertIn("frame-ancestors 'none'", config['globalHeaders']['Content-Security-Policy'])
    def test_project_ids_unique(self):
        projects = json.loads((ROOT / "Data/projects.json").read_text())
        self.assertEqual(len({p['Id'] for p in projects}), len(projects))
        self.assertEqual({p['Category'] for p in projects}, {'Sikkerhed','Udvikling','Robotik'})
