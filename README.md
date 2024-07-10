# Custom-Discord-Activity

This repository provides a practical example of integrating Discord Rich Presence using the `pypresence` library. Rich Presence enhances user experience by dynamically updating game status information on Discord profiles.

## Key Features

### Initialization and Connection

```python
from pypresence import Presence
import time

# Replace with your own Discord Client ID
client_id = 'YOUR_CLIENT_ID'
RPC = Presence(client_id)
RPC.connect()
```

This code block initializes and connects your program to Discord using your application's Client ID.

### Updating Game Status

```python
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
```

The `update_presence()` function dynamically updates the game status on Discord. Customize attributes like `state`, `details`, `large_image`, and `large_text` to reflect the currently played game and other relevant information.

### Continuous Update Loop

```python
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
```

This code segment keeps Rich Presence active through a continuous update loop. Adjust `time.sleep(15)` to customize the update frequency.

## How to Use

1. **Initial Setup**: Ensure Python and `pypresence` are installed. Replace `client_id` with your Discord Client ID in the initialization.

2. **Customize Activity**: Modify parameters in `RPC.update()` within `update_presence()` to update game status and activity details.

3. **Running the Program**: Execute the Python script. Rich Presence will be activated and updated automatically on Discord.

This project serves as an essential guide for developers interested in implementing and customizing Rich Presence in their applications, enhancing visibility and engagement on Discord.


## Example
![image](https://github.com/seregonwar/Custom-Discord-Activity/assets/109359355/92b964f7-cb37-475e-8df8-f52041faac3b)
