import random
import time
import os
from config import USE_PROXY, PROXY_LIST, PROXY_ROTATE_INTERVAL

def get_proxy():
    """
    Returns the current proxy from the proxy list.
    Rotates the proxy if needed.
    """
    if USE_PROXY:
        if PROXY_LIST:
            return get_rotated_proxy()
        else:
            print("Error: Proxy is enabled, but no proxies are provided in the config.")
            return None
    else:
        return None

def get_rotated_proxy():
    """
    Rotates the proxy from the list of proxies and returns a proxy.
    A new proxy is returned based on the rotation interval.
    """
    global last_used_proxy, last_rotation_time

    # Check if it's time to rotate the proxy
    current_time = time.time()
    if current_time - last_rotation_time >= PROXY_ROTATE_INTERVAL:
        last_used_proxy = random.choice(PROXY_LIST)  # Choose a random proxy
        last_rotation_time = current_time
        print(f"Proxy rotated to: {last_used_proxy}")
    
    return last_used_proxy

def set_proxy_env(proxy):
    """
    Set environment variables for the proxy, used by tools like yt-dlp.
    """
    if proxy:
        os.environ['HTTP_PROXY'] = proxy
        os.environ['HTTPS_PROXY'] = proxy
        print(f"Proxy set to {proxy}")
    else:
        os.environ['HTTP_PROXY'] = ""
        os.environ['HTTPS_PROXY'] = ""
        print("No proxy set.")

# Initialize proxy rotation settings
last_used_proxy = None
last_rotation_time = 0

