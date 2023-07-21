#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic."""
import pymongo


def schools_by_topic(mongo_collection, topic):
    """topic (string) will be topic searched"""
    topic_list = []
    for topic in mongo_collection.topic.find():
        topic_list.append(topic)
    return topic_list
