## Steps to run the code
- Create a EC2 instance and conect with the instance
- Run the following command
  ```
  git clone https://github.com/sayansaha934/game-app.git
  sudo apt update
  sudo apt install -y python3 python3-pip tmux
  cd backend
  pip install -r requirements.txt
  tmux new -s backend (to create a new session)
  python3 -m uvicorn main:app  --port 8000 --host 0.0.0.0 --forwarded-allow-ips=*
  ```
