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



@api.route('/repos', methods=['GET'])
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

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/api-map", methods=['GET'])
def site_map():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        methods = []
        for m in rule.methods:
            meth = urllib.parse.unquote("{}".format(m))
            if m not in ('OPTIONS','HEAD'):
                methods.append(meth)
        line = {
            'methods': methods,
            'rule': urllib.parse.unquote("{}".format(rule))
        }
        if '/api/' in urllib.parse.unquote("{}".format(rule)):
            output.append(line)
        else:
            continue
    return jsonify(links=output)

if __name__ == '__main__':
    manager.run()
