# from app.TCP.Proxy import Proxy

# master_server = Proxy('0.0.0.0' , '127.0.0.1', 9000)
# master_server.start()

# while True:
#   try:
#     cmd = input('$ ')
#     if cmd[:4] =='quit':
#       os._exit(0)

#   except Exception as e:
#     print(e)

from app.TCP.RogueProxy import RogueProxy as Proxy
from app.Algorithms.EllipticCurves import EllipticCurve, Point
import os

curve = EllipticCurve(416,569,659)
g = Point(23,213,curve)
curve.setGenerator(g)

master_server = Proxy(curve, 9000)

while True:
  try:
    cmd = input('$ ')
    args = cmd.split(' ')
    command = args[0]

    if command == 'quit':
      os._exit(0)

    elif command == 'add':
      if len(args) < 4:
        print('Usage: add <source_hostname> <destination_hostname> <destination_port>')
        continue

      master_server.add_connection(args[1], args[2], int(args[3]))

    elif command == 'remove':
      if len(args) < 2:
        print('Usage: remove <id>')
        continue

      master_server.remove_connection(int(args[1]))

    elif command == 'intercept':
      if len(args) < 2:
        print('Usage: intercept <id>')
        continue

      master_server.start_intercepting(int(args[1]))
    
    elif command == "stop_intercepting":
      if len(args) < 2:
        print('Usage: stop_intercepting <id>')
        continue

      master_server.stop_intercepting(int(args[1]))

    elif command == 'lock':
      if len(args) < 2:
        print('Usage: intercept <id>')
        continue

      master_server.block_response(int(args[1]))
    
    elif command == "unlock":
      if len(args) < 2:
        print('Usage: stop_intercepting <id>')
        continue

      master_server.unblock_response(int(args[1]))

    elif command == 'help':
      print('Available commands:')
      print('  add <source_hostname> <destination_hostname> <destination_port>')
      print('  remove <id>')
      print('  intercept <id>')
      print('  stop_intercepting <id>')
      print('  list')
      print('  quit')

    elif command == 'list':
      print(master_server)
      
  except Exception as e:
    print(e)