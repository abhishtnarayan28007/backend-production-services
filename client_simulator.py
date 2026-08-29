import requests
import time
import random
API_URL = "https://backend-production-services-production.up.railway.app/webhook/alert"
SOURCES = ["Stripe", "AuthService", "Database", "PaymentGateway", "KubernetesNode"]
PRIORITIES = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

def generate_mock_payload() -> dict:
    event_id = f"EVT-{random.randint(1000, 9999)}"
    source = random.choice(SOURCES)
    priority = random.choice(PRIORITIES)
    
    messages = [
        f"Database latency spiked above threshold in {source}.",
        f"Unauthorized access attempt detected in {source}.",
        f"High volume of failed transactions on {source}.",
        f"System health nominal, routine check completed for {source}."
    ]
    
    return {
        "event_id": event_id,
        "source": source,
        "priority": priority,
        "message": random.choice(messages)
    }
def start_simulation(count: int = 5, delay_seconds: float = 2.0) -> None:
    """Sends a specified number of simulated alert webhooks to the server."""
    print(f"🚀 Starting Deadpool Alert Simulator: Sending {count} events...")
    print("-" * 50)
    
    for i in range(1, count + 1):
        # 1. Generate random payload matching our Pydantic schema
        payload = generate_mock_payload()
        print(f"[{i}/{count}] Dispatching Event ID: {payload['event_id']} ({payload['priority']})")
        
        try:
            # 2. Fire HTTP POST request to our FastAPI endpoint
            response = requests.post(API_URL, json=payload, timeout=5)
            
            # 3. Process the server's response
            if response.status_code == 200:
                print(f"   ✅ Server Response: {response.json()}")
            else:
                print(f"   ⚠️ Server Returned Error Status: {response.status_code}")
                
        except requests.exceptions.RequestException as e:
            print(f"   ❌ Network Error: Could not connect to server at {API_URL}.")
            print(f"      Details: {e}")
            
        # 4. Pause before sending the next alert
        time.sleep(delay_seconds)

if __name__ == "__main__":
    # Run a test loop sending 5 simulated alerts spaced 2 seconds apart
    start_simulation(count=5, delay_seconds=2.0)