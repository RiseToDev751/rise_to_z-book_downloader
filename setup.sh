#!/bin/bash
Kirmizi='\033[31m'

if [[ $(echo $USER) != "root" ]] ; then
    echo -e   ${Kirmizi} " 
            Please Put Sudo Before Command!!!
             
            Example Usage: sudo setup.sh
             
             "
    exit
    fi

sudo apt update && sudo apt upgrade -y 
sudo apt install git -y 
git clone https://github.com/RiseToDev751/rise_to_z-book_downloader

