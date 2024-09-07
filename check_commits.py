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

def write_lastcommit_sha(sha):
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