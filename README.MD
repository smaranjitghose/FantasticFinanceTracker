# Fantastic Finance Tracker 💸

A minimalistic application to track one's finances over a period built using Python

<p align = "center"><img src = "./assets/wallet.gif" height = 300 alt = "Wallet Icon"></p>

## Set-Up ⚒️

- Ensure you have the latest stable version of [Python](https://www.python.org/downloads/) in your system

- Open your terminal / command prompt. 

- Clone the repository 
    ```
    git clone https://github.com/smaranjitghose/FantasticFinanceTracker.git
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

- Create a `secrets.toml` file inside the `.streamlit` sub-directory

```
 touch .streamlit/secrets.toml
```

- Open the `secrets.toml` file, create a variable `deta_key` and assign in to value of the copied project key. Save the file

```
deta_key = "your_deta_project_key"
```

- Load the application

    ```
    streamlit run Home.py
    ```

- If the app does not load by itself in your default browser, open a browser of your choice and navigate to  `http://localhost:80`

- To stop the application, press `CTRL + C` in your terminal

## Demo 👇

[Click Here 🔗](https://smaranjitghose-fantasticfinancetracker-home-7p438y.streamlit.app/)

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

## Note ✏️
- For Streamlit Sharing, mentioning versions of the modules in requirements throws error at times
- Error 401: If project key is changed/removed in the Deta Dashboard (Free Tier issues)