from abstract_data_type import Deque
def decode_html(html_expr):
    """Convert html expr to normal reading"""
    result = []
    content_deque = Deque()
    i = 0
    while i < len(html_expr):
        token = html_expr[i]
        if html_expr[i:i+6] == '<html>':
            content_deque.addRear('<html>')
            i += 6

            
        elif html_expr[i:i+6] == '<head>':
            content_deque.addRear('<head>')
            i += 6


        elif html_expr[i:i+7] == '<title>':
            content_deque.addRear('<title>')
            i += 7
            
            
        elif html_expr[i:i+8] == '</title>':
            content_deque.addRear('</title>')
            loading = ''
            content_deque.removeFront()
            token = content_deque.removeFront()
            while token != '</title>':
                loading += token
                token = content_deque.removeFront()
            result.append(('title', loading))
            i += 8
            
            
        elif html_expr[i:i+7] == '</head>':
            content_deque.addRear('</head>')
            loading = ''
            content_deque.removeFront()
            token = content_deque.removeFront()
            while token != '</head>':
                loading += token
                token = content_deque.removeFront()
            
            result.append(('head', loading))         
            i += 7
            
            
        elif html_expr[i:i+7] == '</html>':
            print(content_deque.items)
            content_deque.removeFront()
            content_deque.addRear('</html>')
            loading = ''
            token = content_deque.removeFront()
            while token != '</html>':
                loading += token
                token = content_deque.removeFront()
            
            result.append(('body', loading))
            html_print(result)
            break
            
        else:
            content_deque.addRear(token)
            i += 1
            
            
            
            

def html_print(html_tuples):
    for typ, content in html_tuples:
        print('=' * 20)
        print(typ + ':')
        print(content)
        print('=' * 20)
        
html_expr = """<html>Hi</html>"""
decode_html(html_expr)

