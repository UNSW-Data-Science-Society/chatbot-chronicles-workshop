css = '''
<style>

.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    color: white;
    padding: 10px;
    text-align: center;
}

.btn-tech-stack {
    display: inline-block;
    padding: 10px 20px;
    font-size: 16px;
    text-align: center;
    text-decoration: none;
    margin: 5px 2px;
    cursor: pointer;
    border-radius: 4px;
    background-color: #4CAF50;
    color: white;
}

.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    align-items: center; 
}

.chat-message.user {
    background-color: #2b313e
}

.chat-message.bot {
    background-color: #475063
}

.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}

/* Media queries for responsiveness */
@media (max-width: 768px) {
    .btn-tech-stack {
        padding: 8px 16px;
        font-size: 14px;
    }

    /* Add more adjustments as needed */
}

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/R30gsMV/robot.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/37RZbFv/human.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''

tech_stack_buttons_1 = '''
<div class="footer">
    <p style="color: black;">Built with:</p>
    <button class="btn btn-python">Python</button>
    <button class="btn btn-langchain">Langchain</button>
    <button class="btn btn-openai">OpenAI</button>
    <button class="btn btn-streamlit">Streamlit</button>
</div>
'''


tech_stack_buttons_2 = '''
<div class="footer">
    <p style="color: black;">Built with:</p>
    <button class="btn btn-python">Python</button>
    <button class="btn btn-langchain">Langchain</button>
    <button class="btn btn-hf">HuggingFace</button>
    <button class="btn btn-streamlit">Streamlit</button>
</div>
'''


'''
# template to add background image 
[ data-testid="stAppViewContainer"] {
    background-image: url("https://images.pexels.com/photos/1296726/pexels-photo-1296726.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2");

    background-size: cover;
}
'''