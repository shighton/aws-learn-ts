import numpy as np

def Handler(event, context):
    
    arr = np.random.randint(0, 10, (3, 3))
    
    return {
        'statusCode': 200,
        'body': {
            'message': 'Hello from Lambda',
            'array': arr.tolist()
        }
    }

