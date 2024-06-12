#!/usr/bin/python3
"""
Module that contains
fetch_and_print_posts() and fetch_and_save_posts() functions
"""
import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """
    Function that fetches all post from JSONPlaceholder
    """
    r = requests.get(url)

    print(f"Status code: {r.status_code}")

    if r.status_code == 200:
        data = r.json()

        for lists in data:
            print(lists['title'])
    else:
        print("Request was not successful")


def fetch_and_save_posts():
    """
    Function that  fetches all post from JSONPlaceholder and saves it
    """
    r = requests.get(url)

    if r.status_code == 200:
        data = r.json()
        list_of_dicts = []

        for lists in data:
            response = {
                'id': lists.get('id'),
                'title': lists.get('title'),
                'body': lists.get('body')
            }

            list_of_dicts.append(response)

        with open('posts.csv', mode="w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(list_of_dicts)
    else:
        print("Request was not successful")
