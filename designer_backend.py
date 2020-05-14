from config_designer import *

# back-end activation:
# docker run -p 80:80 -d -v /home/friend/01-github/trainer:/usr/share/nginx/html nginx

@app.route("/")
def inicio():
    return 'Designer - backend. '+\
        '<a href="/">x</a>'

# curl -d '{"img": "screenshot-1", "msg":"this is a description", "msgcoord":"100, 100", "navcoord":"200, 200", "msgboxsize":"100, 100"}' -X POST http://localhost:5000/update_line
@app.route("/update_line", methods=["post"])
def update_line():

    # get data
    json_data = request.get_json(force=True)
    # fields
    img = json_data['img']
    msg = json_data['msg'] 
    msgcoord = json_data['msgcoord']
    navcoord = json_data['navcoord']
    msgboxsize = json_data['msgboxsize']

    # mount the new line
    newline = img + "|" + msg + "|" + msgcoord + "|" + navcoord + "|" + msgboxsize + "\n"

    # load text file
    f = open('sequence.txt', 'r')
    data = f.readlines()
    f.close()

    # update the line
    for i in range(0, len(data)):
        parts = data[i].split("|")
        if parts[0] == img:
            data[i] = newline
            break
    
    #print(data)

    # remove older file
    os.remove('sequence.txt')

    # overwrite the file
    with open('sequence.txt', 'w') as f:
        for item in data:
            f.write(item)
        f.close()

    # prepare answer
    ret = jsonify({"message": "ok", "details": "line updated"})
    
    # allow call from javascript
    ret.headers.add('Access-Control-Allow-Origin', '*')        
    
    return ret

app.run(host='0.0.0.0', debug=True)