# Fantastic Finance Tracker 💸

A minimalistic application to track one's finances over a period built using Python

<p align = "center"><img src = "./assets/wallet.gif" height = 300 alt = "Wallet Icon"></p>

## Set-Up ⚒️

- Ensure you have the latest stable version of [Python](https://www.python.org/downloads/) in your system

- Open your terminal / command prompt. 

- Clone the repository 
    ```
    git clone https://github.com/smaranjitghose/fantasticqrcode
    ```
- Change the directory to the cloned project
    
    ```
    cd fantasticqrcode
    ```

- Install the dependencies

    ```
    pip install -r requirements.txt
    ```

- Create an environment file

```
touch .env
```

- Open the ```.env`` file in your desired IDE and define a variable ``DETA_KEY= ""``

- Visit [Deta](https://www.deta.sh/) and Sign up for a free Account

- Login to Deta

- Create a Project and Generate Project Key. Refer to the [documentation](https://docs.deta.sh/docs/base/py_tutorial) if you face any hurdle to do so

- Copy the Project Key

- Paste it inside the environment file `.env` as the value of the variable ``DETA_KEY`` within double quotes (i.e. as a string)

- Save the `.env` file

- Open `database.py` in your desired IDE and do the following changes for obtaining the Deta Key:
    - Uncomment the lines of code under `# 1.Use this for testing in local system`
    - Comment out the line `project_key = st.secrets("DELTA_KEY")`

- Load the application

    ```
    streamlit run Home.py
    ```

- If the app does not load by itself in your default browser, open a browser of your choice and navigate to  `http://localhost:80`

- To stop the application, press `CTRL + C` in your terminal

## Future Work 🏗️

- Dockerize the Application
- Experiment with other NoSQL Databases like MongoDB and hosting options like Supabase, Atlas,etc
- Improve Data Visualization (more charts)
- Experiment with user login


## Deployment Options 🥊

**Free Tier**
- [Streamlit Cloud](https://streamlit.io/cloud)  ✔️
- [Railway](https://railway.app/)
- [Render](https://render.com/)
- [Fly](https://fly.io/)
- [Cyclic](https://app.cyclic.sh/#/)

**No Free Tier**
- [Heroku](https://www.heroku.com/)
- [Digital Ocean](https://www.digitalocean.com/)
