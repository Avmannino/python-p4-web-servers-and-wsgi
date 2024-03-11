#!/usr/bin/env python3
from werkzeug.wrappers import Request, Response

@Request.application # Runs any code inside of the function in the browser at the location we specify with our development server
def application(request):
    print(f'This web server is running at {request.remote_addr}')
    return Response('A WSGI generated this response!')

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple(  # This method runs a server for a one-page application without complications.
        hostname='localhost',
        port=5555,
        application=application
    )
    
    # Run server requires 3 arguments:
    # - a hostname (localhost)
    # - a port  (5555)
    # - an application (this will be defined in a function somewhere in the file- we named ours "application")
    
    # run "python server/werkzeug_app.py" in the terminal
    