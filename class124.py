from flask import Flask,jsonify

app=Flask(__name__)

tasks=[
    {
        id:1,
        'title':'buy grocery',
        'description':'milk,cheese,fruit',
        'done':False,           
    },

    {
        id:2,
        'title':'learn python',
        'description':'need to find a good python tutorial on web',
        'done':False,

    }
]

@app.route('/add-data',methods=['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status':'error',
            'message':'please provide the data'
        },
            400
        )

    task={
        id:tasks[-1]['id']+1,
        'title':request.json['title'],
        'description':request.json.get('description',''),
        'done':False,           
    },
    tasks.append(task)
    return jsonify({
        'status':'success',
        'message':'task has been done successfully'
    })
@app.route('/get_data')
def get_task():
    return jsonify({
        'data':'tasks'
    })
    
if __name__ == '__main__':
    app.run(debug=True)