import webview
from app import app
import threading
import sys
import os

def start_server():
    """Start Flask server in background thread"""
    app.run(host='127.0.0.1', port=5000, debug=False, use_reloader=False)

def main():
    """Main function to start the desktop application"""
    print("Starting Shopee Link Converter...")
    
    # Start Flask server in background
    t = threading.Thread(target=start_server)
    t.daemon = True
    t.start()
    
    # Wait a moment for server to start
    import time
    time.sleep(1)
    
    # Create desktop window
    webview.create_window(
        'Shopee Link Converter', 
        'http://127.0.0.1:5000',
        width=1000,
        height=700,
        resizable=True,
        text_select=True
    )
    webview.start()

if __name__ == '__main__':
    main()
