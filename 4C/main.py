import os
import pandas as pd 
import numpy as np
import csv 
import time 
from datetime import datetime
import subprocess
import shutil
from git import Repo
from git import exc
import logging 

#logging for main.py
logging.basicConfig(filename='mainlogging.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def giveTimeStamp():
    logging.info("Function giveTimeStamp started.")
    tsObj = time.time()
    strToret = datetime.fromtimestamp(tsObj).strftime('%Y-%m-%d %H:%M:%S')
    #logging to return the given timestamp
    logging.info("Returning timestamp: {}".format(strToret))
    return strToret
  

def deleteRepo(dirName, type_):
    logging.info(f"Function deleteRepo called with dirName: {dirName}, type_: {type_}")

    try:
        if os.path.exists(dirName):
            shutil.rmtree(dirName)
            logging.info(f"Successfully deleted directory: {dirName}")
        else:
            logging.warning(f"Directory not found: {dirName}")
    
    except OSError as e:
        logging.error(f"Error deleting directory: {dirName}. Error: {e}")
        print("Failed to delete directory, will try manually.") 
        
        
def dumpContentIntoFile(strP, fileP):
    #log information about dump
    logging.info("Entering dumpContentIntoFile function with file: {}".format(fileP))
    with open(fileP, 'w') as fileToWrite:
        fileToWrite.write(strP)
	#getting all content 
        logging.info("Content dumped into file: {}".format(fileP))
        return str(os.stat(fileP).st_size)
  
  
def makeChunks(the_list, size_):
    #get info about the make chunks
    logging.info("Getting makeChunks function. List size: {}, Chunk size: {}".format(len(the_list), size_))
    for i in range(0, len(the_list), size_):
        yield the_list[i:i + size_]
    #clsoing makeChunks function
    logging.info("Closing/Exiting makeChunks function.")

        
def cloneRepo(repo_name, target_dir):
    #getting info about clonerepo
    logging.info("Getting cloneRepo function. Cloning repo: {}, to directory: {}".format(repo_name, target_dir))
    cmd_ = "git clone " + repo_name + " " + target_dir 
    try:
        subprocess.check_output(['bash','-c', cmd_]) 
	#success logging  
        logging.info("Successfully cloned repo: {}".format(repo_name))
    #set error to e
    except subprocess.CalledProcessError as e:
	#get errors
        logging.error("Error cloning repo: {}. Error: {}".format(repo_name, e))
        print('Skipping this repo ... trouble cloning repo:', repo_name)
        

def getDevEmailForCommit(repo_path_param, hash_):
    #getting the info about email for commit
    logging.info("Entering getDevEmailForCommit function with repo_path: {}, commit hash: {}".format(repo_path_param, hash_))
    author_emails = []
    cdCommand = "cd " + repo_path_param + " ; "
    commitCountCmd = " git log --format='%ae'" + hash_ + "^!"
    command2Run = cdCommand + commitCountCmd

    try:
        author_emails = str(subprocess.check_output(['bash','-c', command2Run]))
        author_emails = author_emails.split('\n')
        author_emails = [x_.replace(hash_, '') for x_ in author_emails if x_ != '\n' and '@' in x_]
        author_emails = [x_.replace('^', '') for x_ in author_emails if x_ != '\n' and '@' in x_]
        author_emails = [x_.replace('!', '') for x_ in author_emails if x_ != '\n' and '@' in x_]
        author_emails = [x_.replace('\\n', ',') for x_ in author_emails if x_ != '\n' and '@' in x_]
        
        author_emails = author_emails[0].split(',')
        author_emails = [x_ for x_ in author_emails if len(x_) > 3]
        author_emails = list(np.unique(author_emails))
	#found some emails
        logging.info("Found emails: {}".format(author_emails))
    #set error to e
    except subprocess.CalledProcessError as e:
	#get errors from function
        logging.error("Get error commit details for hash: {}. Error: {}".format(hash_, e))
    return author_emails  

def getDevDayCount(full_path_to_repo, branchName='master', explore=1000):
    #getting info
    logging.info("Getting getDevDayCount function for repo: {}".format(full_path_to_repo))
    repo_emails = []
    all_commits = []
    all_time_list = []

    if os.path.exists(full_path_to_repo):
        repo_ = Repo(full_path_to_repo)
        try:
            all_commits = list(repo_.iter_commits(branchName)) 
	    #success  
            logging.info("Total commits found: {}".format(len(all_commits)))
	#setting error as e
        except exc.GitCommandError as e:
	    #get the errors
            logging.error("Error accessing repository: {}. Error: {}".format(full_path_to_repo, e))

        for commit_ in all_commits:
            commit_hash = commit_.hexsha
            emails = getDevEmailForCommit(full_path_to_repo, commit_hash)
            repo_emails = repo_emails + emails

            timestamp_commit = commit_.committed_datetime
            str_time_commit = timestamp_commit.strftime('%Y-%m-%d')
            all_time_list.append(str_time_commit)

    all_day_list = [datetime(int(x_.split('-')[0]), int(x_.split('-')[1]), int(x_.split('-')[2]), 12, 30) for x_ in all_time_list]
    try:
        min_day = min(all_day_list) 
        max_day = max(all_day_list) 
        ds_life_days = (min_day - max_day).days
	#Repo life span 
        logging.info("Repo life span: {} days.".format(ds_life_days))
    #set error as e
    except (ValueError, TypeError) as e:
        ds_life_days = 0
	#get the errors
        logging.error("Error calculating repo life span. Error: {}".format(e))
        
    ds_life_months = round(float(ds_life_days)/float(30), 5)
    #format life span
    logging.info("Repo life span in months: {}".format(ds_life_months))
    
    return len(repo_emails), len(all_commits), ds_life_days, ds_life_months 
