import traceback
try:
    from app import app
    
    app.run(host='0.0.0.0', debug= True)
    #app.run(host='0.0.0.0', port=5000)
except:
    traceback.print_exc()
    input('Failed to  run a server ;-( Press any key to continue...')
#'192.168.1.105'
