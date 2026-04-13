import asyncio
import websockets

async def handler(websocket, path):
    print("A client connected!")
    try:
        async for message in websocket:
            print(f"Received message: {message}")
            # Echo the message back to the client
            await websocket.send(f"Server received: {message}")
    except websockets.exceptions.ConnectionClosed:
        print("A client disconnected.")

# Start the server on localhost port 8765
# start_server = websockets.serve(handler, "localhost", 8765)
# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()