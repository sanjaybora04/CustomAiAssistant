def run(tag):
    try:
        module = __import__(tag,globals(), locals(), level=1)
        return module.reply()
    except:
        return "No module named "+tag+" in /chatbot/modules!!! or there is some error in the module, Please fix it and it will start working"