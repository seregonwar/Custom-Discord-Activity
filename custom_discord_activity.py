from pypresence import Presence
import time

client_id = 'YOUR_CLIENT_ID'
RPC = Presence(client_id)
RPC.connect()

def update_presence():
    try:
        RPC.update(
            state="Playing as Lucia",
            details="Exploring South Beach",
            large_image="photo1",
            large_text="Grand Theft Auto VI",
            start=time.time()
        )
        print("Rich Presence updated successfully.")
    except Exception as e:
        print(f"Error updating Rich Presence: {e}")

if __name__ == "__main__":
    try:
        update_presence()
        print("Rich Presence activated. Press Ctrl+C to terminate.")
        
        while True:
            time.sleep(15)
    except KeyboardInterrupt:
        print("Rich Presence terminated.")
    finally:
        RPC.close()
