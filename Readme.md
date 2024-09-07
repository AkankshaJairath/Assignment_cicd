# Assignment_cicd
Building CI-CD Pipeline Tool

Create a complete CI-CD pipeline using bash, python, and crontabs. The list of tasks is specified below: 

Task 1: Set Up a Simple HTML Project 
Create a simple HTML project and push it to a GitHub repository. 

Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx

Task 3: Write a Python Script to Check for New Commits
Create a Python script to check for new commits using the GitHub API.

Task 4: Write a Bash Script to Deploy the Code
Create a bash script to clone the latest code and restart Nginx.

Task 5: Set Up a Cron Job to Run the Python Script
Create a cron job to run the Python script at regular intervals.

Task 6: Test the Setup 
Make a new commit to the GitHub repository and check that the changes are automatically deployed. 

## Execution

To start contributing to this project, please follow the below steps:



1. **Clone  Repository**
   - Clone the repository to your local machine using the following command:
     ```bash
     git clone https://github.com/AkankshaJairath/Assignment_cicd.git
     ```

3. **Change the current directory to the Project Directory**
   - Change into the project directory:
     ```bash
     cd Assignment_cicd
     ```

4. **Create New Branch**
   - Create a new branch to make your changes:
     ```bash
     git checkout -b my-branch
     ```

5. **Make Changes**
   - Place html file or modify.

6. **Commit Changes**
     ```bash
     git add .
     git commit -m "Describe your changes here"
     ```

7. **Push Changes**
     ```bash
     git push origin my-branch
     ```


## Local Ubuntu Instance with Nginx ##

**install Nginx**
    - Go to Ubuntu system on local , Install Nginx 

1. **Install nginx**
   - Install nginx :
     ```bash
     sudo apt-get install nginx -y
     ```
2. **Enable nginx**
   - Enable nginx :
     ```bash
     sudo systemctl enable nginx
     ```
3. **check status of nginx**
   - Check nginx :
     ```bash
     sudo systemctl status nginx
     ```
4. **start nginx**
   - start nginx :
     ```bash
     sudo systemctl start nginx
     ```


## Create Project Dir cicd_project , deploy file and check commit file :
   - Create below file:
     ```bash
     mkdir cicd_project
     cd cicd_project
     touch check_commits.py
     touch deploy.sh
     ```

## Python Script to Check for New Commits
    - Add the below content to check_commit.py file
   ```bash
      import requests
      import os

      # Replace these variables with your own repository details
      repo_owner = 'AkankshaJairath'
      repo_name = 'Assignment_cicd'
      branch_name = 'main' 
      commit_file = '/mnt/p/Vscode/Devops/cicd_project/lastcommit_sha.txt'  # File to store the last checked commit SHA

      # GitHub API URL for commits
      github_api = f'https://api.github.com/repos/{repo_owner}/{repo_name}/commits?sha={branch_name}'

      def get_latest_commit():
         response = requests.get(github_api)
    
         if response.status_code == 200:
            commit_ids = response.json()
            latest_sha = commit_ids[0]['sha']  # Access the first commit's SHA
            return latest_sha
         else:
            print(f"Failed to fetch commit id: {response.status_code}")
            return None

      def read_latest_commit():
         if os.path.exists(commit_file):
            with open(commit_file, 'r') as file:
                  return file.read().strip()
         return None

      def write_last_commit_sha(sha):
         with open(commit_file, 'w') as file:
            file.write(sha)

      def main():
         latest_sha = get_latest_commit()
    
         if latest_sha:
            last_sha = read_latest_commit()
        
         if latest_sha != last_sha:
            print(f"New commit detected! Latest SHA: {latest_sha}")
            write_last_commit_sha(latest_sha)
            # Trigger deployment (call deploy script here)
            os.system('/mnt/p/Vscode/Devops/cicd_project/deploy.sh')
         else:
            print("There are no new commits available.")
         else:
            print("Could not retrieve commit info.")

      if __name__ == '__main__':
         main()
   ```


## Bash Script to Deploy the Code ##
    - Add the below content to deploy.sh file
   ```bash
     #!/bin/bash

      # Var
      repo="https://github.com/AkankshaJairath/Assignment_cicd"
      local_dir="/mnt/p/Vscode/Devops/cicd_project/Assignment_cicd"

      echo "Checking if directory exists: $local_dir"

      # Clone the repo (or pull if it already exists)
      if [ ! -d "$local_dir" ]; then
         echo "Cloning repo $repo..."
         git clone "$repo" "$local_dir"
      else
         echo "Directory exists. Pulling latest changes..."
      cd "$local_dir" || exit
      git pull
      fi

      # Check if clone or pull succeeded
      if [ $? -ne 0 ]; then
      echo "Error in cloning or pulling repository."
      exit 1
      fi
      # Copy the updated index.html file to Nginx root directory
      echo "Copying index.html to /var/www/html/"
      sudo cp "$local_dir/index.html" /var/www/html/

      # Check if copy succeeded
      if [ $? -ne 0 ]; then
         echo "Error in copying index.html."
         exit 1
      fi
      # Restart Nginx to apply changes
      echo "Restarting Nginx..."
      sudo systemctl restart nginx

      # Check if restart succeeded
      if [ $? -ne 0 ]; then
         echo "Error in restarting Nginx."
         exit 1
      fi

      echo "Deployment completed and Nginx restarted."
   ```

## File Persimissions 
   ```bash
   chmod +x /mnt/p/Vscode/Devops/cicd_project/deploy.sh
   ```

##  CronJob to check commits in every 5 mins

1. **To edit the cronjob**
   - Edit the crontab with below command:
     ```bash
     cronejob -e
     ```
2. **Modified and create the job**
   - To Modified:
     ```bash
     */5 * * * * /usr/bin/python3 /mnt/p/Vscode/Devops/cicd_project/check_commits.py >> /mnt/p/Vscode/Devops/cicd_project/check_commits.log 2>&1 
     ```

