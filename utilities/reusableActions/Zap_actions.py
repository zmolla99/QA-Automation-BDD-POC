from zapv2 import ZAPv2

class ZapActions:
    def __init__(self):
        self.zap = ZAPv2()  

    def start_scan(self, target_url):
        print(f"Starting scan on {target_url}")
        scan_id = self.zap.ascan.scan(target_url)
        print(f"Scan started with ID: {scan_id}")
        return scan_id

    def get_scan_status(self, scan_id):
        status = self.zap.ascan.status(scan_id)
        print(f"Scan status: {status}%")
        return status

    def get_scan_results(self, target_url):
        print(f"Getting scan results for {target_url}")
        alerts = self.zap.core.alerts(baseurl=target_url)
        return alerts

    def print_alerts(self, alerts):
        for alert in alerts:
            print(f"Alert: {alert['alert']}")
            print(f"Description: {alert['description']}")
            print(f"Risk: {alert['risk']}")
            print(f"Message: {alert['message']}")
            print("\n")
