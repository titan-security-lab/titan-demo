from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    """
    VULNERABLE: Cross-Site Scripting (XSS)
    Attacker can inject: <script>alert('XSS')</script>
    """
    query = request.args.get('q', '')
    
    # No sanitization - VULNERABLE!
    return f"<h1>Search results for: {query}</h1>"
