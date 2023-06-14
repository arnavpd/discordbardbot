import google.generativeai as palm
import os

def get_response(message: str) -> str:
    p_message = message.lower()

    # if p_message == '!help':
    #   return 'Hey! This bot was developed by Tremo and is intended to be your personal AI. Try asking a question with "$" or send a url for a summary! If you would like your inquiry answered via DM, simply start your request with a ? as well. Feel free to send Tremo feedback on his amazing Machine Learning Model.'
      
    if p_message == 'hello':
        return 'Hey there!'
    
    if p_message.startswith('$'):
        return run_bard(p_message, False)

    # if p_message.startswith('www.') or p_message.startswith('https:'):
    #     return run_bard(p_message, True)
    # return 

def run_bard(message, isUrl):
  
    my_secret = os.environ['bard_api']
    palm.configure(api_key=my_secret)
    
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    model = models[0].name

    if isUrl:
      prompt = """scrape this website:""" + message + """if this is a discussion/forum page, summarize the main discussion thread, give me around 2-3 sentences. Additionally give me some interesting points raised in the threads and some noteworthy comments or discussions to check out. Otherwise use your initution and return me a similar type summary, for example if it's a news article, summarise the article and return interesting points and additional links to similar sites, use this type of logic for any site you encounter"""
    else:
      prompt = message +"""\n PS EXTRA: if asked who you are, or what language model you are, or what api, or anything of that sort, say you are simply Tremo, developed by a genius, dont mention palm or bard or google"""
    
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    
    return completion.result