import sys
import subprocess
import time

def main():
    if len(sys.argv) != 3:
        print("Usage: python client.py [IPv4 address] [port number]")
        sys.exit(1)

    ip_address = sys.argv[1]
    port = sys.argv[2]
    total_response_time = 0

    for _ in range(5):
        start_time = time.time()
        curl_command = f"curl -s -o /dev/null -w '%{{time_total}}\n' {ip_address}:{port}"
        response = subprocess.run(curl_command, shell=True, capture_output=True, text=True)
        
        # Check if curl command was successful
        if response.returncode == 0:
            response_time = float(response.stdout.strip())
            total_response_time += response_time
            #print(f"Response time: {response_time}s")
        else:
            print("Failed to execute curl command")
            sys.exit(1)

    average_response_time = total_response_time / 5
    print(f"Average response time: {average_response_time}s")

if __name__ == "__main__":
    main()
