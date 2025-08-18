import asyncio
from pywizlight import wizlight, PilotBuilder

lamp_ip = '192.168.1.x'     
lamp_brightness = 100               # 10 - 250

async def set_lamp(state):
    lamp = wizlight(lamp_ip)
    
    if state == 'on':
        await lamp.turn_on((PilotBuilder(brightness=lamp_brightness)))
        print("Lamp is aan.")
    elif state == 'off':
        await lamp.turn_off()
        print("Lamp is uit.")

lamp_status = 'on'                # on - off


asyncio.run(set_lamp(lamp_status))

