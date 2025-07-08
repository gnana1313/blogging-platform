#!/usr/bin/env python3
"""
Simple script to run the BlogHub application
"""

from app import app
import os

if __name__ == '__main__':
    print("🚀 Starting BlogHub...")
    print("📝 A Multi-User Blogging Platform")
    print("🌐 Access the application at: http://localhost:5000")
    print("📚 Admin panel: http://localhost:5000/admin")
    print("=" * 50)
    
    port = int(os.environ.get('PORT', 5000))
    app.run(
        host='0.0.0.0',
        port=port,
        debug=True
    ) 