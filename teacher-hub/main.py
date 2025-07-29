# Teacher hub main
cat > teacher-hub/main.py << 'EOF'
#!/usr/bin/env python3
"""
Classroom Cube System - Teacher Hub
"""
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("🎲 Classroom Cube Teacher Hub starting...")
    logger.info("✅ Teacher Hub ready! (Basic version)")
    
    # Keep running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
EOF

# Cube client main
cat > cube-client/main.py << 'EOF'
#!/usr/bin/env python3
"""
Classroom Cube System - Cube Client
"""
import asyncio
import logging
import sys

# Handle hardware gracefully
try:
    import RPi.GPIO as GPIO
    HARDWARE_AVAILABLE = True
except ImportError:
    try:
        import fake_rpi.RPi as RPi
        import fake_rpi.RPi.GPIO as GPIO
        HARDWARE_AVAILABLE = False
        print("⚠️ Running in simulation mode")
    except ImportError:
        print("❌ No GPIO available. Install fake-rpi for development.")
        sys.exit(1)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    logger.info("🎲 Classroom Cube Client starting...")
    
    if '--simulation' in sys.argv:
        logger.info("🔧 Running in simulation mode")
    
    logger.info("✅ Cube ready! (Basic version)")
    
    # Keep running
    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
EOF

# Make scripts executable
chmod +x teacher-hub/main.py cube-client/main.py