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
        print('Usage: add <source_hostname> <source_port> <destination_hostname> <destination_port>')
        continue

      master_server.add_connection(args[1], int(args[2]), args[3], int(args[4]))

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

    elif command == 'find_private':
      if len(args) < 2:
        print('Usage: find_private <id>')
        continue

      master_server.findPrivate(int(args[1]))

    elif command == 'send':
      if len(args) < 3:
        print('Usage: send <id> <message>')
        continue

      master_server.sendMessage(int(args[1]), args[2])

    elif command == 'help':
      print('Available commands:')
      print('  add <source_hostname> <destination_hostname> <destination_port>')
      print('  remove <id>')
      print('  intercept <id>')
      print('  stop_intercepting <id>')
      print('  find_private <id>')
      print('  list')
      print('  quit')

    elif command == 'list':
      print(master_server)
      
  except Exception as e:
    print(e)