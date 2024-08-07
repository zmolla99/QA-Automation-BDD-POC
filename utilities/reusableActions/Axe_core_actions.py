from axe_selenium_python import Axe
import json

class AxeCoreActions:
    def __init__(self, driver):
        self.driver = driver
        self.axe = Axe(driver)

    def inject_axe(self):
        self.axe.inject() 

    def run_accessibility_scan(self):
        results = self.axe.run()  
        return results

    def save_scan_results(self, results, filename="axe_results.json"):
        with open(filename, 'w') as file:
            json.dump(results, file, indent=4)

    def print_violations(self, results):
        violations = results.get("violations", [])
        if violations:
            for violation in violations:
                print(f"Violation: {violation['description']}")
                print(f"Help: {violation['help']}")
                print(f"Impact: {violation.get('impact', 'No impact data')}")
                for node in violation.get("nodes", []):
                    print(f"Targeted Element: {node.get('target')}")
                    print(f"Failure Summary: {node.get('failureSummary')}")
                print("\n")
        else:
            print("No accessibility violations found.")

    def check_accessibility_violations(self):
        results = self.run_accessibility_scan()
        violations = results.get("violations", [])
        if violations:
            self.print_violations(results)
            assert False, f"Accessibility violations found: {len(violations)}"
        else:
            print("No accessibility violations found.")
