# CustomAi Assistant
This is a customizable Ai Assistant which uses Artificial Neural Networks(ANN) based Intent recognition system to recognize the intent of user input.
You can customize its responses and you can defines modules to automate something for your personal use. 

* ## Video tutorial :-
 [![Alt text](readmeContent/thumbnail.png)](link)

* ## How to use :-
  * Clone the repository
  ```shell
  git clone https://github.com/sanjaybora04/hackathon
  ```
  * Build virtual environment (Optional)
  ```shell
  python -m venv env
  ```
  now activate the environment
  ```shell
  source env/bin/activate         //for Linux
  source env/scripts/activate     //for Windows (using git bash)
  ```
  * Install required modules using "requirements.txt"
  ```shell
  pip install -r requirements.txt
  ```
  * Now your Ai Assistant is ready to use
  * You can run app.py to host your chatbot in a local server
  * Or you can use it in your own way :-
  * Just import chatbot package in your code and use chatbot.chat.reply(sentence), pass the sentence into this function and it will return the response
  * Here is a sample code for implementation of this Ai  
  ```shell
  import chatbot
  
  while True:
    sentence = input("You : ")
    print(chatbot.chat.reply(sentence))
  ```
  
  while true:
    sentence = 
* ## Configuration (if you want to customize the Assistant) :- 
  * ### For customising responses :-
    * To customise responses for assistant "chatbot/intent.json" has to be modified.
    ![image](readmeContent/intentJson.png)
    * **Tag** :- Please use a different tag for each of your intents 
    * **Pattern** :- You can enter multiple patterns and the model will be trained based on that.
    * **Responses** :- You can enter multiple responses and responses will be chosen randomely from the list.

    * After you have configured intents.json just run train.py from chatbot folder and the training process will start
    * After training is finished your assistant is ready to be used
  * ### For customising modules :-
    
    * For adding custom modules first you have to configure intents.json as mentioned(but inside responses you have to enter "module" to use the command to fire a module) as shown in image below
    ![image](readmeContent/intentjson2.png)
    * Now make a python file inside "chatbot/modules" named same as the tag you entered in the intent. **For Example** :- In the above image for DateAndTime intent you have to make a file named "DateAndTime.py" inside the module folder
    * Now as shown in image below make function reply() in your module and return the string you want the AI to give as response.
    ![image](readmeContent/module.png)
    * The returned string will be returned by the chatbot as a response and you can also perform other tasks in the function such as playing music, opening apps ,etc as well
    ![image](readmeContent/song.png)
    As you can see in this module a song is being played and "Playing song.mp3" is returned as a string
    * Let's see one more example to be clear
    ![image](readmeContent/sendMail.png) 
    * This module is using user's email credentials to send an email to someones email address
    ```
    Note: Don't forget to run train.py each time if you make any changes to "intents.json"
    ```