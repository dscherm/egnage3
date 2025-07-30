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
    
    if "--simulation" in sys.argv or not HARDWARE_AVAILABLE:
        logger.info("🔧 Running in simulation mode")
        
        # Test 5-button setup
        GPIO.setmode(GPIO.BCM)
        button_pins = [17, 18, 22, 23, 24]  # A, B, C, D, CENTER
        for pin in button_pins:
            GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        
        logger.info("✅ 5-button interface configured")
        logger.info("Buttons: A(17), B(18), C(22), D(23), CENTER(24)")
    
    logger.info("✅ Cube ready!")
    
    # Keep running
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info("Cube stopping...")
        if not HARDWARE_AVAILABLE:
            GPIO.cleanup()

if __name__ == "__main__":
    asyncio.run(main())
