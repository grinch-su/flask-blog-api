#!/usr/bin/env python3
from datetime import datetime
import os, time

from github import Github

from flask import Flask, request, jsonify, Blueprint, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Server
from flask_cors import CORS, cross_origin


# create post
@api.route('/post', methods=['POST'])
def createPost():



# get all posts
@api.route('/posts', methods=['GET'])
def getPosts():
    


# get post
@api.route('/post/<int:postId>', methods=['GET'])
def get_post(postId):


# edit post
@api.route('/post/<int:postId>', methods=['PUT'])
def updatePost(postId):



# delete post
@api.route('/post/<int:postId>', methods=['DELETE'])
def deletePost(postId):


@app.route('/repos', methods=['GET'])
def get_all_repos_with_GitHub():
    gh = Github(os.environ['APP_GITHUB_TOKEN'])
    repos = []
    for repo in gh.get_user().get_repos():
        repos.append({
            "name": repo.name,
            "updated_at": repo.updated_at,
            "homepage": repo.homepage,
            "url": repo.html_url,
            "description": repo.description,
            "lang": repo.language
        })
    return jsonify(repos=repos)

if __name__ == '__main__':
    manager.run()
