def run_locust(host, num_users, spawn_rate, web_port):
    import subprocess
    command = f"locust -f locustfile.py --host={host} --users={num_users} --spawn-rate={spawn_rate} --web-port={web_port}"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process
