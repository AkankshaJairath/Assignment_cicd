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